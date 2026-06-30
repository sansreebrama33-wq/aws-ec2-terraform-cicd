from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from AWS EC2! Deployed automatically with Terraform and CI/CD.'

@app.route('/health')
def health():
    return 'Server is healthy'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    