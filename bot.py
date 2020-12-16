# import logging
import requests

# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# # Enable logging
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
# )

# logger = logging.getLogger(__name__)


# def start(update, context):
#     """Send a message when the command /start is issued."""
#     update.message.reply_text("Hi!")


# def fake(update, context):
#     """Send a Fake Address /fake is issued."""
#     url = f"https://randomuser.me/api/"
#     response = requests.get(url).json()
#     gender = response["results"][0]["gender"]
#     name = response["results"][0]["name"]
#     location = response["results"][0]["location"]
#     birthday = response["results"][0]["dob"]
#     if gender == "male":
#         message = f"""
#         Name 🙋‍♂️ : {name['title']}.{name['first']} {name['last']}

#         Address 👇
#         Street 🛣 : {location['number']} {location['name']}
#         City 🌆 : {response['results'][0]['city']}
#         State 🚏 : {response['results'][0]['state']}
#         Country 🏜: {response['results'][0]['country']}
#         Post Code 📮 : {response['results'][0]['postcode']}

#         Contact 👇
#         Email 📧 : {response['results'][0]['email']}
#         Phone 📱 : {response['results'][0]['phone']}

#         Age 👇
#         Birthday 🎂 : {birthday['date']}
#         """

#     elif gender == "female":

#         message = f"""
#         Name 🙋‍♀️ : {name['title']}.{name['first']} {name['last']}

#         Address 👇
#         Street 🛣 : {location['number']} {location['name']}
#         City 🌆 : {response['results'][0]['city']}
#         State 🚏 : {response['results'][0]['state']}
#         Country 🏜: {response['results'][0]['country']}
#         Post Code 📮 : {response['results'][0]['postcode']}

#         Contact 👇
#         Email 📧 : {response['results'][0]['email']}
#         Phone 📱 : {response['results'][0]['phone']}

#         Age 👇
#         Birthday 🎂 : {birthday['date']}
#         """
#     address = f"""
#         Address 👇
#         Street 🛣 : {location['number']} {location['name']}
#     """
#     update.message.reply_text(f"Street 🛣 : {location['number']} {location['name']}")


# def error(update, context):
#     """Log Errors caused by Updates."""
#     logger.warning('Update "%s" caused error "%s"', update, context.error)


# def main():
#     """Start the bot."""
#     # Create the Updater and pass it your bot's token.
#     # Make sure to set use_context=True to use the new context based callbacks
#     # Post version 12 this will no longer be necessary
#     updater = Updater(
#         "1463819644:AAEJ7cZLqHr5wrEROJL_lWDxzklQsBTZ6nc", use_context=True
#     )

#     # Get the dispatcher to register handlers
#     dp = updater.dispatcher

#     # on different commands - answer in Telegram
#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(CommandHandler("fake", fake))

#     # log all errors
#     dp.add_error_handler(error)

#     # Start the Bot
#     updater.start_polling()

#     # Run the bot until you press Ctrl-C or the process receives SIGINT,
#     # SIGTERM or SIGABRT. This should be used most of the time, since
#     # start_polling() is non-blocking and will stop the bot gracefully.
#     updater.idle()


# if __name__ == "__main__":
#     main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
from typing import Dict

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

reply_keyboard = [
    ["Fake Address Generator", "Github Repo"],
    ["About", "Support"],
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def facts_to_str(user_data: Dict[str, str]) -> str:
    facts = list()

    for key, value in user_data.items():
        facts.append(f"{key} - {value}")

    return "\n".join(facts).join(["\n", "\n"])


def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Hi! My name is Doctor Botter. I will hold a more complex conversation with you. "
        "Why don't you tell me something about yourself?",
        reply_markup=markup,
    )

    return CHOOSING


def regular_choice(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    context.user_data["choice"] = text
    update.message.reply_text(
        f"Your {text.lower()}? Yes, I would love to hear about that!"
    )


def fakeaddress(update: Update, context: CallbackContext) -> int:
    """Send a Fake Address /fake is issued."""
    url = f"https://randomuser.me/api/"
    response = requests.get(url).json()
    gender = response["results"][0]["gender"]
    name = response["results"][0]["name"]
    location = response["results"][0]["location"]
    birthday = response["results"][0]["dob"]
    if gender == "male":
        message = f"""
        Name 🙋‍♂️ : {name['title']}.{name['first']} {name['last']}

        Address 👇
        Street 🛣 : {location['street']['number']} {location['street']['name']}
        City 🌆 : {location['city']}
        State 🚏 : {location['state']}
        Country 🏜: {location['country']}
        Post Code 📮 : {location['postcode']}

        Contact 👇  
        Email 📧 : {response['results'][0]['email']}
        Phone 📱 : {response['results'][0]['phone']}

        Age 👇
        Birthday 🎂 : {birthday['date']}
        """

    elif gender == "female":

        message = f"""
        Name 🙋‍♀️ : {name['title']}.{name['first']} {name['last']}

        Address 👇
        Street 🛣 : {location['street']['number']} {location['street']['name']}
        City 🌆 : {location['city']}
        State 🚏 : {location['state']}
        Country 🏜: {location['country']}
        Post Code 📮 : {location['postcode']}

        Contact 👇
        Email 📧 : {response['results'][0]['email']}
        Phone 📱 : {response['results'][0]['phone']}

        Age 👇
        Birthday 🎂 : {birthday['date']}
        """
    update.message.reply_text(message)


def received_information(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    text = update.message.text
    category = user_data["choice"]
    user_data[category] = text
    del user_data["choice"]

    update.message.reply_text(
        "Neat! Just so you know, this is what you already told me:"
        f"{facts_to_str(user_data)} You can tell me more, or change your opinion"
        " on something.",
        reply_markup=markup,
    )


def githubpage(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "You can support me on Github,\nhttps://github.com/Epic-R-R"
    )


def githubrepo(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "You can support me on Github,\nhttps://github.com/Epic-R-R"
    )


def main() -> None:
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(
        "1463819644:AAEJ7cZLqHr5wrEROJL_lWDxzklQsBTZ6nc", use_context=True
    )

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSING: [
                MessageHandler(
                    Filters.regex("^Fake Address Generator$"),
                    fakeaddress,
                ),
                MessageHandler(Filters.regex("^Support$"), githubpage),
                MessageHandler(Filters.regex("^Github Repo"), githubrepo),
                MessageHandler(Filters.regex("^About"), About),
            ],
        },
        fallbacks=[MessageHandler(Filters.regex("^Done$"), fakeaddress)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()