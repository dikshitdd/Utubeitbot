import telegram
import logging
import urllib.request
from youtubetags import fetch_video_tags
from utubeitbo import get_video_url
from .config import Config



# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Create a Telegram bot object
bot = telegram.Bot(token=Config.BOT_TOKEN)

# Define a function to handle incoming messages
def handle_message(update, context):
    # Get the message text
    message_text = update.message.text
    
    # Check if the message contains a valid YouTube URL
    if 'youtube.com' in message_text or 'youtu.be' in message_text:
        # Get the video URL
        video_url = get_video_url(message_text)
        
        # Fetch the video tags
        video_tags = fetch_video_tags(video_url)
        
        # Send the tags back to the user
        update.message.reply_text('Tags for {}: {}'.format(video_url, ', '.join(video_tags)))
    else:
        # Send a message to the user asking for a YouTube URL
        update.message.reply_text('Please provide a valid YouTube URL.')

# Start the bot
def main():
    updater = telegram.ext.Updater(token=Config.BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

if name == 'main':
    main()
