# Cannary Tokens

Description: Tracks if a link has been opened -> a resources was accessed. Only be implementing web token (HTTP request).

Requirements:
- Collect requester (User-Agent, IP, Headers) information when the link is opened
- Store that information somewhere (database -> Dynamodb)
- Notify when a links has been invoked (called/opened)

-> AWS API Acesss Gateway -> ([Python] -> AWS Lambda Function) -> DynamoDB

Lambda Functions:
- create_cannary_handler.py: Creates unique tokens for cannary
- cannary_handler.py: Listener for events
- notify_handler.py: notifies a user when events occur

<!-- EOF -->