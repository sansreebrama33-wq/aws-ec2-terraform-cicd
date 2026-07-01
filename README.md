## Automated Python App Deployment on AWS EC2 with Terraform & CI/CD
A hands-on cloud project where every code push automatically goes live on AWS — no manual steps, no SSH required. Built with Flask, provisioned with Terraform, and deployed through a GitHub Actions pipeline.

## Tools&Technologies 
- Python (Flask) — Web application
- AWS EC2 — Cloud server to host the app
- Terraform — Infrastructure as Code to provision AWS resources
- Linux (Amazon Linux) — Server OS with systemd service management
- GitHub Actions — CI/CD pipeline for automated deployment

## Architecrure
Developer pushes code
        ↓
    GitHub Repo
        ↓
  GitHub Actions (CI/CD Pipeline)
        ↓
  Copies app.py to EC2 
        ↓
  Restarts Flask service 
        ↓
  Live app updated on AWS EC2

## Infrastructure (Terraform)
- EC2 t3.micro (Amazon Linux) — runs the Flask app
- Security Group — opens port 22 (SSH) and port 5000 (Flask)

## Project Structure




