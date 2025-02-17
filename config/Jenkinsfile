pipeline {
    agent any
    environment {
        GIT_CREDENTIALS_ID = 'github-credentials'
        BRANCH = 'requirements'
        DIR_TO_PUSH = '/var/jenkins_home/workspace/Automation_Suite'
    }
    stages {
        stage('Stage-1: Clear old files'){
            steps {
                deleteDir()
            }
        }
        stage('Stage-2: Clone repository') {
            steps {
                bat '''
                        rmdir /s /q repo
                        git clone https://github.com/sagar-harry/Automation_Suite destination_repo
                        cd destination_repo
                        git checkout main
                    '''
            }
        }
        
       stage("Stage-3: Run test scripts") {
            steps {
                script {
                    def venv_path = "C:/Users/Administrator/Desktop/QE_COE/genai_venv/Scripts"
                    def workspace_path = "C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2"

                    bat """
                        cd ${venv_path}
                        call activate
                        cd ${workspace_path}
                        python test_scenarios.py
                    """
                    echo "Completed Stage-3"
                }
            }
        }

        
    }
}
