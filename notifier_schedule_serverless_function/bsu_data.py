import os
import requests
import datetime

from view import transform_json_to_ouptut_format
from ydb_data import get_user
from local_data import get_schedule_type_from_user, get_group_number_from_user, get_teacher_id_from_user, get_date_today, get_date_tomorrow, return_period_from_today_until_saturday, get_date_this_week, get_date_next_week

def make_base_url(user):
    schedule_type = get_schedule_type_from_user(user)
    if schedule_type=='student':
        
        return os.environ.get('BASE_URL_STUDENT')
    elif schedule_type=='teacher':
        
        return os.environ.get('BASE_URL_TEACHER')

def make_params_today(user):

    schedule_type = get_schedule_type_from_user(user)
    period = 1
    date = get_date_today()

    params = {
        "os": "android",
        "date": date,
        "period": period
        }

    if schedule_type == 'student':
        params["group"] = get_group_number_from_user(user)
    elif schedule_type == 'teacher':
        params["teachid"] = get_teacher_id_from_user(user)
    
    return params

def make_params_tomorrow(user):

    schedule_type = get_schedule_type_from_user(user)
    period = 1
    date = get_date_tomorrow()

    params = {
        "os": "android",
        "date": date,
        "period": period
        }

    if schedule_type == 'student':
        params["group"] = get_group_number_from_user(user)
    elif schedule_type == 'teacher':
        params["teachid"] = get_teacher_id_from_user(user)
    
    return params

def make_params_from_today_until_saturday(user):

    schedule_type = get_schedule_type_from_user(user)
    date = get_date_today()
    period = return_period_from_today_until_saturday()

    params = {
        "os": "android",
        "date": date,
        "period": period
        }

    if schedule_type == 'student':
        params["group"] = get_group_number_from_user(user)
    elif schedule_type == 'teacher':
        params["teachid"] = get_teacher_id_from_user(user)
    
    return params

def make_params_this_week(user):

    schedule_type = get_schedule_type_from_user(user)
    date = get_date_this_week()
    period = 6

    params = {
        "os": "android",
        "date": date,
        "period": period
        }

    if schedule_type == 'student':
        params["group"] = get_group_number_from_user(user)
    elif schedule_type == 'teacher':
        params["teachid"] = get_teacher_id_from_user(user)
    
    return params

def make_params_next_week(user):

    schedule_type = get_schedule_type_from_user(user)
    date = get_date_next_week()
    period = 6

    params = {
        "os": "android",
        "date": date,
        "period": period
        }

    if schedule_type == 'student':
        params["group"] = get_group_number_from_user(user)
    elif schedule_type == 'teacher':
        params["teachid"] = get_teacher_id_from_user(user)
    
    return params

def return_today(user_id):
    user_exists, user = get_user(user_id)

    base_url = make_base_url(user)
    params = make_params_today(user)

    result = return_data(params, base_url, user)
    return result

def return_tomorrow(user_id):

    user_exists, user = get_user(user_id)

    base_url = make_base_url(user)
    params = make_params_tomorrow(user)

    result = return_data(params, base_url, user)
    
    return result

def return_schedule_from_today_until_saturday(user_id):
    user_exists, user = get_user(user_id)

    base_url = make_base_url(user)
    params = make_params_from_today_until_saturday(user)

    result = return_data(params, base_url, user)
    return result

def return_this_week(user_id):
    user_exists, user = get_user(user_id)

    base_url = make_base_url(user)
    params = make_params_this_week(user)

    result = return_data(params, base_url, user)
    return result

def return_next_week(user_id):
    user_exists, user = get_user(user_id)

    base_url = make_base_url(user)
    params = make_params_next_week(user)

    result = return_data(params, base_url, user)
    return result


def return_data(params, base_url, user): 
    r = requests.get(base_url, params=params)
    url = r.url

    try:
        response = requests.get(url)
        response_json = response.json()
        response_dict = dict(response_json)

        # Check if data is a dictionary and contains a 'message' key
        if 'message' in response_dict:
            return response_dict['message']

        data = response_dict['schedule']
    except Exception as e:
        print(f"An error occurred: {e}")

    #result = transform_json_to_ouptut_format(data)

    return data

def get_uid_teacher_from_bsu(teacher_name):
    
    
    base_url = os.environ.get('BASE_URL_AUTO')
    params = {
        "term": teacher_name
        }

    try:
        response = requests.get(base_url, params=params)
        response_json = response.json()
 
        if response_json==None:
            return None

        response_dict = dict(response_json[0])
        teacher_uid = response_dict['data']

    except Exception as e:
        print("An error occurred: {e}".format(e))
        return None

    return teacher_uid