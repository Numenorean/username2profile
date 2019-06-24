import telebot, steam_api

bot = telebot.TeleBot('868324459:AAFcSPGqvc22kA1QbQD5sO3fmESPTb0Zk4M')


@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    bot.send_message(cid, "Send me steam username")


@bot.message_handler(content_types=['text'])
def send_profile(m):
    try:
        url = steam_api.main(m.text)
    except AttributeError:
        url = 'Sorry, but this profile does not exist'
    bot.reply_to(m, url)

bot.polling(none_stop=False)
