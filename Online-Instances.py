import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }
        ]
    )
    running_instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_name = 'Unknown'
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    instance_name = tag['Value']
            running_instances.append({
                'InstanceId': instance_id,
                'InstanceName': instance_name
            })

    # Return the list of running instances
    return {
        'statusCode': 200,
        'body': {
            'RunningInstances': running_instances
        }
    }
