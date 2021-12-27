import os
import logging
import boto3
from botocore.exceptions import ClientError
from PIL import Image
import smtplib
import imghdr
from email.message import EmailMessage
import hybrid



#upload
def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


#menu
print ("Welcome to cloud")
print ("# Press 1 to upload file")
print ("# Press 2 to download file")
print ("# other key to exit")
op=int(input())
if (op== 1):
    file_location=input("Enter file name with path: (with \\1) ")
    buck=input("Enter the bucket name: ")
    obj=input("Enter the object name: ")
    #try:
    hybrid.main()
        #upload_file(file_location, buck, obj)
    print("DONE!")
        
    #except:
    print ("")

elif (op==2):
    buck1= input("Enter bucket name :")
    obj1= input("Enter Object name: ")
    file1= input("Enter File name: ")
    #initiate s3 resource1
    s3 = boto3.resource("s3")
    # select bucket
    bucket = s3.Bucket("bucket name")
    # download file into current directory
    for s3_object in bucket.objects.all():
        # Need to split s3_object.key into path and file name, else it will give error file not found.
        path, filename = os.path.split(s3_object.key)
        bucket.download_file(s3_object.key, filename)
else:
    os._exit(0)
