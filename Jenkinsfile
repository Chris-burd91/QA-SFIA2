pipeline{
        agent any
        stages{
            /*stage('Set up with ansible'){
                steps{
                    sh "./scripts/set-up.sh"
                }
            }*/
            /*stage('Testing application'){
                steps{
                    sh "./scripts/testing.sh"
                }
            }*/
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
