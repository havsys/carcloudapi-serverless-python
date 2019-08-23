import json
import uuid
import os
from datetime import datetime
from models.Campaign import createCampaign

def create(event, context):
    try:
        data = json.loads(event['body'])
    except json.decoder.JSONDecodeError as e:
        return {
            'statusCode': 422,
            'body': json.dumps({
                'description': 'Invalid object provided',
                'content': {
                    'reason': 'Api validation error',
                    'errors': [
                        {
                            'field': '',
                            'message': 'JSON parse exception'
                        }
                    ]
                }
            })
        } 
    if 'template_id' not in data:
        return {
            'statusCode': 422,
            'body': json.dumps({
                'description': 'Invalid object provided',
                'content': {
                    'reason': 'Api validation error',
                    'errors': [
                        {
                            'field': 'template_id',
                            'message': 'Missing field template_id'
                        }
                    ]
                }
            })
        }
    if 'target_url' not in data:
        return {
            'statusCode': 422,
            'body': json.dumps({
                'description': 'Invalid object provided',
                'content': {
                    'reason': 'Api validation error',
                    'errors': [
                        {
                            'field': 'target_url',
                            'message': 'Missing field target_url'
                        }
                    ]
                }
            })
        }   
    # datetime object containing current date and time
    now = datetime.now()
    # item to be stored on database
    item = {
        'id': str(uuid.uuid4()),
        'client_id': ('' if 'client_id' not in data else data['client_id']),
        'template_id': data['template_id'],
        'company_type': ('AUTOMATIC' if 'company_type' not in data else data['company_type']),
        'target_url': data['target_url'],
        'schedule': ('' if 'schedule' not in data else data['schedule']),
        'phone_field_name': ('' if 'phone_field_name' not in data else data['phone_field_name']),
        'mobile_field_name': ('' if 'mobile_field_name' not in data else data['mobile_field_name']),
        'billing_reference_field_name': ('' if 'billing_reference_field_name' not in data else data['billing_reference_field_name']),
        'message_content': ('' if 'message_content' not in data else data['message_content']),
        'sender_name': ('' if 'sender_name' not in data else data['sender_name']),
        'created_at': now.strftime("%d/%m/%Y %H:%M:%S"),
        'updated_at': now.strftime("%d/%m/%Y %H:%M:%S"),
        'deleted_at': ''
    }
    
    if createCampaign(item) == True:
        return {
            "statusCode": 200,
            "body": json.dumps({
                'description': 'Campaign created successfully',
                'content': item
            })
        }
    else:
        return {
            "statusCode": 500,
            "body": json.dumps({
                'description': 'Internal server error'
            })
        }
