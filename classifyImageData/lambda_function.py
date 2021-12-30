import json
import base64
import boto3

# Fill this in with the name of your deployed model
ENDPOINT = 'image-classification-2021-12-30-01-54-59-242'
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['body']['image_data'])
    print(image)
    
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType='image/png',
        Body=image)

    print(response)
    
    result = json.loads(response['Body'].read().decode('utf-8'))

    return {
        'statusCode': 200,
        'inferences': result
    }