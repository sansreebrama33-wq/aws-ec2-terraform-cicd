from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my Cloud App! Deployed on AWS EC2 using Terraform and CI/CD.'

@app.route('/health')
def health():
    return 'App is healthy and running fine on AWS EC2.'

@app.route('/about')
def about():
    return 'This app is built with Python Flask, deployed on AWS EC2, provisioned by Terraform, and automated with GitHub Actions CI/CD.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
