import json
import os
import boto3

sns = boto3.client("sns")

def handler(event,context):
    message = "New event created succesfully"

    sns.publish(
        TopicArn=os.environ["SNS_TOPIC_ARN"],
        Message=message,
        Subject="Event Announcement"
    )

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": "Event created and notification sent"})
    }