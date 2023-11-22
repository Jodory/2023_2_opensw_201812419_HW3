import telegram
from telegram import Update
import asyncio
import platform
from telegram.ext import Application
from telegram.ext import MessageHandler
from telegram.ext import filters
from telegram.ext import ContextTypes
from telebot_config import bot_token, chat_id

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

if __name__ == '__main__':
    # 비동기 관련 설정(윈도우 전용)
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # app 빌드
    application = Application.builder().token(bot_token).build()

    # 핸들러 설정
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # polling 시작
    application.run_polling(allowed_updates=Update.ALL_TYPES)