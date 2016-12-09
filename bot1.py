from telegram.ext import Updater, CommandHandler , MessageHandler , Filters


def start(bot, update):
    print("Вызван /start")
    bot.sendMessage(update.message.chat_id, text='Привет,дорогой друг! Я Бот Doleron,чем могу помочь?')

dialog = {"Hi": "Fuck off!","How are you?":"GOVNO","Why?":"Cause life is shit!"}
def talk_to_me(bot, update):
    print("Пришло сообщение "+ update.message.text )
    bot.sendMessage(update.message.chat_id, text= dialog.get(update.message.text) )

def run_bot():
    updater = Updater("304724996:AAF6H9uEkPg4OFwbpj5u_hwQLY5YQ-FpOCI")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(MessageHandler((Filters.text), talk_to_me))
    updater.start_polling()
    updater.idle()

if __name__=='__main__':
    run_bot()
