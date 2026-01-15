# Event Announcement App

## Overview
The Event Announcement App is a serverless, event-driven web application designed to publish event announcements and notify subscribers via email. The application follows a clean separation of concerns by using managed AWS services, eliminating the need for backend servers and manual scaling.

A static frontend hosted on Amazon S3 sends event data to a REST API exposed through Amazon API Gateway. The API triggers an AWS Lambda function that processes the request and publishes notifications to Amazon SNS.

## Architecture
  ![core serverless architecture di](<architecture/core flow architecture.png>)

## Tech Stack
### AWS Services

 - Amazon S3 – Static website hosting
 - Amazon API Gateway – REST API
 - AWS Lambda – Serverless compute
 - Amazon SNS – Email notifications
 - AWS IAM – Access control (least privilege)
 - AWS CloudFormation – Infrastructure as Code
 - Tools & Languages
 - Python (Lambda logic)
 - HTML, CSS, JavaScript (Frontend)

### AWS CLI
 - boto3 (AWS SDK for Python)

## How It Works
#### Frontend flow
 - Collects event details from the user
 - Sends HTTP requests to the API Gateway endpoint
 - Contains no AWS credentials or business logic  

#### Backend flow
 - API Gateway receives requests and forwards them to Lambda
 -Lambda validates input, formats the message, and triggers SNS

#### Notifications
 - Amazon SNS broadcasts event announcements to subscribed email addresses
 - The application remains unaware of subscribers, ensuring decoupling

## Infrastructure as Code
All AWS resources are defined using AWS CloudFormation templates.

Benefits:
 - Reproducible deployments
 - Version-controlled infrastructure
 - Clear audit trail of changes
 - No manual console dependency
 - CloudFormation acts as the single source of truth for the system.

## Security
 - IAM roles follow least-privilege principles
 - Lambda can only publish to the specific SNS topic it needs
 - No AWS credentials are exposed to the frontend
 - API Gateway acts as the controlled public entry point

## Deployment
- Prerequisites
- High-level deploy steps (no commands yet)

## Design Decisions & Trade-offs
- Why serverless
- Optional components explained

## What I Learned
- Cloud concepts
- Engineering mindset

## Future Improvements
- Auth
- Persistence
- Observability
