pipeline {
    agent any

    environment {
        PIP_PATH = 'C:\\Users\\Moham\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\pip.exe'
        PYTHON_PATH = 'C:\\Users\\Moham\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
    }

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                bat "${PIP_PATH} install -r requirements.txt"
            }
        }

//         stage('Parallel Steps') {
//             parallel {
//                 stage('Running API Tests') {
//                     steps {
//                         echo 'Testing...'
//                         bat "${PYTHON_PATH} -m unittest Tests/test_api/test_runner.py"
//                     }
//                 }

                stage('Setup Selenium Server HUB') {
                    steps {
                        echo 'Setting up Selenium server HUB...'
                        bat "start /b java -jar selenium-server-4.17.0.jar hub"
                        // Delay for 10 seconds
                        bat 'ping 127.0.0.1 -n 11 > nul' // Windows command to sleep for 10 seconds
                    }
                }

                stage('Setup Selenium Server nodes') {
                    steps {
                        echo 'Setting up Selenium server nodes...'
                        bat "start /b java -jar selenium-server-4.17.0.jar node --port 5555 --selenium-manager true"
                        // Delay for 10 seconds
                        bat 'ping 127.0.0.1 -n 11 > nul' // Windows command to sleep for 10 seconds
                    }
                }
            }
        }

        stage('Running UI API Tests') {
            steps {
                echo 'Testing...'
                bat "${PYTHON_PATH} -m unittest test_runner_ui_api.py"
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // bat "rd /s /q venv"
        }
    }
}
