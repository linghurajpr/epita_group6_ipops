
import pytest
from argparse import ArgumentTypeError

from epita_group6.cli import (
    validate_ip,
    display_result,
    main,
)


def test_valid_ipv4():
    assert validate_ip("8.8.8.8") == "8.8.8.8"


def test_valid_ipv6():
    address = "2001:4860::8888"
    assert validate_ip(address) == address


def test_invalid_ip():
    with pytest.raises(ArgumentTypeError):
        validate_ip("invalid-ip")


def test_display_result(capsys):
    data = {
        "ip": "8.8.8.8",
        "asn": "AS15169",
        "as_name": "Google LLC",
        "as_domain": "google.com",
        "country_code": "US",
        "country": "United States",
        "continent_code": "NA",
        "continent": "North America",
    }

    display_result(data)

    output = capsys.readouterr().out

    assert "8.8.8.8" in output
    assert "Google LLC" in output
    assert "United States" in output


def test_missing_fields(capsys):
    display_result({"ip": "8.8.8.8"})

    output = capsys.readouterr().out

    assert "8.8.8.8" in output
    assert "Not available" in output


def test_api_failure(monkeypatch, capsys):
    def failing_api(ip):
        raise RuntimeError("Network unavailable")

    monkeypatch.setattr(
        "epita_group6.cli.get_ip_info",
        failing_api,
    )

    exit_code = main(["--ip", "8.8.8.8"])

    captured = capsys.readouterr()

    assert exit_code == 1
    assert "Error" in captured.err
