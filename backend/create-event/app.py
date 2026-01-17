import json
import os
import boto3

sns = boto3.client("sns")

REQUIRED_FIELDS = ["title", "date", "description"]

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "OPTIONS,POST",
    "Access-Control-Allow-Headers": "Content-Type"
}

def handler(event, context):
    # Handle CORS preflight
    if event.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": CORS_HEADERS,
            "body": ""
        }

    # Check if body exists
    if "body" not in event or not event["body"]:
        return response(400, "Request body is missing")

    # Parse JSON safely
    try:
        body = json.loads(event["body"])
    except json.JSONDecodeError:
        return response(400, "Invalid JSON format")

    # Validate required fields
    missing_fields = [
        field for field in REQUIRED_FIELDS
        if field not in body or not body[field]
    ]

    if missing_fields:
        return response(
            400,
            f"Missing required fields: {', '.join(missing_fields)}"
        )

    title = body["title"]
    date = body["date"]
    description = body["description"]

    # Create clean email message
    message = (
        f"📢 New Event Announced!\n\n"
        f"Title: {title}\n"
        f"Date: {date}\n\n"
        f"Description:\n{description}\n"
    )

    # Publish to SNS
    sns.publish(
        TopicArn=os.environ["SNS_TOPIC_ARN"],
        Subject=f"New Event: {title}",
        Message=message
    )

    return response(200, "Event created and notification sent")


def response(status_code, message):
    return {
        "statusCode": status_code,
        "headers": {
            **CORS_HEADERS,
            "Content-Type": "application/json"
        },
        "body": json.dumps({"message": message})
    }
