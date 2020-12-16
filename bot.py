#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from typing import Dict

import requests
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    ConversationHandler,
    Filters,
    MessageHandler,
    Updater,
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


def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Hi! My name is Doctor Botter. I will hold a more complex conversation with you. "
        "Why don't you tell me something about yourself?",
        reply_markup=markup,
    )

    return CHOOSING


def fakeaddress(update: Update, context: CallbackContext) -> int:
    """Send a Fake Address /fake is issued."""
    url = f"https://randomuser.me/api/"
    response = requests.get(url).json()
    gender = response["results"][0]["gender"]
    name = response["results"][0]["name"]
    location = response["results"][0]["location"]
    birthday = response["results"][0]["dob"]
    if gender == "male":
        try:
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
        except:
            pass

    elif gender == "female":
        try:
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
        except:
            pass
    update.message.reply_text(message)


def githubpage(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "You can support me on Github,\nhttps://github.com/Epic-R-R"
    )


def githubrepo(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "This is repositorie for fake address generator,\nhttps://github.com/Epic-R-R/Fake-Address-Generator"
    )


def About(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Hi there 👋🏻\nWorking hard and fix bug and build tools and software - Epic-R-R"
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
        fallbacks=[],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
