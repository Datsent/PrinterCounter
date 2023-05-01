properties([githubProjectProperty(displayName: '', projectUrlStr: 'https://github.com/Datsent/PrinterCounter.git/'), pipelineTriggers([githubPush()])])
pipeline{
    agent {
        node 'UNI-COMP-108'
    }
    environment {
        SOURCE_PATH = 'C:\\PrinterCounter'
    }
    stages{
        stage('Checkout git repository'){
            steps{
                git 'https://github.com/Datsent/PrinterCounter.git'
                echo 'Clone Git Project Done'
            }
        }
        stage('Check files'){
            steps{
                bat 'dir'   
            }
        }
        stage('Create backup old Ver'){
            steps{
               bat 'xcopy c:\\PrinterCounter\\ c:\\PrinterCounter_temp\\ /E /Y' 
            }
        }
        stage('Prepair for test'){
            steps{
                bat "mkdir Archive"
                bat 'xcopy c:\\PrinterCounter\\Printers.csv * /Y'
            }
        }
        stage('Test'){
            steps{
                catchError(message: 'The Build is FAILED. No Push', stageResult: 'FAILURE') {
                    script {
                        try{
                            bat 'pip install selenium'
                            bat 'python test.py'
                            echo "Test PASSED"
                        }
                        catch (e) {
                            echo "Test FAILED"
                            currentBuild.result = "FAILURE"
                            currentStage.result = "FAILURE"
                        } 
                    }
                }
            }
        }
        stage('Deploy'){
            steps{
              catchError(message: 'The Build is FAILED. Return to Previus Ver', stageResult: 'FAILURE') {
                script {
                    if (currentBuild.result == "FAILURE"){
                        echo "The Test stage is fail. Backuping"
                        bat 'xcopy c:\\PrinterCounter_temp\\ c:\\PrinterCounter\\ /E /Y'
                        bat 'rmdir Archive\\ /s /q'
                        currentStage.result = "FAILURE"
                    }
                    else{
                        bat 'xcopy Models\\ c:\\PrinterCounter\\Models\\ /E /Y'
                        bat 'xcopy Counter.py c:\\PrinterCounter\\  /Y'
                        bat 'xcopy DataFile.py c:\\PrinterCounter\\ /Y'
                        bat 'xcopy PrinterCounter.py c:\\PrinterCounter\\ /Y'
                        bat 'xcopy c:\\PrinterCounter_temp\\Printers.csv c:\\PrinterCounter\\ /Y'
                        bat 'rmdir c:\\PrinterCounter\\Archive /s /q'
                        bat 'xcopy c:\\PrinterCounter_temp\\Archive c:\\PrinterCounter\\Archive\\ /E /Y'
                        bat 'rmdir c:\\PrinterCounter_temp\\ /s /q'
                        bat 'rmdir Archive\\ /s /q'
                    }
                }
              }
            }    
        }
    }
}
