import telebot
import openai

# Replace with your keys
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(func=lambda message: True)
def chat_with_ai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message.text}]
    )
    bot.reply_to(message, response["choices"][0]["message"]["content"])

bot.polling()
