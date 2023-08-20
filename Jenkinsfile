pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/master']],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'my-repo']],
                    submoduleCfg: [],
                    userRemoteConfigs: [[
                        credentialsId: ' ', // ssh key
                        url: 'https://github.com/TsykalanovDima/Jen' // ssh url
                    ]]
                ])
            }
        }
    }
}
