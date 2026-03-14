# 📚 Scooter Service: API Automation Framework

![CI/CD Status](https://github.com/AlyaSmirnova/Sprint_7/actions/workflows/api-tests.yml/badge.svg?branch=main)
[![Python Version](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org)
[![Requests](https://img.shields.io/badge/HTTP-Requests-blue?logo=python\&logoColor=white)](https://requests.readthedocs.io)
[![Reports](https://img.shields.io/badge/Reports-Allure-orange?logo=allure)](https://github.com/AlyaSmirnova/Sprint_7)

## ✅ Table of Contents
1. [Description](#-description)
2. [Tech Stack & Tools](#-tech-stack-&-tools)
3. [Project Architecture](#-project-architecture)
4. [Allure Reporting Features](#-allure-reporting-features)
5. [Test Coverage](#-test-coverage)
6. [Execution Guide](#-execution-guide)
7. [CI/CD Workflow](#-cicd-workflow)

## 💫 Description
This project contains automated API tests for the **Yandex Scooter** service. The framework validates the core backend functionality including courier management and order processing.
Official API Documentation: [Yandex Scooter API](https://qa-scooter.praktikum-services.ru/docs/).

## 🧑‍💻Tech Stack & Tools
- **Language:** Python 3.13+
- **Framework:** [Pytest](https://docs.pytest.org/)
- **HTTP Client:** [Requests](https://requests.readthedocs.io)
- **Reporting:** Allure Framework
- **CI/CD:** GitHub Actions

## 📁 Project Architecture
```text
    ├── .github/workflows/     # CI/CD pipeline configuration 
    ├── allure-results/        # Raw test execution data (generated after run)
    ├── srs/                   # Support modules
    │   ├── config.py          # API Endpoints and Base URL
    │   ├── data.py            # Test data and Response messages
    │   ├── helpers.py         # Data generators (random strings, etc.)
    │ 
    ├── tests/                 # Test scenarios
    │   ├── test_create_courier.py
    │   ├── test_create_order.py
    │   ├── test_get_orders_list.py
    │   ├── test_login_courier.py
    │   
    ├── conftest.py              # Pytest fixtures
    ├── pytest.ini               # Configuration file (Allure flags)
    ├── requirements.txt         # Project dependencies
    └── .gitignore               # Files to exclude from Git
```

## 📊 Allure Reporting Features
The project is integrated with the **Allure Framework** to provide deep visibility into the API automation process. Key features include:

*   **Request & Response Transparency:** Detailed logging of HTTP requests (Body, Headers) and Server responses, enabling rapid debugging directly from the report.
*   **Hierarchical Grouping:** Tests are logically organized by **Features** (e.g., Courier Management) and **Stories** (e.g., Courier Authorization) for structured analysis.
*   **Dynamic Documentation:** Detailed `@allure.title` and `@allure.description` transform technical code into readable business scenarios for stakeholders.
*   **Step-by-Step Execution:** Comprehensive `@allure.step` logging tracks every action, from generating random test data to validating final JSON response structures.
*   **Parametrization Support:** Clear visualization of multiple test variations (e.g., different scooter colors) within a single test suite.

## 🧪 Test Coverage
The automation suite provides comprehensive coverage for the following functional modules of the **Yandex Scooter** API:

### 1. Courier Management
* **Registration Flow:** 
    * Successful courier creation with valid data.
    * Verification of error handling when creating a duplicate courier (409 Conflict).
    * Validation of mandatory fields: ensuring an account cannot be created if required data is missing (400 Bad Request).
* **Authorization (Login):** 
    * Successful login and retrieval of the courier ID.
    * Error handling for incorrect login/password combinations (404 Not Found).
    * Validation of missing mandatory fields in the login request.
    * Verification of system behavior when attempting to log in as a non-existent user.

### 2. Order Management
* **Order Creation:** 
    * Functional testing of the order placement process with various color combinations (Black, Grey, both, or none).
    * Verification of successful response status codes (201 Created).
    * Validation of the order `track` number presence and data type in the response.
* **Order Retrieval:** 
    * Verification of the global order list retrieval (200 OK).
    * Data structure validation to ensure the response contains a non-empty list of orders.

### 3. Technical Implementation Details
* **Data Parameterization:** Using `@pytest.mark.parametrize` to execute multiple test variations efficiently.
* **Response Validation:** Strict verification of HTTP status codes, JSON keys, and specific error messages.
* **Clean Code Practices:** Centralized configuration for endpoints and reusable test data to ensure maintainability.

## ⚙️ Execution Guide
### 1. Environment Setup
Clone the repository and set up a local virtual environment to ensure dependency isolation:

1. **Clone repository**
> ```bash 
> git clone https://github.com/AlyaSmirnova/Sprint_7
> cd Sprint_7
📦 Repository: [Sprint_5](https://github.com/AlyaSmirnova/Sprint_7)

2. **Create a virtual environment**
> ```bash 
> python -m venv venv

3. **Activate the virtual environment**
> ```bash 
> source venv/bin/activate

4. **Install required dependencies**
> `$ pip install -r requirements.txt`

### 2. Running Tests
The framework is pre-configured via `pytest.ini`. You can execute the full test suite and collect Allure results with a single command:
> ```bash 
> pytest
*Note: This will automatically clear previous results and generate new data in the `allure-results` folder.*

### 3. Generatig Allure Report
To transform the raw execution data into a visual, interactive HTML report, use the following command:
> ```bash 
> allure serve allure-results
*This will launch a local web server and open the report in your default browser.*

## ⚙️ CI/CD Workflow
The project is fully automated using **GitHub Actions**. Upon every `push` to the **main** branch or any `Pull Request` creation:

1.  **Environment Provisioning:** A clean **Ubuntu** runner is initialized in the cloud environment.
2.  **Dependency Management:** The Python **3.13** environment is set up, and all required libraries (`Requests`, `Pytest`, `Allure`) are installed from `requirements.txt`.
3.  **Automated Execution:** The full API test suite is executed against the **Stellar Burgers** (or Scooter) production/staging environment.
4.  **Artifact Generation:** Test results are collected, and the **Allure report** is prepared for analysis, ensuring that any API regression is caught immediately.
5.  **Status Reporting:** Real-time feedback on build success or failure is provided via GitHub status badges.