pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }
        
        stage('Setup Environment') {
            steps {
                sh 'pip install -r requirements.txt' // Установка зависимостей Python из requirements.txt
                sh 'pip install selenium' // Установка библиотеки Selenium
                sh 'brew install --cask chromedriver' // Установка chromedriver на MacOS (предполагается, что Homebrew установлен)
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'behave features'
            }
        }
    }
    
    post {
        always {
            sh 'pkill -f chromedriver' // Завершение chromedriver
        }
    }
}
