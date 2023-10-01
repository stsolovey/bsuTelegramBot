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


def get_current_time():
    time_zone = datetime.timezone(datetime.timedelta(hours=3))
    return datetime.datetime.now(tz=time_zone)


def find_classes_for_notification(schedule):
    upcoming_classes = []
    
    time_zone = datetime.timezone(datetime.timedelta(hours=3))
    current_time = datetime.datetime.now(tz=time_zone)
    
    #current_time = datetime.datetime(2023, 9, 28, 18, 15, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=10800)))
    
    for class_info in schedule:
        # Convert the date and timestart into a datetime object
        class_start_str = f"{class_info['date']} {class_info['timestart']}"
        class_start_time = datetime.datetime.strptime(class_start_str, '%d.%m.%Y %H:%M').replace(tzinfo=time_zone)
        
        # Calculate the time difference
        time_difference = class_start_time - current_time
        print("time_difference", time_difference)
        # Check if the class starts in the next 20 minutes
        if datetime.timedelta(minutes=0) <= time_difference <= datetime.timedelta(minutes=20):
            upcoming_classes.append(class_info)
            
    return upcoming_classes if upcoming_classes else None


def approve_every_day_notification(user_time):
    #TODO: rewrite using timedelta\
    time_zone = datetime.timezone(datetime.timedelta(hours=3))
    now_hours = datetime.datetime.now(tz=time_zone).hour

    now_minute = datetime.datetime.now().minute
    user_hour, user_minute = user_time.split(":")
    user_hour = int(user_hour)
    user_minute = int(user_minute)
    result = (now_hours == user_hour) and (now_minute < 15)

    return result

def it_is_night_or_sunday():
    # Get the current time and day of the week
    time_zone = datetime.timezone(datetime.timedelta(hours=3))
    now = datetime.datetime.now(tz=time_zone)
    current_time = now.time()
    
    # Define the time boundaries
    morning_time_boundary = datetime.datetime.strptime("08:15", "%H:%M").time()
    evening_time_boundary = datetime.datetime.strptime("19:30", "%H:%M").time()

    night = current_time < morning_time_boundary or current_time > evening_time_boundary
    sunday = now.weekday()==7  # Monday is 1, Sunday is 7

    # Check if it is Sunday or if the time is outside the defined boundaries
    if night or sunday:
        return True
    else:
        return False

