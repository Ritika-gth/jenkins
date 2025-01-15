pipeline {
  agent any
  stages {
    stage ('clone git repo') {
      steps {
        git 'https://github.com/Ritika-gth/jenkins.git'
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
