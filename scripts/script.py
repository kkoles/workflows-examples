import gzip
from io import TextIOWrapper, BytesIO
import requests
from requests.auth import HTTPBasicAuth
import json
import boto3
import botocore
import datetime
import sys
import os


number_of_days = int(sys.argv[1])
logs_s3_bucket = str(sys.argv[2])
output_file    = str(sys.argv[3])
user = str(sys.argv[4])

# Get environment variables
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_S3_LOGS_BUCKET = os.getenv('AWS_S3_LOGS_BUCKET')

if __name__ == "__main__":
    print(f"""
    NUMBER OF DAYS: {number_of_days}
    LOGS BUCKET: {AWS_S3_LOGS_BUCKET}
    USER: {USER}
    AWS_ACCESS_KEY_ID: {AWS_ACCESS_KEY_ID }
    """)
