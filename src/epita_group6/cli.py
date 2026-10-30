
"""Command-line interface for EPITA Group 6 IP Geolocation."""

import argparse
import ipaddress
import json
import sys

from .api import get_ip_info


def validate_ip(value):
    """Validate an IPv4 or IPv6 address."""
    try:
        ipaddress.ip_address(value)
        return value
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            f"Invalid IP address: {value}"
        ) from exc


def create_parser():
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="epita-group6-cli",
        description="Retrieve IP information using IPinfo Lite.",
    )

    parser.add_argument(
        "--ip",
        type=validate_ip,
        help="IP address to look up.",
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Display the response as JSON.",
    )

    return parser


def display_result(data):
    """Display IP information in a readable format."""
    fields = {
        "IP Address": "ip",
        "ASN": "asn",
        "Organization": "as_name",
        "Domain": "as_domain",
        "Country Code": "country_code",
        "Country": "country",
        "Continent Code": "continent_code",
        "Continent": "continent",
    }

    print("\n" + "=" * 45)
    print("       IPinfo Geolocation & IP Ops")
    print("=" * 45)

    for label, key in fields.items():
        value = data.get(key)

        if value is None or value == "":
            value = "Not available"

        print(f"{label:<18}: {value}")

    print("=" * 45)


def main(argv=None):
    """Run the command-line application."""
    parser = create_parser()
    args = parser.parse_args(argv)

    try:
        # Assumes get_ip_info(None) retrieves the current public IP.
        data = get_ip_info(args.ip)

        if not isinstance(data, dict):
            print(
                "Error: Unexpected API response.",
                file=sys.stderr,
            )
            return 1

        if args.json:
            print(json.dumps(data, indent=2))
        else:
            display_result(data)

        return 0

    except Exception as exc:
        print(
            f"Error: Unable to retrieve IP information: {exc}",
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
