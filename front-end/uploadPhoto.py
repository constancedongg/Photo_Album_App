import json
import base64
import boto3
import random
import string

def lambda_handler(event, context):
	s3 = boto3.client("s3")
	# retrieving data from event
	print(event)
	get_file_content = event["body"]
	file_name = ''.join(random.sample(string.ascii_letters + string.digits, 8)) + '.jpg'
	print(file_name)
	# decoding data
	print('before')
	print(get_file_content)
	print(type(get_file_content))
	decode_content = base64.b64decode(get_file_content)
	print('after')
	# decode_content = decode_content.decode('ascii')
	print(decode_content)
	print(type(decode_content))
	# decode_content = json.loads(decode_content)
	# image = decode_content["image"]
	# print(image)
	
	# uploading file to S3 bucket
	s3_upload = s3.put_object(Bucket="photob2", Key=file_name, Body=decode_content)

	return {
        "statusCode": 200,
        "body": file_name
        }
#test one more time