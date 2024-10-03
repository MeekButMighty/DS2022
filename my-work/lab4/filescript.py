#!/usr/bin/env python3

import urllib.request
url = "https://s2.glbimg.com/xT8ywXOVA8DMoYG0FddeQtKIh0I=/e.glbimg.com/og/ed/f/original/2021/03/14/gettyimages-1307116129.jpg"
save_path = 'queenbey.jpg'
urllib.request.urlretrieve(url, save_path)

import boto3 
bucket_name = 'ds2022-azt6gn'
s3_client = boto3.client('s3')
s3_client.upload_file(save_path, bucket_name, save_path, ExtraArgs={'ContentType': 'image/jpeg'})

import logging

s3_client = boto3.client('s3')
response = s3_client.generate_presigned_url('get_object',Params={'Bucket': bucket_name, 'Key': save_path}, ExpiresIn=604800)
print (response)

#https://ds2022-azt6gn.s3.amazonaws.com/queenbey.jpg?AWSAccessKeyId=AKIAWOOXUDZ5RYPC3PNA&Signature=%2Be8DYU6M0szQ3AcEdSnUf8Cmtvo%3D&Expires=1728244649
