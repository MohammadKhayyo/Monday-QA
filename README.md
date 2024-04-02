# monday.com Automation Testing Suite

## Overview

Embark on a seamless automation testing journey with our comprehensive suite designed for monday.com. Utilizing the synergy of Selenium Grid and GraphQL, this framework elevates testing for both UI and backend processes. Crafted around the Page Object Model (POM) design pattern, it promises enhanced maintainability, scalability, and clarity of test scripts. Our modular project architecture, inclusive of Infrastructure, Logic, Tests, Utils, and flexible configurations, ensures tailored test executions for precision and efficiency.

## Features

- **Selenium Grid & GraphQL Integration**: Achieve simultaneous multi-browser/platform testing and incisive API validations.
- **Page Object Model (POM)**: Streamline test script management while minimizing redundancy.
- **Dynamic Test Execution**: Customize test parameters such as browser choice, execution mode, and platform for targeted testing.
- **Cross-Browser Compatibility**: Validate functionality across major browsers for comprehensive coverage.
- **Jira & Slack Connectivity**: Automate issue logging and enjoy real-time Slack updates, fostering proactive project management.
- **CI/CD Excellence with Jenkins Pipeline**: Leverage automated testing within your CI/CD pipeline for increased efficiency and reliability.

## Project Architecture

- **Infrastructure**: Foundations for Selenium WebDriver and GraphQL configurations, driver management, and grid setups.
- **Logic**: Business logic encapsulation for simplified interactions with the monday.com platform.
- **Tests**: Comprehensive suite of API and UI tests, employing POM for enhanced interaction.
- **Utils**: Auxiliary functions and tools to support and extend testing capabilities.
- **Configuration**: Easily adjustable settings for custom test environments via a central `config.json`.

## Getting Started

### Prerequisites

- Java & Python 3.9+
- Selenium WebDriver & requests library
- pytest for running tests
- Active Selenium Grid instance

### Setup

1. **Repository Cloning**

```sh
git clone https://github.com/MohammadKhayyo/Monday-QA.git
```

2. **Install Dependencies**

```sh
pip install -r requirements.txt
```

3. **Selenium Grid Initialization**

Ensure your Grid is operational. For setup guidance, refer to Selenium's official docs.

### Configuration

Adjust `config.json` to tailor your testing environment:

- `browser`: Desired browser for testing (e.g., "chrome").
- `platform`: Target platform (e.g., "WINDOWS").
- `execution_mode`: Choose between "parallel" and "serial" execution.
- `driver`: Select "grid" for Selenium Grid or "regular" for local execution.

## Running Tests

Launch tests with ease:

```sh
pytest test_runner_pytest.py
```

## Continuous Integration

Integrate seamlessly into your development lifecycle with Jenkins, Jira, and Slack:

- **Jenkins Pipeline**: Automate test executions with our provided Jenkinsfile.
- **Jira Integration**: Automatically update issues based on test results.
- **Slack Notifications**: Keep your team informed with real-time updates on test progress and outcomes.

## Visual Insights

### Jira & Slack Integration

Stay ahead with automated Jira updates and Slack notifications for every test run, ensuring your team is always in the loop.

![image](https://github.com/MohammadKhayyo/Monday-QA/assets/89653649/ec2d57ac-417c-4159-93f8-32e1c9b50c85)
![image](https://github.com/MohammadKhayyo/Monday-QA/assets/89653649/9f8fe33a-4244-4aba-baad-1130f2564458)

### Jenkins Pipeline, Slack Integration and HTML Reports

Visualize your testing pipeline's flow and delve into detailed HTML reports for an in-depth analysis.

![image](https://github.com/MohammadKhayyo/Monday-QA/assets/89653649/d48f43cb-e06d-48b4-8c1b-9be4dfe81540)
![image](https://github.com/MohammadKhayyo/Monday-QA/assets/89653649/16e33c88-3612-40ca-8a22-a4811c9922a4)
![image](https://github.com/MohammadKhayyo/Monday-QA/assets/89653649/5e0c899f-e28e-452d-90ef-d14308b85a6c)
