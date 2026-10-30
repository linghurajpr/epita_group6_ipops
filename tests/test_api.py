
from unittest.mock import patch, Mock
import requests
import pytest

from epita_group6.api import get_ip_info, IPInfoError


def test_get_ip_info_success():
    """Test successful IP lookup."""

    mock_response = Mock()
    mock_response.json.return_value = {
        "ip": "8.8.8.8",
        "city": "Mountain View",
        "country": "US"
    }

    mock_response.raise_for_status.return_value = None

    with patch("epita_group6.api.requests.get", return_value=mock_response):
        with patch.dict("os.environ", {"IPINFO_TOKEN": "test-token"}):
            result = get_ip_info("8.8.8.8")

    assert result["ip"] == "8.8.8.8"
    assert result["country"] == "US"


def test_invalid_ip():
    """Test invalid IP address."""

    with patch.dict("os.environ", {"IPINFO_TOKEN": "test-token"}):
        with pytest.raises(IPInfoError, match="Invalid IP address"):
            get_ip_info("not-an-ip")


def test_missing_token():
    """Test missing API token."""

    with patch.dict("os.environ", {}, clear=True):
        with pytest.raises(IPInfoError, match="IPINFO_TOKEN is missing"):
            get_ip_info("8.8.8.8")


@pytest.mark.parametrize(
    "status_code, expected_message",
    [
        (401, "Unauthorized API token"),
        (403, "Unauthorized API token"),
        (429, "API rate limit exceeded"),
        (500, "HTTP error: 500"),
    ],
)
def test_http_errors(status_code, expected_message):
    mock_response = Mock()
    mock_response.status_code = status_code
    mock_response.raise_for_status.side_effect = (
        requests.exceptions.HTTPError()
    )

    with patch.dict("os.environ", {"IPINFO_TOKEN": "test-token"}):
        with patch(
            "epita_group6.api.requests.get",
            return_value=mock_response,
        ):
            with pytest.raises(IPInfoError, match=expected_message):
                get_ip_info("8.8.8.8")


def test_request_timeout():
    with patch.dict("os.environ", {"IPINFO_TOKEN": "test-token"}):
        with patch(
            "epita_group6.api.requests.get",
            side_effect=requests.exceptions.Timeout,
        ):
            with pytest.raises(IPInfoError, match="Request timed out"):
                get_ip_info("8.8.8.8")


def test_connection_error():
    with patch.dict("os.environ", {"IPINFO_TOKEN": "test-token"}):
        with patch(
            "epita_group6.api.requests.get",
            side_effect=requests.exceptions.ConnectionError,
        ):
            with pytest.raises(
                IPInfoError,
                match="Could not connect to IPInfo",
            ):
                get_ip_info("8.8.8.8")


def test_invalid_json_response():
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.side_effect = ValueError("Invalid JSON")

    with patch.dict("os.environ", {"IPINFO_TOKEN": "test-token"}):
        with patch(
            "epita_group6.api.requests.get",
            return_value=mock_response,
        ):
            with pytest.raises(
                IPInfoError,
                match="Invalid JSON response",
            ):
                get_ip_info("8.8.8.8")


def test_ipv6_lookup():
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "ip": "2001:4860:4860::8888",
        "country": "US",
    }

    with patch.dict("os.environ", {"IPINFO_TOKEN": "test-token"}):
        with patch(
            "epita_group6.api.requests.get",
            return_value=mock_response,
        ) as mock_get:
            result = get_ip_info("2001:4860:4860::8888")

    assert result["ip"] == "2001:4860:4860::8888"
    assert "/2001:4860:4860::8888/json" in mock_get.call_args.args[0]

