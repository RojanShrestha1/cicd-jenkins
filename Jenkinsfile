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
        stage("PRUNE DOCKER DATA"){

            steps {

                sh '''
                    docker system prune -a --volumes -f
                '''
            }
        }

        stage('Start Services') {
            steps {
                sh '''docker-compose up -d --no-color --wait'''
                sh '''docker-compose ps'''
            }
        }
      
    }

}