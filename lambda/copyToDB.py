# pylint: disable=no-member, disable=import-error
import csv
import os
import boto3

s3 = boto3.resource('s3')
db_client = boto3.client('dynamodb')

table = 'trainingTable'
obj = s3.Object('csv-training', 'data.csv').get()

def lambda_handler(event, context):   
    
    lines = obj['Body'].read().decode('utf-8').splitlines()

    for row in range(0, 3):
        line = lines[row].split(',')
        print(line)
        db_client.put_item(TableName = table, Item = put_item_db(line[0], line[1], line[2], line[3]))
    
    return {
      'body': 'ok'
    }

def put_item_db(n0, n1, n2, n3):
    db_item = {
        'id': {'S': n0 },
        'col1': {'S': n1 },
        'col2': {'S': n2 },
        'col3': {'S': n3 }
    }
    return db_item