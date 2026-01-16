import json
import os
import boto3

sns = boto3.client("sns")

REQUIRED_FIELDS = ["title", "date", "description"]

def handler(event, context):
    # Check if body exists
    if "body" not in event or not event["body"]:
        return response(400, "Request body is missing")

    #  Parse JSON safely
    try:
        body = json.loads(event["body"])
    except json.JSONDecodeError:
        return response(400, "Invalid JSON format")

    # Validate required fields
    missing_fields = [f for f in REQUIRED_FIELDS if f not in body or not body[f]]
    if missing_fields:
        return response(
            400,
            f"Missing required fields: {', '.join(missing_fields)}"
        )

    title = body["title"]
    date = body["date"]
    description = body["description"]

    #  Create clean email message
    message = (
        f"📢 New Event Announced!\n\n"
        f"Title: {title}\n"
        f"Date: {date}\n\n"
        f"Description:\n{description}\n"
    )

    #  Publish to SNS
    sns.publish(
        TopicArn=os.environ["SNS_TOPIC_ARN"],
        Subject=f"New Event: {title}",
        Message=message
    )

    #  Success response
    return response(200, "Event created and notification sent")


def response(status_code, message):
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": message})
    }
