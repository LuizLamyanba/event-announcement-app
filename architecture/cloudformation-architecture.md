
Each resource is explicitly connected using CloudFormation references, ensuring clear dependencies and controlled permissions.

---
![cloudformation architecture diagram](<../snippets/cloudformation architecture flow diagram.png>)

## Step-by-Step Resource Flow

### 1. Amazon SNS (Notification Layer)

- An SNS topic is created to broadcast event announcements.
- An email subscription is attached to the topic.
- Email delivery requires manual confirmation by the subscriber.

Purpose:
- Decouples notification delivery from application logic
- Enables fan-out and scalable messaging

---

### 2. IAM Role for Lambda (Security Layer)

- A dedicated IAM role is created for the Lambda function.
- Permissions granted:
  - CloudWatch Logs (for observability)
  - SNS `Publish` permission (restricted to the specific topic)

Purpose:
- Enforces least-privilege access
- Prevents unauthorized access to AWS services

---

### 3. AWS Lambda Function (Application Logic)

- The Lambda function contains all business logic.
- It receives HTTP requests from API Gateway.
- Validates input, formats messages, and publishes to SNS.
- SNS topic ARN is injected using environment variables.

Purpose:
- Stateless, scalable application logic
- No server management required

---

### 4. API Gateway (Public API Layer)

- A REST API is created as the public entry point.
- The `/create-event` resource accepts `POST` requests.
- Lambda proxy integration is used.
- API Gateway is explicitly granted permission to invoke Lambda.

Purpose:
- Acts as a secure HTTP interface
- Decouples frontend from backend logic

---

### 5. Deployment & Outputs

- The API is deployed to the `prod` stage.
- The final API endpoint URL is exposed as a CloudFormation output.

Purpose:
- Enables frontend and testing tools to consume the API
- Ensures reproducibility across environments

---

## Architectural Principles Followed

- Infrastructure as Code (IaC)
- Least-privilege IAM
- Serverless-first design
- Event-driven communication
- Explicit resource dependencies

This CloudFormation template represents the **single source of truth** for backend infrastructure.
