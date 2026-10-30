
from unittest.mock import patch, Mock

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
