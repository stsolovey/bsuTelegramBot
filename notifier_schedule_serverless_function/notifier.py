import os
import telebot
from telebot import types

from local_data import find_classes_for_notification
from local_data import approve_every_day_notification, it_is_night_or_sunday
from bsu_data import return_today, return_tomorrow
from view import transform_json_to_ouptut_format
from ydb_data import get_all_items, check_criteria

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))

def keyboard_schedule_window(chat_id, schedule, title, callback_data):
    title_schedule = title + schedule

    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("⚙️ настройки уведомлений", callback_data=callback_data)
    markup.add(item1)
    
    bot.send_message(chat_id=chat_id,  
                    text=title_schedule, 
                    reply_markup=markup,
                    parse_mode='markdown' )

def notification_before_lessons_schedule(notify_before_lessons_dict):
    if it_is_night_or_sunday():
        print("It is night or synday.")
        return None
        
    if notify_before_lessons_dict:            
        for user in notify_before_lessons_dict:
            user_id = user['user_id']
            chat_id = user['chat_id']

            todays_schedule = return_today(user_id)
            classes_for_notification = find_classes_for_notification(todays_schedule)
            title = '🔔 '
            callback_data = 'before_lessons_notifications'

            if classes_for_notification:

                transformed_schedule = transform_json_to_ouptut_format(classes_for_notification)

                try:
                    keyboard_schedule_window(chat_id, transformed_schedule, title, callback_data)
                    #bot.send_message(chat_id, transformed_todays_schedule, parse_mode='markdown')
                except Exception as e:
                    print(e)

def notification_every_day_schedule(notify_every_day_dict):
    if notify_every_day_dict:    
        for user in notify_every_day_dict:

            user_id = user['user_id']
            chat_id = user['chat_id']
            user_time = user["notify_every_day"]
            
            it_is_time_to_notify = approve_every_day_notification(user_time)
            
            if it_is_time_to_notify:

                if user_time=="08:00":
                    title = '🔔 Cегодня: '
                    schedule = return_today(user_id)  
                else:
                    title = '🔔 Завтра: '
                    schedule = return_tomorrow(user_id)
                callback_data = 'everyday_notifications'
                transformed_schedule = transform_json_to_ouptut_format(schedule)
                
                try:
                    keyboard_schedule_window(chat_id, transformed_schedule, title)
                    #bot.send_message(chat_id, transformed_schedule, parse_mode='markdown')
                except Exception as e:
                    print(e)