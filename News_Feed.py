import json
import boto3


def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('sns')
    
    print(event['Records'][0]['eventName'])
    
    if event['Records'][0]['eventName'] != "INSERT":
        pass
    else:
        values = event['Records'][0]['dynamodb']["NewImage"]
    
        title = values["Title"]["S"]
        date = values["Date"]["S"]
        link = values["Link"]["S"]
        category = values["Category"]["S"]
        
        response = client.publish(
        TopicArn='arn:aws:sns:us-west-2:<REDACTED>:AWS_NEWS_FEED_2',
        Message=f"{title}\n\n{link}",
        Subject=f'[{category}] AWS News Post'
    )