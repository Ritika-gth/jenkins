pipeline {
  agent any
  stages {
   stage('Run Hello World') {
    steps {
        sh 'python3 src/HelloWorld.py'
      }
    }
    stage ('Build') {
      steps {
        echo 'Building project...'
      }
    }
    stage ('Test') {
      steps {
        echo 'Testing project...'
      }
    }
    stage ('Deploy') {
      steps {
        echo 'Deploying project...'
      }
    }
  }
}
