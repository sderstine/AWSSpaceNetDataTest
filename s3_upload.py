import boto3
import json
import rasterio
import os
from rasterio.plot import show


os.environ['GDAL_HTTP_UNSAFESSL'] = 'YES'

def download_and_open(bucket_name, s3_key):
    # Initialize Boto3 S3 client
    s3 = boto3.client('s3',
                      aws_access_key_id='YOUR_ACCESS_KEY_ID',
                      aws_secret_access_key='YOUR_SECRET_ACCESS_KEY',
                      region_name='us-east-2')

    # Download the JSON file from S3
    response = s3.get_object(Bucket=bucket_name, Key=s3_key)

    # Read the content of the file
    json_data = response['Body'].read()

    # Decode the JSON data into a Python dictionary
    json_dict = json.loads(json_data)

    return json_dict

# # Example usage:
# bucket_name = 'test_Maxar'
# s3_key = 's3://cic-cm-intern2024-storage/ingest/test_Maxar/'
# data_dict = download_and_open(bucket_name, s3_key)

# # Now you can use the 'data_dict' dictionary
# print(data_dict)
def open_image(image_path):
    with rasterio.open(image_path) as dataset:
        image = dataset.read()
        metadata = dataset.meta

    #show(image)
    return image, metadata