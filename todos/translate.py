import os
import json
import random
import string

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def translate(event, context):
    letters = string.ascii_lowercase
    iam_role = "arn:aws:iam::040478882905:role/TranslateTemporarySessionRol"
    iam_role = "arn:aws:iam::040478882905:user/translateuser"
    sts_client = boto3.client('sts')
    assumed_role_object=sts_client.assume_role(
        RoleArn=iam_role,
        RoleSessionName=''.join(random.choice(letters) for i in range(16)))
    credentials=assumed_role_object['Credentials']

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    item = result['Item']

    translate = boto3.client(service_name = 'translate',
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken'])
    tr_result = translate.translate_text(Text = item['text'], SourceLanguageCode="auto", TargetLanguageCode=event['pathParameters']['lang'])

    item['text'] = tr_result.get('TranslatedText')

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item,
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
