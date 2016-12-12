import boto3

# Using S3
s3 = boto3.resource('s3')

# Print buckets

for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a file to a bucket
data = open('buckets.txt', 'rb')
s3.Bucket('oca-guru-bucket').put_object(Key='buckets.txt', Body=data)
