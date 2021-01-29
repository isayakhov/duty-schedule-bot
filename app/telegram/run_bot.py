if __name__ == "__main__":
    from telegram.ext import CommandHandler, Updater
    from app.config import TELEGRAM_TOKEN
    from . import handlers

    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("help", handlers.start))
    dispatcher.add_handler(CommandHandler("start", handlers.start))
    dispatcher.add_handler(CommandHandler("week", handlers.show_schedule, pass_chat_data=True))
    dispatcher.add_handler(CommandHandler("create", handlers.create_schedule, pass_chat_data=True))
    dispatcher.add_handler(CommandHandler("add", handlers.add_person, pass_args=True, pass_chat_data=True))
    dispatcher.add_handler(CommandHandler("remove", handlers.remove_person, pass_args=True, pass_chat_data=True))
    dispatcher.add_error_handler(handlers.error)

    updater.start_polling()
    updater.idle()
