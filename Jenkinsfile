pipeline {
    agent any

    stages {
        stage('Verifying Tooling') {
            steps {
                sh ''' 
                    docker version
                    docker info
                    docker-compose version
                    curl --version
                    jq --version
                
                '''
                
            }
        }
      
    }

}