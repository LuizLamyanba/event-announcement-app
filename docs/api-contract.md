# API Contract – Create Event

## Endpoint
POST /create-event

## Headers
Content-Type: application/json

## Request Body
{
  "title": "string",
  "date": "YYYY-MM-DD",
  "description": "string"
}

## Success Response (200)
{
  "message": "Event created and notification sent"
}

## Error Responses
400 – Missing or invalid input
