import gzip
from io import TextIOWrapper, BytesIO
import requests
from requests.auth import HTTPBasicAuth
import json
import boto3
import botocore
import datetime
import sys

number_of_days = int(sys.argv[1])
logs_s3_bucket = str(sys.argv[2])
output_file    = str(sys.argv[3])
user = str(sys.argv[4])

if __name__ == "__main__":
    print(f"""
    NUMBER OF DAYS: {number_of_days}
    LOGS BUCKET: {logs_s3_bucket}
    OUTPUT_FILE: {output_file}
    USER: {user}
    """)
