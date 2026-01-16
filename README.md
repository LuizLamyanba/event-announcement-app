# Event Announcement App

## Overview
The Event Announcement App is a serverless, event-driven web application designed to publish event announcements and notify subscribers via email. The application follows a clean separation of concerns by using managed AWS services, eliminating the need for backend servers and manual scaling.

A static frontend hosted on Amazon S3 sends event data to a REST API exposed through Amazon API Gateway. The API triggers an AWS Lambda function that processes the request and publishes notifications to Amazon SNS.

## Architecture
  ![core serverless architecture di](<architecture/core flow architecture.png>)
  [architecture readme!](architecture/architecture.md) (brief description about the architecture core flow of the project)

#### Core Flow
1. A client sends an event payload to the API
2. API Gateway forwards the request to Lambda
3. Lambda validates and processes the request
4. SNS publishes a notification to subscribed emails
  

## Tech Stack
### AWS Services

 - Amazon S3 – Static website hosting
 - Amazon API Gateway – REST API
 - AWS Lambda – Serverless compute
 - Amazon SNS – Email notifications
 - AWS IAM – Access control (least privilege)
 - AWS CloudFormation – Infrastructure as Code
 

### Languages & Tools
 - Python – Lambda business logic
 - AWS CLI – Deployment & operations
 - boto3 – AWS SDK for Python
 - Git & GitHub – Version control

## How It Works
#### Frontend flow
 - Collects event details from the user
 - Sends HTTP requests to the API Gateway endpoint
 - Contains no AWS credentials or business logic  

#### Backend flow

  -API Gateway exposes a POST /create-event endpoint
  -Lambda receives the request via proxy integration
  -Request body is parsed and validated
  -A clean, dynamic email message is generated
  -SNS sends notifications to confirmed subscribers

#####  Input Validation & Error Handling
The API handles common client errors:
  -Missing request body
  -Invalid JSON
  -Missing required fields (title, date, description)

Responses follow HTTP standards:
  -200 OK → Event processed successfully
  -400 Bad Request → Invalid input

This ensures API professionalism and predictable behavior.

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

The stack includes:
  -IAM role for Lambda
  -SNS topic & subscriptions
  -Lambda function
  -API Gateway REST API

## Security Consideration
 - IAM roles follow least-privilege principles
 - Lambda can only publish to the specific SNS topic it needs
 - No AWS credentials are exposed to the frontend
 - API Gateway acts as the controlled public entry point
 - Email subscriptions require manual confirmation (SNS security model)

## Deployment (will be updated as project finishes updated due : 19 jan 2026)
- Prerequisites
- High-level deploy steps (no commands yet)

## Design Decisions & Trade-offs (will be updated as project finishes updated due : 19 jan 2026)
- Why serverless
- Optional components explained

## What I Learned
- Designing serverless architectures instead of writing ad-hoc code
- Difference between infrastructure changes vs application code changes
- CloudFormation stack lifecycle and rollback behavior
- Debugging real AWS deployment issues using stack events
- API Gateway → Lambda proxy integration
- Secure IAM policy design
- Event-driven communication using SNS
- Importance of input validation and error handling in APIs
- Real-world deployment workflows (artifacts, S3, updates)

## Future Improvements (will be updated as project finishes updated due : 19 jan 2026)
- Auth
- Persistence
- Observability
