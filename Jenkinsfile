properties([githubProjectProperty(displayName: '', projectUrlStr: 'https://github.com/Datsent/PrinterCounter.git')])

pipeline{
    agent {
        node'uni_pc'
    }
    environment {
        SOURCE_PATH = 'C:\\Users\\dima\\Desktop\\PrinterCounter'
    }
    stages{
        stage('Checkout git repository'){
            steps{
                git 'https://github.com/Datsent/PrinterCounter.git/'
                echo 'Clone Git Project Done'
            }
        }
        stage('Copy source file'){
            steps{
               bat "COPY ${SOURCE_PATH}\\Printers.csv Printers.csv"
               bat "mkdir Archive"
               echo "${SOURCE_PATH} coped"
            }
        }
        stage('Run App'){
            steps{
                bat 'python PrinterCounter.py'
                echo 'Running finished'
            }
        }
        stage('Delete source file'){
            steps{
                bat "del Printers.csv"
                bat "rmdir /s /q Archive"
                echo 'Deleted'
            }
        }
        stage('Deploy App'){
            steps{
                bat "xcopy * ${SOURCE_PATH} /E /Y"
            }
        }
    }
    post { 
        always { 
            cleanWs()
        }
    }
}
