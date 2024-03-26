pipeline {
    agent any
    environment {
        // Environment variables setup
        API_MONDAY = credentials('token_monday')
        JIRA_TOKEN = credentials('token_jira')
    }
    stages {
        // Previous stages remain unchanged

        stage('Publish Report') {
            steps {
                // Check if the reports directory exists and is not empty
                script {
                    if (bat(script: 'if exist reports\\* (exit 0) else (exit 1)', returnStatus: true) == 0) {
                        echo 'Reports directory exists and is not empty. Proceeding with compression...'
                        bat 'powershell Compress-Archive -Path reports\\* -DestinationPath report.zip -Force'
                    } else {
                        error 'Reports directory is empty or does not exist. Skipping compression...'
                    }
                }
                // Only attempt to archive report.zip if the above check passes
                archiveArtifacts artifacts: 'report.zip', onlyIfSuccessful: true
            }
        }

        // Subsequent stages and post steps remain unchanged
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
