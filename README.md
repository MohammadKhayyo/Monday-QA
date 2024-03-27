# Selenium Testing Framework

This repository contains a Python-based Selenium testing framework designed to automate and streamline browser-based testing for web applications. The framework utilizes the Selenium WebDriver for controlling browsers and executing test scenarios across different environments and platforms.

## Project Structure

The project is organized into several key directories:

- `infra/`: Contains the core infrastructure setup for the Selenium WebDriver, including configuration management and driver initialization.
- `logic/`: Holds the business logic for page interactions, encapsulating the actions that can be performed on the web pages.
- `Test/`: Contains all test cases, organized into `parallel` and `non_parallel` directories for tests that are intended to run in parallel or serially, respectively.
- `Utils/`: Utility scripts supporting various functionalities such as string generation and user data management.

### Key Components

- **WebDriverManager (`infra/browser_wrapper.py`)**: Manages the initialization and configuration of the Selenium WebDriver instances.
- **ConfigurationManager (`infra/configurations.py`)**: Loads and handles configuration settings from JSON files.
- **Page Classes (`logic/*.py`)**: Define methods for interacting with web pages, encapsulating the Selenium commands.
- **Test Classes (`Test/non_parallel/*.py` and `Test/parallel/*.py`)**: Test suites designed to validate the functionality of web applications using the framework.

## Setup

### Prerequisites

- Python 3.8 or higher
- Selenium WebDriver
- Browser drivers (e.g., ChromeDriver for Google Chrome, geckodriver for Firefox) matching the installed browser versions

### Installation

1. Clone the repository to your local machine.
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Ensure browser drivers are installed and accessible in your system's PATH.

## Configuration

Edit the `config.json` file in the project root to specify your testing environment settings, such as browser types, WebDriver settings, and application URLs.

Example `config.json` structure:

```json
{
  "parallel": true,
  "browser_types": ["chrome", "firefox"],
  "hub": "http://localhost:4444/wd/hub",
  "url": "https://your-application-url.com"
}
```

## Running Tests

To execute the test suites:

1. Navigate to the project root directory.
2. Run the test runner script:

```bash
python ui/test_runner_api.py
```

This will initiate the test execution based on the configurations defined in `config.json`. Tests can be run in parallel or serially, depending on your setup.

## Contributing

Contributions to enhance the testing framework are welcome. Please follow the standard GitHub pull request process to propose your changes.
# POC_MONDAY
