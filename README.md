# Student Record and Academic Management Platform

DevOps Mini Project 4 — AWS, Terraform, Ansible and Docker

## Overview
A Flask-based Student Record and Academic Management Platform deployed on AWS EC2 using Docker.

## Technology Stack
- AWS EC2 and Ubuntu 24.04 LTS
- Terraform: Infrastructure as Code
- Ansible: Configuration management
- Docker: Application containerization
- Python and Flask: REST API
- Git and GitHub: Version control

## API Endpoints
- GET /api/health: Application health check
- GET /api/students: Retrieve student records
- POST /api/marks: Update student marks

## Project Structure
- app/: Flask application and Dockerfile
- terraform/: Terraform configuration
- ansible/: Ansible playbook
- screenshots/: Project evidence

## Run the Application
Build: sudo docker build -t student-platform:latest ./app
Run: sudo docker run -d --name student-platform -p 80:8080 student-platform:latest
Test: curl http://localhost/api/health

## Infrastructure Automation
T erraform validation succeeded. AWS authentication and full Terraform-managed provisioning remain unverified.

## Security
- Never commit AWS credentials, private keys or Terraform state files.
- Restrict SSH access to trusted IP addresses.

## Author
Omkar Ghorpade
