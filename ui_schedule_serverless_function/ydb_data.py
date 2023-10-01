import json
import logging
import os
import datetime

import boto3
from botocore.exceptions import ClientError

"""
message.from_user.id
message.from_user.first_name
message.from_user.last_name
message.from_user.username
"""

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

def create_user(message, dynamodb=None):

    if not dynamodb:
            dynamodb = get_dynamodb_resource()

    table = dynamodb.Table('Users')
    time_zone = datetime.timezone(datetime.timedelta(hours=3))
    response = table.put_item(
        Item={
        'user_id': str(message.from_user.id),
        'first_name': str(message.from_user.first_name),
        'register_date': datetime.date.today().strftime('%Y-%m-%d'),
        'last_seen': datetime.datetime.now(tz=time_zone).strftime('%Y-%m-%d %H:%M:%S')
        }
    )

    return response
    
def set_schedule_type(user_id, schedule_type, dynamodb=None):

    if not dynamodb:
        dynamodb = get_dynamodb_resource()

    table = dynamodb.Table('Users')
    
    if schedule_type not in ['student', 'teacher']:
        return "Invalid group_type. Must be 'student' or 'teacher'."
    
    response = table.update_item(
        Key={
            'user_id': str(user_id),
        },
        UpdateExpression="set schedule_type = :s",
        ExpressionAttributeValues={
            ':s': str(schedule_type),
        },
        ReturnValues="UPDATED_NEW"
    )

    return response

def get_schedule_type(user_id, dynamodb=None):

    if not dynamodb:
        dynamodb = get_dynamodb_resource()

    table = dynamodb.Table('Users')
    try:
        response = table.get_item(Key={'user_id': str(user_id)})
    except ClientError as e:
        print(e.response['Error']['Message'])
        return False
    
    if 'Item' in response:
        user_data = response['Item']
        if 'schedule_type' in user_data:
            if user_data['schedule_type'] in ['student', 'teacher']:
                return True, user_data['schedule_type']
            else:
                return False, "Invalid value for schedule_type"
        else:
            return False, "schedule_type not set"
    else:
        return False, "User does not exist"




def set_group_number(user_id, group_number, dynamodb=None):

    if not dynamodb:
        dynamodb = get_dynamodb_resource()

    table = dynamodb.Table('Users')
    response = table.update_item(
        Key={
            'user_id': str(user_id),
        },
        UpdateExpression="set #gn = :g",
        ExpressionAttributeNames={'#gn': 'group_number'},
        ExpressionAttributeValues={':g': str(group_number)},
        ReturnValues="UPDATED_NEW"
    )

    return response

def set_teacher_name(user_id, teacher_name, dynamodb=None):
    if not dynamodb:
        dynamodb = get_dynamodb_resource()

    table = dynamodb.Table('Users')
    response = table.update_item(
        Key={
            'user_id': str(user_id),
        },
        UpdateExpression="set #tn = :n",
        ExpressionAttributeNames={'#tn': 'teacher_name'},
        ExpressionAttributeValues={':n': str(teacher_name)},
        ReturnValues="UPDATED_NEW"
    )
    return response

def set_teacher_uid(user_id, teacher_uid, dynamodb=None):
    if not dynamodb:
        dynamodb = get_dynamodb_resource()

    table = dynamodb.Table('Users')
    response = table.update_item(
        Key={
            'user_id': str(user_id),
        },
        UpdateExpression="set #tuid = :u",
        ExpressionAttributeNames={'#tuid': 'teacher_uid'},
        ExpressionAttributeValues={':u': str(teacher_uid)},
        ReturnValues="UPDATED_NEW"
    )
    return response

def set_chat_id(user_id, chat_id, dynamodb=None):

    if not dynamodb:
        dynamodb = get_dynamodb_resource()

    table = dynamodb.Table('Users')
    response = table.update_item(
        Key={
            'user_id': str(user_id),
        },
        UpdateExpression="set #chid = :c",
        ExpressionAttributeNames={'#chid': 'chat_id'},
        ExpressionAttributeValues={':c': str(chat_id)},
        ReturnValues="UPDATED_NEW"
    )
    return response

def set_notify_before_lessons(user_id, bool_flag, dynamodb=None):
    if not dynamodb:
            dynamodb = get_dynamodb_resource()

    table = dynamodb.Table('Users')
    response = table.update_item(
        Key={
            'user_id': str(user_id),
        },
        UpdateExpression="set #nbl = :n",
        ExpressionAttributeNames={'#nbl': 'notify_before_lessons'},
        ExpressionAttributeValues={':n': bool_flag},
        ReturnValues="UPDATED_NEW"
    )
    return response

def set_notify_every_day(user_id, time, dynamodb=None):

    if not dynamodb:
            dynamodb = get_dynamodb_resource()

    table = dynamodb.Table('Users')
    response = table.update_item(
        Key={
            'user_id': str(user_id),
        },
        UpdateExpression="set #ned = :n",
        ExpressionAttributeNames={'#ned': 'notify_every_day'},
        ExpressionAttributeValues={':n': time},
        ReturnValues="UPDATED_NEW"
    )
    return response

def get_group_number(user_id, dynamodb=None):
    if not dynamodb:
        dynamodb = get_dynamodb_resource()

    table = dynamodb.Table('Users')
    try:
        response = table.get_item(Key={'user_id': str(user_id)})
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None
    
    if 'Item' in response:
        user_data = response['Item']
        return user_data.get('group_number', None)
    else:
        return None

def get_teacher_name(user_id, dynamodb=None):
    if not dynamodb:
        dynamodb = get_dynamodb_resource()

    table = dynamodb.Table('Users')
    try:
        response = table.get_item(Key={'user_id': str(user_id)})
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None
    
    if 'Item' in response:
        user_data = response['Item']
        return user_data.get('teacher_name', None)
    else:
        return None

def get_chat_id(user_id, dynamodb=None):

    if not dynamodb:
        dynamodb = get_dynamodb_resource()

    table = dynamodb.Table('Users')
    try:
        response = table.get_item(Key={'user_id': str(user_id)})
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None
    
    if 'Item' in response:
        user_data = response['Item']
        return user_data.get('chat_id', None)
    else:
        return None

def chat_id_check_set(message):
    chat_id = get_chat_id(message.from_user.id)
    if chat_id==None or chat_id!=message.chat.id: 
        set_chat_id(message.from_user.id, message.chat.id)


def set_last_seen(user_id, dynamodb=None):

    if not dynamodb:
        dynamodb = get_dynamodb_resource()

    table = dynamodb.Table('Users')
    time_zone = datetime.timezone(datetime.timedelta(hours=3))
    response = table.update_item(
        Key={
            'user_id': str(user_id),
        },
        UpdateExpression="set #ls = :l",
        ExpressionAttributeNames={'#ls': 'last_seen'},
        ExpressionAttributeValues={':l': datetime.datetime.now(tz=time_zone).strftime('%Y-%m-%d %H:%M:%S')},
        ReturnValues="UPDATED_NEW"
    )

    return response

def increment_user_action_counter(user_id, dynamodb=None):

    if not dynamodb:
        dynamodb = get_dynamodb_resource()
        
    table = dynamodb.Table('Users')

    try:
        response = table.update_item(
            Key={'user_id': str(user_id)},
            UpdateExpression='ADD actions_counter :incr',
            ExpressionAttributeValues={':incr': 1},
            ReturnValues="UPDATED_NEW"
        )
        
        # Printing for debugging purposes
        print("UpdateItem succeeded:", response)
        
    except Exception as e:
        print("Error updating item:", e)

