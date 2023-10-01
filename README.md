# 🤖 bsuTimetableClassesBot - A Telegram Schedule Bot

Welcome to [🤖 bsuTimetableClassesBot](https://t.me/bsuTimetableClassesBot) - a handy Telegram bot designed for the students of Belgorod State University. Get your class schedule directly on Telegram!

<p align="center">
  <a href="https://t.me/bsuTimetableClassesBot"><img src="https://img.shields.io/badge/Telegram-bot-blue.svg"></a>
  <a href="https://cloud.yandex.ru/"><img src="https://img.shields.io/badge/Yandex.Cloud-functions-9cf?style=flat-square&logo=data:image/png;base64,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"></a>
</p>

## 📖 Features

- 🛫 Start working with command `/start`.
- 🗿 You will come here if you call `/about`.
- 🆘 Ask for help if you get lost `/help`

## 📝 Sample Output

![Main Menu](images/main_menu.png)
![Sample Output](images/sample_ouptut.png)

## 🛠 Configuration


1. env variables (bot token etc.)
2. Triggers for notifications function.

| Description  | cron triggers  |
|---|---|
| Два раза в день в 8 и в 20  | 0 5,17 ? 9-5 * *  |
| 3-4 пара. За 15 минут перед парами. utc=0 12:00 14:00  | 45 8,10 ? 9-5 2-7 *  |
| 2-7 пары. За 15 минут перед парами. utc=0 10:15 19:15  | 0 7,16 ? 9-5 2-7 *  |
| 5 пара. За 15 минут перед парами. utc=0 15:45  | 30 12 ? 9-5 2-7 *	  |
| 1-6 пара. За 15 минут перед парами. utc=0 8:30 17:30  | 15 5,14 ? 9-5 2-7 *  |



## 🚀 Getting Started

How to Use:

1. Create a Yandex Serverless Functions with the provided code.
2. Set up a Telegram Bot.
3. Connect the Yandex functions and the Telegram bot.
4. Create the Yandex Database and connect it to functions.
5. Set triggers for notifications function.
6. Delight in the convenience!

![Yandex Services](images/yc_services.png)

Also you can go to [🤖 BotFather](https://t.me/BotFather) and:

1. Call `/setcommands`
2. Choose your telegram bot
3. Set `menu` button:

```
start - Get started
about - About the project
help - Get help
```
4. Well done!

## 💸 Сost-price

The first million operations per month for Functions and Databases in Yandex Cloud are free. Then you will have to pay a few rubles, so be careful.

## ✍️ Author

This bot was crafted with ❤️ by a proud student.

📜 License

BSU © 2023 [👨‍⚕️ Duck Ever](https://t.me/duckever)


<p align="center">
  <img src="images/pxl_pgss.jpg" alt="Belgorod State Univercity"/>
</p>