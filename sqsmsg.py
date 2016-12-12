import boto3


sns = boto3.client('sns')
#topic = sns.Topic('oca-sns-test')

# Test sending an SNS to a topic.
sns.publish(
    PhoneNumber='00447792731440',
    Message='Testing Python SDK SNS.'
    #MessageStructure='string'
    #MessageAttributes={
    #    'string': {
    #        'DataType': 'string',
    #        'StringValue': 'string',
    #        'BinaryValue': b'bytes'
    #    }
    #}
)
