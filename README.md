# EPITA Group 6 – Geolocation & IP Ops

**IP Geolocation and Network Intelligence using IPInfo API**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![API](https://img.shields.io/badge/API-IPInfo_Lite-orange)
![Status](https://img.shields.io/badge/Status-In_Development-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

## 1. Project Overview

**EPITA Group 6 – Geolocation & IP Ops** is a Python-based application that integrates the IPInfo API to retrieve geographical and network information associated with IPv4 and IPv6 addresses.

The application provides an interface for retrieving IP intelligence, validating IP addresses, processing API responses and handling network-related errors.

The project is developed as part of the EPITA Engineering Tools practical assignment (TP2).

## 2. Objectives

- Retrieve public IP address information.
- Perform geolocation lookups for IPv4 and IPv6 addresses.
- Identify the country and continent associated with an IP address.
- Retrieve Autonomous System Number (ASN) information.
- Identify network organizations and associated domains.
- Implement secure API authentication.
- Handle API errors and invalid user inputs.
- Provide a Python command-line interface.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| IPInfo Lite API | IP geolocation and network intelligence |
| Requests | HTTP API communication |
| Python-dotenv | Environment variable management |
| Typer | Command-line interface |
| Pytest | Automated testing |
| Git & GitHub | Version control and collaboration |

## 4. Project Architecture

```text
epita_group6_ipops/
│
├── src/
│   └── epita_group6/
│       ├── __init__.py
│       ├── api.py
│       └── cli.py
│
├── tests/
│   ├── test_api.py
│   └── test_cli.py
│
├── README.md
├── requirements.txt
├── pyproject.toml
├── .env.example
└── .gitignore
```

### Component descriptions

- **api.py:** Handles IPInfo API communication, authentication, IP validation and error handling.
- **cli.py:** Provides command-line interaction with the application.
- **test_api.py:** Tests API integration and input validation.
- **test_cli.py:** Tests command-line functionality.
- **pyproject.toml:** Defines project metadata, dependencies and CLI configuration.
- **.env.example:** Provides an example environment configuration.

## 5. IPInfo API Integration

The project uses the IPInfo Lite API.

**API Base URL:**

```text
https://api.ipinfo.io/lite
```

**Example endpoint:**

```http
GET https://api.ipinfo.io/lite/8.8.8.8
```

Authentication is provided through an API token.

Example request:

```bash
curl "https://api.ipinfo.io/lite/8.8.8.8?token=YOUR_TOKEN"
```

### Example API Response

```json
{
  "ip": "8.8.8.8",
  "asn": "AS15169",
  "as_name": "Google LLC",
  "as_domain": "google.com",
  "country_code": "US",
  "country": "United States",
  "continent_code": "NA",
  "continent": "North America"
}
```

*Illustrative response based on the IPInfo Lite API documentation.*

## 6. Installation and Setup

### Prerequisites

- Python 3.10 or higher
- Git
- IPInfo API account
- IPInfo API token

### Clone the repository

```bash
git clone https://github.com/linghurajpr/epita_group6_ipops.git

cd epita_group6_ipops
```

### Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file:

```bash
touch .env
```

Add your API token:

```env
IPINFO_TOKEN=your_ipinfo_api_token
```

**Security:** Never commit your `.env` file or expose your API token publicly.

## 7. Running the Application

The API integration can be tested directly using Python:

```bash
PYTHONPATH=src python3 -c "from epita_group6.api import get_ip_info; print(get_ip_info('8.8.8.8'))"
```

The CLI interface will provide commands for performing IP lookups once its implementation is completed.

## 8. Testing

The project uses Pytest for automated testing.

Run the test suite:

```bash
PYTHONPATH=src pytest -v
```

Tests cover:

- IP address validation.
- Missing API credentials.
- API authentication errors.
- HTTP request failures.
- API response handling.
- CLI functionality.

## 9. Error Handling

The application is designed to handle:

- Invalid IPv4 and IPv6 addresses.
- Missing API tokens.
- Unauthorized API requests.
- API rate-limit errors.
- Network connection failures.
- Request timeouts.
- Invalid JSON responses.

## 10. Team Members

**EPITA – Group 6**

| Member | Responsibility |
|---|---|
| Daakshayani Neelamegam Senthilkumar | IPInfo API Integration |
| Linghuraj Periyaswamy Ramani | CLI Development |
| Jai Bansal | Testing and Validation |
| Hamed Yazdannejat | Documentation and Integration |

## 11. Repository

GitHub: https://github.com/linghurajpr/epita_group6_ipops

## 12. Academic Context

**Institution:** EPITA – School of Engineering and Computer Science

**Assignment:** Engineering Tools – TP2

**Group:** 6

**Project:** Geolocation & IP Ops

---

*Developed collaboratively by EPITA Group 6.*
