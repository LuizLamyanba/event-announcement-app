# IAM Permissions Overview

## Lambda Execution Role
Permissions:
- logs:CreateLogGroup
- logs:CreateLogStream
- logs:PutLogEvents
- sns:Publish (specific topic only)

## Frontend
- No AWS credentials
- Communicates only via API Gateway

## API Gateway
- Public HTTP entry point
- No direct access to SNS or IAM
