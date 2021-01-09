import pytest
import time
import os
from decimal import *

import boto3
import json

from todos.get import get
from todos import decimalencoder


@pytest.mark.api
def test_get():

    table_name = "todo_test_table"
    id = 'some todo id'
    text = 'text of body'
    timestamp = Decimal(time.time())
    item = {
        'id': id,
        'text': text,
        'checked': False,
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }
        
    context = {}
    event = {
        'pathParameters': {
            'id': id
        }
    }

    os.environ['DYNAMODB_TABLE'] = table_name

    dynamodb = boto3.resource('dynamodb', 'us-east-1')
    table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
    )
    try:

        # Wait until the table exists.
        table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
        if (table.table_status != 'ACTIVE'):
            raise AssertionError()
    

        table.put_item(Item=item)

        response = get(event, context)

        print("Response : " + json.dumps(response))
        print("Item : " + json.dumps(item, cls=decimalencoder.DecimalEncoder))

        assert response['statusCode'] == 200, "Operación ha devuelto resultado correcto"
        assert response['body'] == json.dumps(item, cls=decimalencoder.DecimalEncoder), "El cuerpo de la respuesta no es el esperado"
        table.delete()
    except:
        table.delete()
