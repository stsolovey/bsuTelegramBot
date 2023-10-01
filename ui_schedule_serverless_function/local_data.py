import datetime

def get_schedule_type_from_user(user_data):
    if 'schedule_type' in user_data:
        if user_data['schedule_type'] in ['student', 'teacher']:
            return True, user_data['schedule_type']
        else:
            return False, "Invalid value for schedule_type"
    else:
        return False, "schedule_type not set"

def check_schedule_type_is_set(user_data):
    if 'schedule_type' in user_data:
        if user_data['schedule_type'] in ['student', 'teacher']:
            return True
        else:
            return False
    else:
        return False

def validate_schedule(user_data):
    if user_data['schedule_type'] == 'student':
    # if schedule type student show related schedule picker
        if 'group_number' in user_data and user_data['group_number']:
            return True
        else:
            return False
    elif  user_data['schedule_type'] == 'teacher':
        # if schedule type teacher show related schedule picker
        if 'teacher_name' in user_data and user_data['teacher_name']:
            return True
        else:
            return False

def format_teacher_name(input_str):
    words = input_str.split()  # This will automatically remove extra spaces
    capitalized_words = [word.capitalize() for word in words]
    formatted_str = " ".join(capitalized_words)
    return formatted_str

def get_schedule_type_from_user(user):
    if user:
        return user.get('schedule_type', None)
    else:
        return None

def get_group_number_from_user(user):
    if user:
        return user.get('group_number', None)
    else:
        return None

def get_teacher_name_from_user(user):
    if user:
        return user.get('teacher_name', None)
    else:
        return None

def get_teacher_id_from_user(user):
    if user:
        return user.get('teacher_uid', None)
    else:
        return None

def get_date_today():
    return datetime.datetime.today().strftime('%d.%m.%Y')

def get_date_tomorrow():
    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
    return tomorrow.strftime('%d.%m.%Y')

def return_period_from_today_until_saturday():

    now = datetime.datetime.now()
    today_weekday = now.weekday()

    # If today is Sunday, return next week
    if today_weekday == 6:
        return return_next_week()
    
    # Calculate the days until Saturday
    days_until_saturday = 5 - today_weekday

    return str(days_until_saturday)

def get_date_this_week():
    now = datetime.datetime.now()
    monday = now - datetime.timedelta(days = now.weekday())
    return monday.strftime('%d.%m.%Y')

def get_date_next_week():
    now = datetime.datetime.now()
    thismonday = now - datetime.timedelta(days = now.weekday())
    nextmonday = thismonday + datetime.timedelta(days = 7)
    return nextmonday.strftime('%d.%m.%Y')

def time_based_on_call_data(call_data):
            if call_data == "set_eight_am":
                return "08:00"
            elif call_data == "set_eight_pm":
                return "20:00"
            else:
                return None

def turn_on_off_bool_flag_based_on_call_data(call_data):
            if call_data == "turn_on_before_lesson_notification":
                return True
            elif call_data == "turn_off_before_lesson_notification":
                return False
            else:
                return None