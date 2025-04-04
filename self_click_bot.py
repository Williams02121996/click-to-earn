<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Telegram Mini App</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        button { padding: 10px 20px; font-size: 18px; }
    </style>
</head>
<body>
    <h1>Welcome to My Mini App</h1>
    <button onclick="sendMessage()">Send Message</button>
    
    <script>
        let tg = window.Telegram.WebApp;
        tg.expand(); // Expand to full screen
        
        function sendMessage() {
            tg.sendData("Hello from Mini App!"); // Sends data to bot
        }
    </script>
</body>
</html>
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Define the start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! This is your self-click bot.')

# Define a command to simulate a click
def click(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Button clicked!')

def main() -> None:
    # Replace 'YOUR_TOKEN' with your bot's token
    updater = Updater("7807350841:AAGOk5Za6Emwe9F1J94KlK_F6J0pcH-gei4")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the start handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Register the click handler
    dispatcher.add_handler(CommandHandler("click", click))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
