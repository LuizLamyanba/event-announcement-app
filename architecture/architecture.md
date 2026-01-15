# Event Announcement Application – Architecture

## Overview
The Event Announcement Application is a fully serverless, event-driven system built on AWS.
It enables users to create and distribute event announcements through a lightweight web interface,
with email notifications delivered automatically to subscribed users.

The architecture is designed to be **simple, scalable, secure, and cost-efficient**, following
AWS best practices and real-world cloud design principles.

---

## High-Level Architecture
The system follows a **left-to-right request flow**, as shown in the architecture diagram:

User (Web Browser)  
→ Amazon S3 (Static Website)  
→ Amazon API Gateway (Public REST API)  
→ AWS Lambda (Application Logic)  
→ Amazon SNS (Email Notifications)  
→ Email Subscribers

Each component has a clearly defined responsibility, ensuring a clean separation of concerns.

---

## Architecture Diagram
The diagram visually represents how requests flow through the system from the user interface
to the notification layer.

![core serverless architecture di](https://github.com/LuizLamyanba/event-announcement-app/blob/main/architecture/core%20flow%20architecture.png)


---

## Component Breakdown

### 1. User (Web Browser)
Users interact with the application using a standard web browser.
All communication with the backend happens securely over HTTPS.

Responsibilities:
- Access the frontend
- Submit event creation or subscription requests

---

### 2. Amazon S3 – Static Website Hosting
Amazon S3 hosts the frontend assets (HTML, CSS, and JavaScript) as a static website.

Responsibilities:
- Serve static content to users
- Execute frontend JavaScript logic
- Send API requests to Amazon API Gateway
- Store no AWS credentials or secrets

Why S3:
- Highly available
- Cost-effective
- No server management required

---

### 3. Amazon API Gateway – Public REST API
Amazon API Gateway serves as the public entry point for backend operations.

Responsibilities:
- Receive HTTP requests from the frontend
- Route requests to the appropriate Lambda function
- Enforce request validation and throttling
- Provide secure HTTPS endpoints

Why API Gateway:
- Native integration with AWS Lambda
- Built-in scaling and security features
- Ideal for serverless architectures

---

### 4. AWS Lambda – Application Logic
AWS Lambda contains the core business logic of the application.

Responsibilities:
- Validate incoming requests
- Process event announcement data
- Handle subscription logic
- Publish messages to Amazon SNS
- Execute without managing servers

Why Lambda:
- Automatic scaling
- Pay-per-execution pricing
- Stateless and highly reliable

---

### 5. Amazon SNS – Email Notifications
Amazon Simple Notification Service (SNS) is used to distribute event announcements via email.

Responsibilities:
- Receive messages from Lambda
- Fan-out notifications to all email subscribers
- Manage email delivery and retries

Why SNS:
- Decouples notification delivery from application logic
- Supports multiple subscribers
- Highly scalable and fault-tolerant

---

### 6. Email Subscribers
Subscribers receive event announcements through email.
They are managed entirely by Amazon SNS.

---

## Architecture Characteristics

- Fully serverless
- Event-driven communication
- No infrastructure management
- Automatic scaling
- High availability
- Cost-efficient (pay-as-you-use)
- Secure by design

---

## Design Decisions

- **S3 over EC2**: Static hosting eliminates server maintenance
- **API Gateway over ALB**: Purpose-built for serverless APIs
- **Lambda over containers**: Simplifies scaling and deployment
- **SNS over direct email handling**: Enables reliable fan-out and decoupling

---

## Conclusion
This architecture demonstrates a production-style serverless design that balances simplicity,
scalability, and maintainability. The clear separation of responsibilities makes the system easy
to extend, secure, and operate in real-world environments.
