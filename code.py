import telebot

bot = telebot.TeleBot('8790345810:AAHVGu4IzAOFyIvIhmxbOV0o8H3v3TCXJtk')

users = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, добавьте всех пользователей, что бы потом можно было сразу всех отмечать')

@bot.message_handler(commands=['add'])
def add_user(message):
    chat_id = message.chat.id

    if chat_id not in users:
        users[chat_id] = {}

    user_id = message.from_user.id
    username = message.from_user.first_name

    users[chat_id][user_id] = username

    bot.reply_to(message, f"{username} добавлен!")

@bot.message_handler(commands=['all'])
def mention_all(message):
    chat_id = message.chat.id

    if chat_id not in users or len(users[chat_id]) == 0:
        bot.send_message(chat_id, "Нет добавленных участников")
        return

    text = "May I have your attention please?\n\n"

    for user_id, username in users[chat_id].items():
        text += f"[{username}](tg://user?id={user_id}) "

    bot.send_message(chat_id, text, parse_mode='Markdown')

bot.polling(none_stop=True)
