# EPITA Group 6 — Geolocation & IP Operations

**IP Geolocation and Network Information Retrieval using the IPinfo API**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![API](https://img.shields.io/badge/API-IPinfo-orange)
![Testing](https://img.shields.io/badge/Testing-Pytest-green)
![Package Manager](https://img.shields.io/badge/Package_Manager-uv-purple)

## 1. Project Overview

**Geolocation & IP Operations** is a Python application developed by EPITA Group 6 as part of the Engineering Tools TP2 assignment.

The application integrates the [IPinfo API](https://ipinfo.io/) to retrieve geolocation and network information associated with public IPv4 and IPv6 addresses.

It provides a command-line interface (CLI) that allows users to retrieve information about their public IP address or specify an IP address for lookup.

The project demonstrates practical API integration, authentication, input validation, HTTP error handling, JSON response processing, and automated testing.

## 2. Project Objectives

The main objectives are to:

- Retrieve information about the user's public IP address.
- Perform lookups for IPv4 and IPv6 addresses.
- Retrieve geographical information associated with an IP address.
- Process IP-related information returned by the IPinfo API.
- Implement secure API authentication.
- Validate user input and handle invalid IP addresses.
- Handle HTTP errors, connection failures, and request timeouts.
- Provide a command-line interface for interacting with the application.
- Test the API and CLI behaviour.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.10+ | Core programming language |
| IPinfo API | IP geolocation and network information |
| Requests | HTTP communication |
| python-dotenv | Environment variable management |
| argparse | Command-line argument parsing |
| pytest | Automated testing |
| uv | Python project and dependency management |
| Git | Version control |
| GitHub | Team collaboration |

## 4. Project Structure

```text
epita_group6_ipops/
├── .env.example
├── .gitignore
├── README.md
├── pyproject.toml
├── requirements.txt
├── uv.lock
├── src/
│   └── epita_group6/
│       ├── __init__.py
│       ├── api.py
│       └── cli.py
└── tests/
    ├── test_api.py
    └── test_cli.py
```

### Main Components

- **api.py:** Handles IPinfo API requests, authentication, IP address validation, response processing, and API errors.
- **cli.py:** Implements the command-line interface and displays API results.
- **tests/:** Contains automated tests for API functionality and CLI behaviour.
- **pyproject.toml:** Defines project metadata, dependencies, development dependencies, and the CLI entry point.
- **uv.lock:** Records resolved dependency versions for reproducible installations.
- **.env.example:** Provides an example configuration for the API token.

## 5. Getting Started

### Prerequisites

Make sure you have:

- Python 3.10 or later.
- Git.
- [uv](https://docs.astral.sh/uv/getting-started/installation/).
- An IPinfo API token.
- An internet connection.

### 5.1 Clone the Repository

```bash
git clone https://github.com/linghurajpr/epita_group6_ipops.git
cd epita_group6_ipops
```

### 5.2 Install Dependencies

Install the project and its development dependencies:

```bash
uv sync --extra dev
```

This command creates the virtual environment if necessary and installs the project dependencies, including pytest.

### 5.3 Configure API Authentication

Create a local `.env` file from the example:

```bash
cp .env.example .env
```

Open `.env` and add your IPinfo token:

```env
IPINFO_TOKEN=your_actual_ipinfo_token
```

Replace the placeholder with your own token.

**Security note:** Never commit your real API token or `.env` file to GitHub. The `.env` file is excluded through `.gitignore`.

## 6. Running the Application

The project provides the following command:

```bash
uv run epita-group6-cli
```

### Display Help

```bash
uv run epita-group6-cli --help
```

### Retrieve Your Public IP Information

```bash
uv run epita-group6-cli
```

### Look Up a Specific IPv4 Address

```bash
uv run epita-group6-cli --ip 8.8.8.8
```

### Look Up a Specific IPv6 Address

```bash
uv run epita-group6-cli --ip 2001:4860:4860::8888
```

### Display the Response as JSON

```bash
uv run epita-group6-cli --ip 8.8.8.8 --json
```

The `--json` option displays the API response in JSON format.

## 7. API Integration

The application communicates with the IPinfo service using HTTP GET requests.

| Property | Details |
|---|---|
| API Provider | IPinfo |
| Base URL | `https://ipinfo.io` |
| Default endpoint | `/json` |
| IP lookup endpoint | `/{ip_address}/json` |
| HTTP method | GET |
| Response format | JSON |
| Authentication | Bearer token |

The authentication header is constructed as follows:

```http
Authorization: Bearer YOUR_IPINFO_TOKEN
```

The application validates a supplied IP address before sending the request.

For more information, consult the [official IPinfo documentation](https://ipinfo.io/developers).

## 8. Error Handling

The application uses a custom `IPInfoError` exception to report API-related failures.

The following situations are handled:

| Error scenario | Application behaviour |
|---|---|
| Missing API token | Reports that `IPINFO_TOKEN` is missing |
| Invalid IP address | Rejects the input before making the request |
| HTTP 401 or 403 | Reports an authentication error |
| HTTP 429 | Reports that the API rate limit has been exceeded |
| Other HTTP errors | Reports the corresponding HTTP status |
| Request timeout | Reports a timeout |
| Connection failure | Reports that the IPinfo service could not be reached |
| Invalid JSON response | Reports an invalid response |

Errors are displayed through the CLI without exposing the API token.

## 9. Testing

The project uses **pytest** for automated testing.

### Run the Test Suite

```bash
uv run pytest -v
```

The tests cover API and CLI behaviour, including:

- Successful API responses.
- IPv4 and IPv6 lookups.
- Invalid IP addresses.
- Missing API credentials.
- HTTP errors (401, 403, 429, and 500).
- Request timeouts.
- Connection failures.
- Invalid JSON responses.
- CLI output and error handling.

### Current Test Status

**17 tests passed** in the latest local test run.

```text
17 passed
```

The API tests use mocked responses for controlled and repeatable testing. A real API lookup can also be performed manually using the CLI and a valid IPinfo token.

## 10. Application Workflow

```text
             User
               |
               v
       Command-Line Interface
               |
               v
       Input Validation
               |
               v
        API Request Setup
               |
               v
        IPinfo API Request
               |
               v
          JSON Response
               |
               v
        Error Handling
               |
               v
       CLI Output Formatting
               |
               v
             User
```

1. The user starts the application through the CLI.
2. The application reads the requested IP address, if provided.
3. The API layer validates the input and retrieves the API token.
4. An authenticated HTTP request is sent to IPinfo.
5. The response is checked and processed.
6. The CLI displays the result or an appropriate error message.

## 11. Team Responsibilities

| Team Member | Responsibility |
|---|---|
| Daakshayani Neelamegam Senthilkumar | API Integration & Python Implementation |
| Jai Bansal | API Testing & Response Validation |
| Linghuraj Periyaswamy Ramani | CLI Implementation |
| Hamed Yazdannejat | Documentation & Final Testing |

All team members collaborate on integration, debugging, code review, and final validation.

## 12. Git Workflow

The project uses Git branches and pull requests to organise team development.

Recommended workflow:

1. Pull the latest changes from `main`.
2. Create a feature branch.
3. Implement and test changes locally.
4. Commit changes with a descriptive message.
5. Push the branch to GitHub.
6. Open a pull request.
7. Review and merge approved changes.
8. Test the integrated application.

Example:

```bash
git switch main
git pull origin main

git switch -c feature/my-task

git add .
git commit -m "Describe the changes"

git push -u origin feature/my-task
```

## 13. Security and Best Practices

- Keep API credentials in `.env`, not in source code.
- Never commit secrets to GitHub.
- Use `.env.example` to document required environment variables.
- Validate user input before making API requests.
- Use request timeouts to avoid indefinite waiting.
- Handle API and network errors explicitly.
- Keep dependencies and the lock file synchronised.
- Run the automated tests before submitting changes.

## 14. Project Status

The project currently provides:

- IPinfo API integration.
- IPv4 and IPv6 address lookup.
- Public IP information retrieval.
- CLI input and JSON output options.
- API authentication through an environment variable.
- API and CLI error handling.
- Automated tests.

Further improvements may be added as the project develops.

---

**EPITA — MSc Artificial Intelligence Systems**  
**Engineering Tools — TP 2**  
**Group 6**
