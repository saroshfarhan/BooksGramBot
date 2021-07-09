from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, ForceReply
import logging
from jokesApi import joke
import bookRecommender
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'G:/SeleniumTest/PythonTests/TelegramBot')

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def recommend(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /recommend is issued."""
    results = bookRecommender.get_Name()
    photo = results[0]
    title = results[1]
    author = results[2]
    description = results[3]
    amzn_url = results[4]

    caption = title + "\n by " + author + "\n" + description + "\n" + amzn_url
    print(caption)
    update.message.reply_photo(photo=photo, caption=caption)


def jokes(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /joke is issued."""
    punchline = joke()  # getting te joke via jokesApi.py
    update.message.reply_text(punchline)


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("YOUR_BOT'S_ACCESS_TOKEN")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    #dispatcher.add_handler(CommandHandler("get", get))
    dispatcher.add_handler(CommandHandler("recommend", recommend))
    dispatcher.add_handler(CommandHandler("joke", jokes))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
