pipeline{
        agent any
        stages{
            stage('Clone repository'){
                steps{
                    sh "./scripts/get-repo.sh"
                }
            }
            stage('Install docker & docker compose'){
                steps{
                    sh "./scripts/docker-installs.sh"
                    sh "sudo usermod -aG docker jenkins"
                    sh "newgrp docker"
                }
            }
            stage('Deploy application'){
                steps{
                    sh "./scripts/deploy.sh"
                }
            }

      }
}
