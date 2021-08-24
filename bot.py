import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from tracker import get_prices

telegram_bot_token = "1961253995:AAHxV1L8VKhRMB-ED99u2BccA8BohBaqEH0"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


def Price(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        change_day = crypto_data[i]["change_day"]
        change_hour = crypto_data[i]["change_hour"]
        message += f"Coin: {coin}\nGiá: ${price:,.2f}\nThay đổi trong giờ: {change_hour:.3f}%\nThay Đổi Trong Ngày: {change_day:.3f}%\n\n"

    context.bot.send_message(chat_id=chat_id, text=message)


dispatcher.add_handler(CommandHandler("Price", Price))
updater.start_polling()
