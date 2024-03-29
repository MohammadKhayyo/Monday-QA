# UI & API Testing Suite for monday.com

This repository hosts a comprehensive testing suite designed to automate UI and API tests for the monday.com platform. Integrating Selenium Grid for UI testing and utilizing GraphQL queries for API validations, this suite ensures a thorough examination of both front-end and back-end components. Our CI/CD pipeline, constructed with Jenkins, Docker, and GitHub Actions, significantly enhances automation, testing efficiency, and overall software quality.

## Key Features

- **Seamless Integration**: Effortlessly combines UI and API tests, offering a holistic approach to quality assurance for the monday.com platform.
- **Advanced Testing Techniques**: Leverages Selenium Grid for distributed UI testing and GraphQL for efficient API testing, covering a wide range of scenarios and use cases.
- **CI/CD Pipeline**: Employs Jenkins, Docker, and GitHub Actions to automate the testing lifecycle, from code pushes to deployment, facilitating continuous integration and delivery.
- **Enhanced Efficiency**: Boosts automation, streamlines testing workflows, and significantly reduces manual testing efforts.
- **Quality Assurance**: Elevates the standard of software quality through comprehensive testing strategies.

## Getting Started

### Prerequisites

- Docker
- Jenkins with Pipeline, Docker, and GitHub plugins installed
- Node.js and npm (for managing project dependencies)
- Access to a monday.com account for API credentials

### Installation and Setup

1. **Clone the Repository**

```sh
git clone https://github.com/MohammadKhayyo/Monday-final-project.git
cd monday-testing-suite
```

2. **Configure Environment Variables**

Create a `.env` file at the root of your project directory, specifying your monday.com API credentials, among other necessary configurations:

```
MONDAY_API_KEY=your_monday_api_key
JENKINS_URL=your_jenkins_url
DOCKER_HUB_USERNAME=your_docker_hub_username
```

3. **Running Docker Containers**

Ensure Docker is running on your machine. Build and run the containers necessary for Selenium Grid and the application under test:

```sh
docker-compose up -d
```

4. **Setting Up Jenkins Pipeline**

In Jenkins, create a new pipeline job, pointing it to your repository's `Jenkinsfile`. Configure the necessary credentials and environment variables in Jenkins to match those in your `.env` file.

### Executing Tests

Trigger the pipeline through a push to your repository or manually via Jenkins. The pipeline will automatically:

- Set up the testing environment.
- Execute UI and API tests against the monday.com platform.
- Provide feedback and generate reports on test outcomes.

## Contributing

We welcome contributions that enhance the testing suite's capabilities or extend its coverage. Please fork the repository, create a feature branch, and submit a pull request with your changes. For detailed guidelines, refer to `CONTRIBUTING.md`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
