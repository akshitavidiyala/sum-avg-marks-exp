pipeline {
    agent any

    stages {
        stage('Run Python Script') {
            steps {
                sh 'python3 sum_avg_marks.py'
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'artifacts.txt', fingerprint: true
            }
        }
    }
}

