pipeline{
        agent any
        stages{
            stage('Testing application'){
                steps{
                    sh "./scripts/testing.sh"
                }
            }
            stage('Build application'){
                steps{
                    sh "./scripts/build.sh"
                }
            }
            stage('Deploy application'){
                steps{
                    sh "./scripts/deploy.sh"
            
            
                }
            }

      }
}
