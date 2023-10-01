from notifier import notification_every_day_schedule, notification_before_lessons_schedule
from ydb_data import return_notifier_list

def handler(event, _):
    
    notify_every_day_dict, notify_before_lessons_dict =  return_notifier_list()
 
    notification_every_day_schedule(notify_every_day_dict)
    
    notification_before_lessons_schedule(notify_before_lessons_dict)

    return {
        'statusCode': 200,
        'body': '!',
    }