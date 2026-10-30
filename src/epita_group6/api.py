import os
import ipaddress
import requests

from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://ipinfo.io"


class IPInfoError(Exception):
    """Custom exception for IPInfo API errors."""
    pass


def get_ip_info(ip_address=None):
    """Retrieve IP geolocation information from IPInfo."""

    token = os.getenv("IPINFO_TOKEN")

    if not token:
        raise IPInfoError("IPINFO_TOKEN is missing.")

    if ip_address is not None:
        try:
            ipaddress.ip_address(ip_address)
        except ValueError:
            raise IPInfoError("Invalid IP address.")

        endpoint = f"{BASE_URL}/{ip_address}/json"
    else:
        endpoint = f"{BASE_URL}/json"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    try:
        response = requests.get(
            endpoint,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if not isinstance(data, dict):
            raise IPInfoError("Unexpected API response.")

        return data

    except requests.exceptions.Timeout:
        raise IPInfoError("Request timed out.")

    except requests.exceptions.HTTPError:
        status = response.status_code

        if status in (401, 403):
            raise IPInfoError("Unauthorized API token.")

        if status == 429:
            raise IPInfoError("API rate limit exceeded.")

        raise IPInfoError(f"HTTP error: {status}")

    except ValueError:
        raise IPInfoError("Invalid JSON response.")

    except requests.exceptions.RequestException:
        raise IPInfoError("Could not connect to IPInfo.")
