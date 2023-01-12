import json
import time

# Wait for 1 second to create an artificially long cold start
time.sleep(1)

def lambda_handler(event, context):
    # Sleep for 100ms to simulate work
    time.sleep(0.1)

    # Return a response to the API Gateway
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        }),
    }

