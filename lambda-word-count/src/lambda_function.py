import json
import boto3
from utils.word_counter import count_words

def lambda_handler(event, context):
    # Initialize SNS client
    sns_client = boto3.client('sns')
    
    # Get the bucket name and file name from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    
    # Get the S3 resource
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket_name, file_name)
    
    # Read the content of the file
    file_content = obj.get()['Body'].read().decode('utf-8')
    
    # Count the words using the utility function
    word_count = count_words(file_content)
    
    # Prepare the message
    message = f"The word count in the {file_name} file is {word_count}."
    
    # Publish the result to SNS
    sns_topic_arn = 'arn:aws:sns:your-region:your-account-id:your-sns-topic'  # Replace with your SNS topic ARN
    sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=message,
        Subject='Word Count Result'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }