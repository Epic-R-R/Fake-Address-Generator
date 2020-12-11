import logging
import requests

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Hi!")


def fake(update, context):
    """Send a Fake Address /fake is issued."""
    url = f"https://randomuser.me/api/"
    response = requests.get(url).json()
    gender = response["results"][0]["gender"]
    name = response["results"][0]["name"]
    location = response["results"][0]["location"]
    birthday = response["results"][0]["dob"]
    if gender == "male":
        message = f"""
        Name 🙋‍♂️ : {name["title"]}.{name["first"]} {name["last"]}

        Address 👇
        Street 🛣 : {location["number"]} {location["name"]}
        City 🌆 : {response["results"][0]["city"]}
        State 🚏 : {response["results"][0]["state"]}
        Country 🏜: {response["results"][0]["country"]}
        Post Code 📮 : {response["results"][0]["postcode"]}

        Contact 👇
        Email 📧 : {response["results"][0]["email"]}
        Phone 📱 : {response["results"][0]["phone"]}

        Age 👇
        Birthday 🎂 : {birthday["date"]}
        """

    elif gender == "female":
        message = f"""
        Name 🙋‍♀️ : {name["title"]}.{name["first"]} {name["last"]}

        Address 👇
        Street 🛣 : {location["number"]} {location["name"]}
        City 🌆 : {response["results"][0]["city"]}
        State 🚏 : {response["results"][0]["state"]}
        Country 🏜: {response["results"][0]["country"]}
        Post Code 📮 : {response["results"][0]["postcode"]}

        Contact 👇
        Email 📧 : {response["results"][0]["email"]}
        Phone 📱 : {response["results"][0]["phone"]}

        Age 👇
        Birthday 🎂 : {birthday["date"]}
        """
    print(message)
    update.message.reply_text("chi")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(
        "1463819644:AAEJ7cZLqHr5wrEROJL_lWDxzklQsBTZ6nc", use_context=True
    )

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("fake", fake))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()