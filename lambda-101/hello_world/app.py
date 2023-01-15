import json
import random


# def lambda_handler(event, context):
#
#     # Return a response to the API Gateway
#     return {
#         "statusCode": 200,
#         "body": json.dumps({
#             "message": "hello from version 2"
#         }),
#     }



def lambda_handler(event, context):

    # Pick a number between 0 and 200.
    # If the value is zero, raise an Exception.
    val = random.randrange(0, 200)
    if val == 0:
        raise Exception("something went wrong!")

    # Return a response to the API Gateway
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        }),
    }

