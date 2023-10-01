import json
import logging
import os
import datetime

import boto3
from botocore.exceptions import ClientError

def get_dynamodb_resource():
    try: 
        return boto3.resource(
                'dynamodb',
                endpoint_url=os.environ.get('USER_STORAGE_URL'),
                region_name = 'us-east-1',
                aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
        )
    except Error as e:
        print(e)

def get_all_items(table):
    # Scan the DynamoDB table and return all items
    response = table.scan()
    return response['Items']

def loop_through_items(items):
    # Loop through items and return a dictionary that meets the specified criteria
    result_dict_one = []
    result_dict_two = []
    for item in items:
        criteria_result = check_criteria(item)
        if criteria_result:
            if criteria_result['notify_every_day']:
                result_dict_one.append(criteria_result)
            if criteria_result['notify_before_lessons']:
                result_dict_two.append(criteria_result)
            
    return result_dict_one, result_dict_two

def return_notifier_list():
    #print("run return_notifier_list")
    dynamodb = get_dynamodb_resource()
    table = dynamodb.Table('Users')
    items = get_all_items(table)
    #print("items: ", items)
    result_one, result_two = loop_through_items(items)
    return result_one, result_two

def get_user(user_id, dynamodb=None):
    if not dynamodb:
        dynamodb = get_dynamodb_resource()

    table = dynamodb.Table('Users')
    try:
        response = table.get_item(Key={'user_id': str(user_id)})
    except ClientError as e:
        return None

    if 'Item' in response:
        return True, response['Item']
    else:
        return False, None

def check_criteria(item):

    user_id = item.get('user_id', None)
    
    if user_id is None:
        return None
    
    chat_id = item.get('chat_id', None)
    schedule_type = item.get('schedule_type', None)
    group_number = item.get('group_number', None)
    teacher_uid = item.get('teacher_uid', None)
    notify_every_day = item.get('notify_every_day', None)
    notify_before_lessons = item.get('notify_before_lessons', None)

    if schedule_type and chat_id and (group_number or teacher_uid) and (notify_every_day or notify_before_lessons):
        temp_dict = {
            'user_id': user_id,
            'chat_id': chat_id,
            'schedule_type': schedule_type,
            'group_number': group_number,
            'teacher_uid': teacher_uid, 
            'notify_every_day': notify_every_day,
            'notify_before_lessons': notify_before_lessons
        }   
        return temp_dict
    else:
        return None