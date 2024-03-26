pipeline {
    agent any
    environment {
        // Environment variables setup
        API_MONDAY = credentials('token_monday')
        JIRA_TOKEN = credentials('token_jira')
    }
    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                bat 'C:\\Users\\Moham\\AppData\\Local\\Programs\\Python\\Python311\\python.exe -m venv venv'
                bat 'venv\\Scripts\\pip.exe install -r requirements.txt'
            }
            post {
                success {
                    slackSend (color: 'good', message: "SUCCESS: Setup Environment stage completed successfully.")
                }
                failure {
                    slackSend (color: 'danger', message: "FAILURE: Setup Environment stage failed.")
                }
            }
        }
        stage('Setup Selenium Server HUB') {
            steps {
                echo 'Setting up Selenium server HUB...'
                bat "start /b java -jar selenium-server-4.17.0.jar hub"
                bat 'ping 127.0.0.1 -n 11 > nul'
            }
            post {
                success {
                    slackSend (color: 'good', message: "SUCCESS: Setup Selenium Server HUB stage completed successfully.")
                }
                failure {
                    slackSend (color: 'danger', message: "FAILURE: Setup Selenium Server HUB stage failed.")
                }
            }
        }
        stage('Setup Selenium Server nodes') {
            steps {
                echo 'Setting up Selenium server nodes...'
                bat "start /b java -jar selenium-server-4.17.0.jar node --port 5555 --selenium-manager true"
                bat 'ping 127.0.0.1 -n 11 > nul'
            }
            post {
                success {
                    slackSend (color: 'good', message: "SUCCESS: Setup Selenium Server nodes stage completed successfully.")
                }
                failure {
                    slackSend (color: 'danger', message: "FAILURE: Setup Selenium Server nodes stage failed.")
                }
            }
        }
        stage('Running Tests') {
            steps {
                echo 'Testing..'
                bat "venv\\Scripts\\python.exe test_runner_ui_api.py"
            }
            post {
                success {
                    slackSend (color: 'good', message: "SUCCESS: Running Tests stage completed successfully.")
                }
                failure {
                    slackSend (color: 'danger', message: "FAILURE: Running Tests stage failed.")
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Deployment steps go here
            }
            post {
                success {
                    slackSend (color: 'good', message: "SUCCESS: Deploy stage completed successfully.")
                }
                failure {
                    slackSend (color: 'danger', message: "FAILURE: Deploy stage failed.")
                }
            }
        }
        stage('Publish Report') {
            steps {
                script {
                    bat 'echo Current Working Directory: %CD%'
                    bat 'dir reports\\*'
                    if (bat(script: 'if exist reports\\* (exit 0) else (exit 1)', returnStatus: true) == 0) {
                        echo 'Reports directory exists and is not empty. Proceeding with compression using 7-Zip...'

                        // Specify the path to the 7-Zip executable
                        def pathTo7Zip = '"C:\\Program Files\\7-Zip\\7z.exe"'
                        // Compress the reports directory into report.zip using 7-Zip
                        def compressCmd = "${pathTo7Zip} a -tzip report.zip reports\\* -mx=9"
                        def compressOutput = bat(script: compressCmd, returnStdout: true).trim()
                        echo "Compression Output: ${compressOutput}"

                        // Verify report.zip was created
                        if (bat(script: 'if exist report.zip (exit 0) else (exit 1)', returnStatus: true) == 0) {
                            echo 'report.zip exists. Proceeding to archive...'
                            archiveArtifacts artifacts: 'report.zip', onlyIfSuccessful: true
                        } else {
                            error 'report.zip does not exist after compression attempt with 7-Zip.'
                        }
                    } else {
                        error 'Reports directory is empty or does not exist. Skipping compression...'
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            slackSend (color: 'warning', message: "NOTIFICATION: Cleaning up resources...")
        }
        success {
            echo 'Build succeeded.'
            slackSend (color: 'good', message: "SUCCESS: Build completed successfully.")
        }
        failure {
            echo 'Build failed.'
            slackSend (color: 'danger', message: "FAILURE: Build failed.")
        }
    }
}
