import os
import telebot

from telebot import types

from bsu_data import return_today, return_tomorrow, return_this_week, return_next_week
from bsu_data import return_schedule_from_today_until_saturday, get_uid_teacher_from_bsu
from keyboards import keyboard_settings, keyboard_notification_settings, keyboard_schedule_type, show_shedule_picker
from keyboards import keyboard_set_everyday_time_notification, keyboard_set_everyday_notification
from keyboards import keyboard_set_before_lesson_notification, keyboard_switch_before_lesson_notification
from keyboards import keyboard_schedule_window, keyboard_ask_for_input


bot = telebot.TeleBot(os.environ.get('BOT_TOKEN')) 


from ydb_data import get_user, create_user, set_schedule_type, set_group_number, set_teacher_name, set_teacher_uid
from ydb_data import chat_id_check_set

from local_data import check_schedule_type_is_set, validate_schedule, format_teacher_name
from local_data import time_based_on_call_data, turn_on_off_bool_flag_based_on_call_data

def start(message):
    print("start message:", message)
    
    user_exists, user = get_user(message.from_user.id)

    if user_exists:

        chat_id_check_set(message)

        if check_schedule_type_is_set(user):

            if validate_schedule(user):

                show_shedule_picker(message)
            else:
  
                keyboard_ask_for_input(message.chat.id, user['schedule_type'])
                
        else:
 
            keyboard_schedule_type(message)
    else:
        print('going to add user {}'.format(message.from_user.first_name))
        create_user(message)
        keyboard_schedule_type(message)

# --------------------- bot ---------------------


@bot.message_handler(commands=['start'])
def return_schedule(message):
    bot.send_message(message.chat.id,
                     start(message),
                     parse_mode='markdown')

@bot.message_handler(commands=['type'])
def return_schedule(message):
    bot.send_message(message.chat.id,
                     keyboard_schedule_type(message),
                     parse_mode='markdown')

@bot.message_handler(commands=['about'])
def return_schedule(message):
    bot.send_message(message.chat.id,
                     "Лабораторная работа по облачным 🌩️ данным",
                     parse_mode='markdown')

@bot.message_handler(commands=['help'])
def return_schedule(message):
    bot.send_message(message.chat.id,
                     """Для начала работы или вызова главного меню используйте команду /start

Укажите тип расписания.

Студенты выбирают "расписание группы". 
Преподаватели — "расписание преподавателя".

Управляйте этим в меню "⚙️ Настройки".

"🔔 уведомления"
Вы можете выбрать ежедневные уведомления: утром или вечером в 8-00 и 20-00. 
А так же можно включить уведомления перед началом занятий, за 15 минут. 

Уведомления можно выключить

Успехов! 😊
                     """,
                     parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "today_schedule":
        today_schedule = return_today(call.from_user.id)
        title = "Сегодня: "
        keyboard_schedule_window(call.message, today_schedule, title)
        
    elif call.data == "tomorrow_schedule":
        tomorrow_schedule = return_tomorrow(call.from_user.id)
        title = "Завтра: "
        keyboard_schedule_window(call.message, tomorrow_schedule, title)
        
    elif call.data == "thisweekfromtoday_schedule":
        thisweekfromtoday_schedule = return_schedule_from_today_until_saturday(call.from_user.id)
        title = "До конца недели: "
        keyboard_schedule_window(call.message, thisweekfromtoday_schedule, title)
        
    elif call.data == "thisweek_schedule":
        thisweek_schedule = return_this_week(call.from_user.id)
        title = "Эта неделя: "
        keyboard_schedule_window(call.message, thisweek_schedule, title)
        
    elif call.data == "nextweek_schedule":
        nextweek_schedule = return_next_week(call.from_user.id)
        title = "Следующая неделя: "
        keyboard_schedule_window(call.message, nextweek_schedule, title)
        
    elif call.data == "student" or call.data == "teacher":
        schedule_type = call.data
        set_schedule_type(call.from_user.id, schedule_type)
        keyboard_ask_for_input(call.message, schedule_type)
 
    elif call.data == "settings":
        keyboard_settings(call.message)
        
    elif call.data == "schedule_settings":
        keyboard_schedule_type(call.message)
        
    elif call.data == "notification_settings":
        keyboard_notification_settings(call.message)
        
    elif call.data == "everyday_notifications":
        keyboard_set_everyday_time_notification(call.message)
        
    elif call.data == "before_lessons_notifications":
        keyboard_set_before_lesson_notification(call.message)
        

    elif call.data == "main_schedule_picker":
        show_shedule_picker(call.message)
        

    elif call.data == "set_eight_am" or call.data == "set_eight_pm" or call.data == "stop_everyday_notification": 
        
        time = time_based_on_call_data(call.data)
        keyboard_set_everyday_notification(call.message, time)
        
        
    elif call.data == "turn_on_before_lesson_notification" or call.data == "turn_off_before_lesson_notification": 
        bool_flag = turn_on_off_bool_flag_based_on_call_data(call.data)
        keyboard_switch_before_lesson_notification(call.message, bool_flag)
        

# Handles all text messages that match the regular expression
@bot.message_handler(regexp="\d{8}")
def handle_message(message):
    set_group_number(message.from_user.id, message.text)
    text = 'Группа {} добавлена'.format(message.text)
    bot.send_message(message.chat.id, text, parse_mode='markdown')  
    show_shedule_picker(message) 

@bot.message_handler(regexp="[А-ЯЁа-яё]+(?:-[А-ЯЁа-яё]+)? [А-ЯЁа-яё]+(?: [А-ЯЁа-яё]+)*")
def handle_message(message):
    teacher_name = format_teacher_name(message.text)
    teacher_uid = get_uid_teacher_from_bsu(teacher_name)

    if teacher_uid:
        set_teacher_name(message.from_user.id, teacher_name)
        
        set_teacher_uid(message.from_user.id, teacher_uid)
        
        text = 'Преподаватель {} (uid:{}) добавлен'.format(teacher_name, teacher_uid)
        bot.send_message(message.chat.id, text, parse_mode='markdown')
        show_shedule_picker(message)
    else:
        text = 'Преподаватель {} не найден'.format(message.text)
        bot.send_message(message.chat.id, text, parse_mode='markdown')


@bot.message_handler(content_types=["text"])
def text_processing(message):
    bot.send_message(message.chat.id, message.text)
# ---------------- main ----------------
#if __name__ == '__main__':
#    bot.infinity_polling()

#bot.infinity_polling()