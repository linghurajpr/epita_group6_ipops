# EPITA Group 6 — Geolocation & IP Operations

**Course:** Engineering Tools — Session 2 (CM2 / Lab 2)  
**Program:** MSc Artificial Intelligence Systems (AIS), EPITA  
**Project:** TP 2 — API Integration and Command-Line Interface  
**Group:** 6  
**Domain:** Geolocation & IP Operations  
**API Provider:** [IPinfo](https://ipinfo.io/)

---

## 1. Project Overview

This project focuses on integrating an external REST API into a Python application and making its functionality accessible through a command-line interface (CLI).

Our team uses the **IPinfo API** to retrieve IP-related information and demonstrate how an external web service can be consumed, processed, validated, and presented through a Python-based tool.

The project covers the essential stages of API-driven application development, including HTTP requests, authentication, response handling, error management, input validation, command-line interaction, and testing.

The goal is to build a simple, reliable, and maintainable Python application that demonstrates practical API integration and CLI development.

## 2. Project Objectives

The main objectives of this project are to:

- Integrate the IPinfo REST API into a Python application.
- Understand HTTP requests, API authentication, and JSON responses.
- Implement the API integration using Python.
- Develop a command-line interface for interacting with the application.
- Validate API responses and handle potential errors.
- Test API connectivity, response processing, and CLI behaviour.
- Follow good software development practices, including modular code, secure credential management, documentation, and version control.

## 3. API Information

We use the IPinfo API for IP-related information.

| Property | Details |
|---|---|
| API Provider | IPinfo |
| Domain | Geolocation & IP Operations |
| API Endpoint | `https://ipinfo.io/json` |
| HTTP Method | `GET` |
| Response Format | JSON |
| Authentication | API token |
| Authentication Header | `Authorization: Bearer <token>` |

### Example API Request

```http
GET https://ipinfo.io/json
Authorization: Bearer YOUR_IPINFO_TOKEN
```

The API response can contain information associated with an IP address, depending on the endpoint, account permissions, and available data.

Typical fields may include:

- IP address
- Hostname
- City
- Region
- Country
- Geographic coordinates
- Organisation or network information
- Postal code
- Time zone

**Note:** The actual fields returned depend on the API response. The application should handle missing or unavailable fields gracefully.

### API Documentation

Official IPinfo documentation: https://ipinfo.io/developers

## 4. Planned Features

The following features define the intended project scope. Their implementation status should be updated as development progresses.

### 4.1 API Integration

- Send HTTP GET requests to the IPinfo API.
- Authenticate requests using an API token.
- Receive and parse JSON responses.
- Handle HTTP errors and unsuccessful requests.
- Handle connection failures and request timeouts.

### 4.2 Python Implementation

- Implement API communication in Python.
- Separate API-related logic from the CLI where appropriate.
- Validate API responses before processing them.
- Handle unexpected or missing response fields.
- Keep the code readable, reusable, and maintainable.

### 4.3 Command-Line Interface

The CLI will provide a convenient way to interact with the application from a terminal.

The intended functionality includes:

- Launching the application from the command line.
- Requesting IP-related information from the API.
- Displaying the retrieved information in a readable format.
- Communicating API failures and invalid responses through understandable error messages.
- Providing appropriate feedback when a request cannot be completed.

**Implementation note:** Exact CLI commands and options will be documented once the interface has been finalised.

### 4.4 Testing and Validation

- Verify that API requests are constructed correctly.
- Check response status codes and JSON parsing.
- Validate expected response fields.
- Test unsuccessful HTTP responses.
- Test connection and timeout failures.
- Verify CLI behaviour for successful and unsuccessful requests.

## 5. Application Workflow

The intended application workflow is:

```text
        User
         |
         v
  Command-Line Interface
         |
         v
  Python Application Logic
         |
         v
  API Request & Authentication
         |
         v
       IPinfo API
         |
         v
     JSON Response
         |
         v
  Response Validation
         |
         v
  Formatted CLI Output
         |
         v
        User
```

### Workflow Explanation

1. The user starts the application through the command-line interface.
2. The CLI passes the requested operation to the Python application.
3. The application prepares an authenticated HTTP GET request.
4. The request is sent to the IPinfo API.
5. The API returns a response containing IP-related information or an error.
6. The application checks the response and processes the returned data.
7. The CLI displays the results or an appropriate error message.

## 6. Team Responsibilities

The project is divided among four members, with each member responsible for a specific area of development.

| Team Member | Primary Responsibility | Key Tasks |
|---|---|---|
| **Daakshayani Neelamegam Senthilkumar** | API Integration & Python Implementation | Implement API communication, authentication, HTTP requests, JSON parsing, and core Python functionality. |
| **Jai Bansal** | API Testing & Response Validation | Test API requests, validate response structures, verify status codes, and check error-handling behaviour. |
| **Linghuraj Periyaswamy Ramani** | CLI Implementation | Develop the command-line interface, handle user interaction, connect CLI commands to application logic, and present results clearly. |
| **Hamed Yazdannejat** | Documentation & Final Testing | Maintain project documentation, review setup instructions, coordinate final testing, and verify the application workflow. |

### Collaboration

Although each member has a primary responsibility, all team members will collaborate on integration, debugging, code review, and final validation.

The final application will be tested as a complete system rather than as four independent components.

## 7. Technology Stack

The project uses the following technologies and tools.

| Technology | Purpose |
|---|---|
| Python | Core application implementation |
| REST API | Communication with the IPinfo service |
| HTTP | Sending requests and receiving responses |
| JSON | Processing API responses |
| Command-Line Interface | User interaction |
| Git | Version control |
| GitHub | Repository hosting and collaboration |
| Python Testing Framework | Automated testing, once configured |

Additional Python packages and development tools will be documented according to the final implementation.

## 8. Getting Started

### Prerequisites

Before running the application, ensure that you have:

- Python 3 installed.
- Git installed.
- Access to the project repository.
- An IPinfo API token, if required by the account and endpoint configuration.
- An internet connection to communicate with the API.

### 8.1 Clone the Repository

```bash
git clone <REPOSITORY_URL>
cd <REPOSITORY_DIRECTORY>
```

Replace the placeholders with the actual repository URL and directory name.

### 8.2 Create a Virtual Environment

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 8.3 Install Dependencies

If the repository contains a `requirements.txt` file:

```bash
python -m pip install -r requirements.txt
```

If the project uses `pyproject.toml` or another dependency-management configuration, follow the instructions defined in that file.

### 8.4 Configure API Credentials

Store the IPinfo API token in a local environment variable rather than directly in the source code.

On macOS or Linux:

```bash
export IPINFO_TOKEN="your_ipinfo_token"
```

On Windows PowerShell:

```powershell
$env:IPINFO_TOKEN="your_ipinfo_token"
```

Replace `your_ipinfo_token` with your own token.

The application should retrieve the token from the environment and use it to construct the authentication header.

Example Python pattern:

```python
import os

token = os.getenv("IPINFO_TOKEN")

if not token:
    raise RuntimeError(
        "IPINFO_TOKEN is not configured."
    )

headers = {
    "Authorization": f"Bearer {token}"
}
```

This snippet illustrates credential handling; it is not a complete API client.

**Security requirement:** Never commit real API tokens, passwords, or other secrets to GitHub.

Add local environment files to `.gitignore` where applicable.

Example:

```gitignore
.venv/
__pycache__/
*.py[cod]
.env
.pytest_cache/
```

## 9. Running the Application

The exact entry point and CLI syntax depend on the implementation.

Once the entry point has been finalised, document the command here.

For example, if the application is implemented as a Python module:

```bash
python -m <module_name>
```

If the project defines a console script in `pyproject.toml`, use the installed command instead.

**TODO:** Replace the example above with the actual command supported by the repository.

## 10. Testing

Testing is an important part of this project because API requests can fail for several reasons, including network problems, invalid credentials, unexpected response data, and service-side errors.

### 10.1 API Integration Tests

The API integration should be checked for:

- Correct endpoint and HTTP method.
- Correct authentication header.
- Successful HTTP responses.
- Valid JSON response parsing.
- Missing or unexpected response fields.
- Invalid or expired credentials.
- HTTP error responses.
- Network failures and request timeouts.

### 10.2 Response Validation

The response-validation tests should verify that:

- The response is processed only when appropriate.
- Expected fields are handled correctly.
- Missing fields do not cause unexpected crashes.
- Invalid response data produces understandable errors.
- The application does not assume every API response contains the same information.

### 10.3 CLI Tests

The CLI should be tested for:

- Correct command execution.
- Appropriate display of returned information.
- Clear error messages when requests fail.
- Appropriate behaviour when required configuration is missing.
- Correct interaction with the Python API layer.

### 10.4 Final End-to-End Testing

Before submission, the team should verify the complete workflow:

1. Configure the required environment variables.
2. Start the application using the documented command.
3. Send a request to the IPinfo API.
4. Verify that the response is processed correctly.
5. Confirm that the CLI displays the result clearly.
6. Test at least one failure scenario.
7. Verify that the application does not expose API credentials.

Automated test commands will be added here once the testing framework and project configuration are finalised.

## 11. Error Handling

The application should handle errors in a controlled and understandable way.

| Error Scenario | Expected Behaviour |
|---|---|
| Missing API token | Explain how to configure the required token. |
| Invalid credentials | Report an authentication failure without exposing secrets. |
| HTTP error response | Report the failure and handle the response appropriately. |
| Connection failure | Inform the user that the API could not be reached. |
| Request timeout | Report the timeout and avoid hanging indefinitely. |
| Invalid JSON | Handle response-parsing failures safely. |
| Missing response fields | Display available information without assuming every field exists. |

Error handling should distinguish between API failures, configuration problems, and unexpected application errors wherever practical.

## 12. Repository Structure

The final directory structure will depend on the implementation. A possible organisation is:

```text
epita_group6_geolocation/
│
├── README.md
├── pyproject.toml
├── requirements.txt
├── .gitignore
│
├── src/
│   └── <python_package>/
│       ├── __init__.py
│       ├── api.py
│       ├── cli.py
│       └── main.py
│
└── tests/
    ├── test_api.py
    ├── test_response_validation.py
    └── test_cli.py
```

This is a proposed structure, not a description of files already present in the repository.

The team should update this section to reflect the actual directory structure and remove unused files or dependency-management options.

## 13. Git Workflow & Collaboration

To keep development organised, each team member should work on a separate feature branch when implementing a distinct component.

### Recommended Workflow

1. Pull the latest changes from the shared repository.
2. Create a feature branch for the assigned task.
3. Implement and test the changes locally.
4. Commit the changes with a descriptive message.
5. Push the branch to GitHub.
6. Open a pull request for review.
7. Resolve conflicts and incorporate feedback.
8. Merge the changes after review and validation.
9. Test the integrated application.

### Example Commands

Create a feature branch:

```bash
git checkout -b feature/api-integration
```

Stage and commit changes:

```bash
git add .
git commit -m "Implement IPinfo API integration"
```

Push the branch:

```bash
git push -u origin feature/api-integration
```

Use appropriate branch names and commit messages for each task.

### Suggested Branch Names

| Task | Example Branch |
|---|---|
| API integration | `feature/api-integration` |
| API testing | `feature/api-testing` |
| CLI implementation | `feature/cli` |
| Documentation |