import pytest
import time
import os
from decimal import *

import boto3
from moto import mock_dynamodb



@mock_dynamodb
@pytest.mark.unit
def test_dynamodb2_resource() :

    table_name = "Test Table"
    id = "some id"
    key = {
         'id': id
    }

    dynamodb = boto3.resource('dynamodb')
    assert dynamodb is not None, "No se ha recuperado el recurso dynamodb"

    client = dynamodb.meta.client
    assert client is not None, "No hay hacceso al cliente dynamodb"

    presigned_url = client.generate_presigned_url("get_item", {'TableName': table_name, 'Key': key}) 
    assert  presigned_url.startswith("https://dynamodb.us-east-1.amazonaws.com/?TableName=Test"), "No se ha detectado una URL correcta"
    
    

