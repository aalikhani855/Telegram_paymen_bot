import requests
from telegram import Update, WebAppInfo
from telegram.ext import CommandHandler,CallbackContext,Application
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def start(update: Update, context: CallbackContext):
    params = {
        'merchant': 'oxapay',
        'amount': 22.22,
        'callbackUrl': "http://yourcallback:3333",
        'description': "Hello World!",
        'orderId': "ORD-1122",
        'email': "myemail@gmail.com",
    }
    url = "https://api.oxapay.com/merchants/request"
    response = requests.post(url=url, json=params)
    res = response.json()
    if res['result'] == 100:
        await context.bot.send_message(chat_id=f'{update.message.chat_id}' ,text=f"""your link created""",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='Paymen Link',web_app=WebAppInfo(url=f'{res["payLink"]}'))]]))

token = '6412423193:AAEzuwMteiD7k5z3SV7X1UIVGiIreoUFNdk'

def main():
    application = Application.builder().token(token).build()
    starting = CommandHandler('start', start)
    application.add_handler(starting)
    application.run_polling()

if __name__ == '__main__':
    main()
