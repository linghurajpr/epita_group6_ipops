import os
import ipaddress
import requests

from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.ipinfo.io/lite"


class IPInfoError(Exception):
    """Custom exception for IPInfo API errors."""
    pass


def get_ip_info(ip_address=None):
    """Retrieve IP geolocation and network information."""

    token = os.getenv("IPINFO_TOKEN")

    if not token:
        raise IPInfoError("IPINFO_TOKEN is missing. Check your .env file.")

    if ip_address is not None:
        try:
            ipaddress.ip_address(ip_address)
        except ValueError:
            raise IPInfoError("Invalid IPv4 or IPv6 address.")

    if ip_address:
        endpoint = f"{BASE_URL}/{ip_address}"
    else:
        endpoint = f"{BASE_URL}/me"

    try:
        response = requests.get(
            endpoint,
            params={"token": token},
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if not isinstance(data, dict):
            raise IPInfoError("Unexpected API response format.")

        return data

    except requests.exceptions.Timeout:
        raise IPInfoError("Request timed out.")

    except requests.exceptions.HTTPError:
        status = response.status_code

        if status in (401, 403):
            raise IPInfoError("Invalid or unauthorized API token.")

        if status == 429:
            raise IPInfoError("API rate limit exceeded.")

        raise IPInfoError(f"IPInfo API returned HTTP {status}.")

    except requests.exceptions.RequestException:
        raise IPInfoError("Could not connect to IPInfo.")

    except ValueError:
        raise IPInfoError("Invalid JSON response.")
