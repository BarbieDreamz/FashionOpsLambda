#I was working on something and decided if I'm going to write some code I should at least publish it. This is how to enable versioning on an S3 bucket using Lambda.

import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    response = s3.list_buckets()
    buckets = response['Buckets']

    for bucket in buckets:
        bucket_name = bucket['Name']
        try:
            s3.put_bucket_versioning(Bucket=bucket_name, VersioningConfiguration={'Status': 'Enabled'})
            print(f"Enabled versioning for bucket: {bucket_name}")
        except Exception as e:
            print(f"Error enabling versioning on {bucket_name}: {e}")

    return {'statusCode': 200, 'body': 'Versioning enabled for buckets'}

#I gave my IAM user full access for S3 and Lambda then threw in EC2 because why not. ALSO, it's my code soo....https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_versioning.html
