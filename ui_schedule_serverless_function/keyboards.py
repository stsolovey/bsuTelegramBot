import os
import telebot
from telebot import types

from ydb_data import get_user, set_notify_every_day, set_notify_before_lessons, set_last_seen, increment_user_action_counter
from local_data import get_schedule_type_from_user, get_group_number_from_user, get_teacher_name_from_user
from emoji import random_smileys, random_upside_down, random_negative, random_negative_funny, random_current_week
from emoji import random_positive, random_notification, random_schedule, random_settings, random_teacher

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))


def keyboard_settings(message):
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton(random_schedule() + " Расписание", callback_data="schedule_settings")
    item2 = types.InlineKeyboardButton(random_notification() + " Уведомления", callback_data="notification_settings")
    item3 = types.InlineKeyboardButton("⬅️ назад", callback_data="main_schedule_picker")

    markup.add(item1, item2, item3)

    bot.edit_message_text(chat_id=message.chat.id, 
                          message_id=message.message_id, 
                          text= random_settings() + ' Настройки:', 
                          reply_markup=markup )
                     
def keyboard_notification_settings(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("🔄 Ежедневное", callback_data="everyday_notifications")
    item2 = types.InlineKeyboardButton("📋 Перед занятиями", callback_data="before_lessons_notifications")
    item3 = types.InlineKeyboardButton("⬅️ назад", callback_data="settings")

    markup.add(item1, item2, item3)
    bot.edit_message_text(chat_id=message.chat.id, 
                          message_id=message.message_id, 
                          text= random_settings() + random_notification() + ' Настройки уведомления:', 
                          reply_markup=markup )

def keyboard_schedule_type(message):
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("👯👯👯 Расписание группы", callback_data="student")
    item2 = types.InlineKeyboardButton(random_teacher() + " Расписание преподавателя", callback_data="teacher")

    if message.from_user.is_bot:
        user_id = message.chat.id
        edit_message = True
    else:
        user_id = message.from_user.id
        edit_message = False
    user_exists, user = get_user(user_id)

    if user_exists:
        item3 = types.InlineKeyboardButton("⬅️ назад", callback_data="settings")
        markup.add(item1, item2, item3, )
    else:
        markup.add(item1, item2, )
    
    bot.edit_message_text(chat_id=message.chat.id, 
                          message_id=message.message_id, 
                          text= random_settings() + random_schedule() + ' Укажите тип расписания:', # ⚙️📋 
                          reply_markup=markup )

def show_shedule_picker(message):
    set_last_seen
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("📅 Сегодня", callback_data="today_schedule")
    item2 = types.InlineKeyboardButton("📆 Завтра", callback_data="tomorrow_schedule")
    item3 = types.InlineKeyboardButton(random_schedule() + " До конца недели", callback_data="thisweekfromtoday_schedule") #📋
    item4 = types.InlineKeyboardButton(random_current_week() + " Текущая неделя", callback_data="thisweek_schedule") # 🐳
    item5 = types.InlineKeyboardButton("🔮 Следующая неделя", callback_data="nextweek_schedule")
    item6 = types.InlineKeyboardButton(random_settings() + " Настройки", callback_data="settings")

    markup.add(item1, item2)  # First row, two columns
    markup.add(item3, item4)  # Second row, two columns
    markup.add(item5)         # Third row, one column
    markup.add(item6)         # Fourth row, one column

    if message.from_user.is_bot:
        user_id = message.chat.id
        edit_message = True
    else:
        user_id = message.from_user.id
        edit_message = False


    user_exists, user = get_user(user_id)

    if user_exists:
        set_last_seen(user_id)
        increment_user_action_counter(user_id)
        schedule_type = get_schedule_type_from_user(user)
        if schedule_type=='student':
            group_number = get_group_number_from_user(user)
            title_text = "Расписание группы {} {}".format(group_number, random_smileys())

        if schedule_type=='teacher':
            teacher_name = get_teacher_name_from_user(user)
            title_text = "Расписание преподавателя {} {}".format(random_teacher(), teacher_name)
 
        if edit_message:
            bot.edit_message_text(chat_id=message.chat.id, 
                            message_id=message.message_id, 
                            text=title_text, 
                            reply_markup=markup )
        else:
            bot.send_message(message.chat.id,
                        title_text,
                        reply_markup=markup)

    else:
        bot.send_message(message.chat.id,
                        "Пользователь не существует",
                        parse_mode='markdown')

def keyboard_set_everyday_time_notification(message):

    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("🌅🍳☕ 0️⃣8️⃣:0️⃣0️⃣", callback_data="set_eight_am")
    item2 = types.InlineKeyboardButton("🌃🌕🔭 2️⃣0️⃣:0️⃣0️⃣", callback_data="set_eight_pm")
    item3 = types.InlineKeyboardButton("Выключить " + random_upside_down(), 
                                       callback_data="stop_everyday_notification")
    item4 = types.InlineKeyboardButton("🏃⬅️ назад", callback_data="notification_settings")
    markup.add(item1, item2, item3, item4, )
    
    bot.edit_message_text(chat_id=message.chat.id, 
                          message_id=message.message_id, 
                          text='''🔔Ежедневно (Mск):''', 
                          reply_markup=markup )

def keyboard_set_everyday_notification(message, time):

    set_notify_every_day(message.chat.id, time)
    if time == "08:00":
        replay_message = """Установлено ежедневное\nуведомление в 0️⃣8️⃣:0️⃣0️⃣ 😏"""
    elif time == "20:00":
        replay_message = """Установлено ежедневное\nуведомление в 2️⃣0️⃣:0️⃣0️⃣ 🙂"""
    else:
        replay_message = """Ежедневное уведомление выключено 🛑😉"""

    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("⬅️ назад", callback_data="everyday_notifications")
    item2 = types.InlineKeyboardButton("⬅️⬅️ в начало ⬅️⬅️", callback_data="main_schedule_picker")
    markup.add(item1, item2)
    
    bot.edit_message_text(chat_id=message.chat.id, 
                          message_id=message.message_id, 
                          text=replay_message, 
                          reply_markup=markup )

def keyboard_set_before_lesson_notification(message):
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton(random_positive() + " Включить  ", callback_data="turn_on_before_lesson_notification")
    item2 = types.InlineKeyboardButton(random_negative_funny() + " Выключить", callback_data="turn_off_before_lesson_notification")
    item3 = types.InlineKeyboardButton("⬅️ назад", callback_data="notification_settings")
    markup.add(item1, item2, item3,)
    
    bot.edit_message_text(chat_id=message.chat.id, 
                          message_id=message.message_id, 
                          text=random_notification() + ' Перед занятиями:', 
                          reply_markup=markup )

def keyboard_switch_before_lesson_notification(message, bool_flag):
    set_notify_before_lessons(message.chat.id, bool_flag)

    if bool_flag:
        replay_message = """Включено! 😊"""
    else:
        replay_message = """Выключено! 😜"""

    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("🏃🏻‍♂️⬅️ назад", callback_data="before_lessons_notifications")
    item2 = types.InlineKeyboardButton("⬅️⬅️ в начало ⬅️⬅️", callback_data="main_schedule_picker")
    markup.add(item1, item2)
    
    bot.edit_message_text(chat_id=message.chat.id, 
                          message_id=message.message_id, 
                          text=replay_message, 
                          reply_markup=markup )


def keyboard_schedule_window(message, schedule, title):
    title_schedule = title +" "+ random_smileys() +"\n"+ schedule

    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("⬅️ назад", callback_data="main_schedule_picker")
    markup.add(item1)
    
    bot.edit_message_text(chat_id=message.chat.id, 
                          message_id=message.message_id, 
                          text=title_schedule, 
                          reply_markup=markup,
                          parse_mode='markdown' )

def keyboard_ask_for_input(message, schedule_type):
    if schedule_type == 'student':
        text = "Введите номер группы, 8 цифр:"
        #save message id, save state
    if schedule_type == 'teacher':
        text = "Введите Фамилию Имя Отчество преподавателя полностью:"
        #save message id, save state

    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("⬅️ назад", callback_data="schedule_settings")
    markup.add(item1)

    bot.edit_message_text(chat_id=message.chat.id, 
                          message_id=message.message_id, 
                          text=text, 
                          reply_markup=markup,
                          parse_mode='markdown' )