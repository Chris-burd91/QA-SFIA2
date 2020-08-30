pipeline{
        agent any
        stages{
            stage('Clone repository'){
                steps{
                    sh "./scripts/get-repo.sh"
                }
            }
            stage('Deploy application'){
                steps{
                    sh "./scripts/deploy.sh"
                }
            }
            stage('Testing application'){
                steps{
                    sh "./scripts/tests"
            
                }
            }

      }
}
