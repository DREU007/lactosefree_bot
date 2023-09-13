import os
import logging
from telegram import (
    Update,
    InlineQueryResultArticle,
    InputTextMessageContent,
)

from telegram.ext import (
    filters,
    MessageHandler,
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    InlineQueryHandler,
)

from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


help_msg = (
    "Welcome to Lactose Free Bot, Armenia!\n"
    "I'm in early development stage,\n"
    "So please be patient and see you soon!\n"
    "\n"
    "/HELP - to see this help message\n"
    "/POST - send me data\n"
    "/INFO - retrive all available info\n"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=help_msg            
    )


async def help_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=help_msg
    ) 


# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(
#         chat_id=update.effective_chat.id,
#         text=update.message.text
#     )


# async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     text_caps = " ".join(context.args).upper()
#     await context.bot.send_message(
#         chat_id=update.effective_chat.id,
#         text = text_caps
#     )


# async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.inline_query.query
#     if not query:
#         return
#     results = []
#     results.append(
#         InlineQueryResultArticle(
#             id=query.upper(),
#             title='Caps',
#             input_message_content=InputTextMessageContent(query.upper())
#         )
#     )
#     await context.bot.answer_inline_query(update.inline_query.id, results)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Sorry, I didn't understand that command."
    )


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help_info)
#    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
#    caps_handler = CommandHandler('caps', caps)
#    inline_caps_handler = InlineQueryHandler(inline_caps)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
#    application.add_handler(echo_handler)
#    application.add_handler(caps_handler)
#    application.add_handler(inline_caps_handler) 
    application.add_handler(unknown_handler)
    application.run_polling()
