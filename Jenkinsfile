pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Получение исходного кода из репозитория
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Установка зависимостей (если необходимо)
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                // Запуск BDD-тестов
                sh 'behave /путь/к/файлу/google.feature'
            }
        }
    }
    
    post {
        always {
            // Очистка ресурсов, завершение сеансов и т.д.
            sh 'pkill -9 chromedriver'
            sh 'pkill -9 chrome'
        }
    }
}
