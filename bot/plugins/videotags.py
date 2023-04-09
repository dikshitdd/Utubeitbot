import telegram
from telegram.ext import Updater, CommandHandler
from youtubetags import YouTubeTags

# Define a function to handle the /tags command
def tags(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! Send me a YouTube video URL and I'll fetch its tags.")

# Define a function to handle incoming messages
def handle_message(update, context):
    url = update.message.text
    tags = YouTubeTags.get_tags(url)
    if tags:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Tags: {}".format(", ".join(tags)))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I couldn't fetch the tags. Please check if the URL is correct.")

# Create a Telegram bot object and set up a CommandHandler
bot_token = "YOUR_BOT_TOKEN_HERE"
bot = telegram.Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Set up a message handler
message_handler = telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
