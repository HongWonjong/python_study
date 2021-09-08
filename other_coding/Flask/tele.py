from main.board import telegram_bot
import telegram

chat_token = "1932369917:AAH1rreLUbVapprkK1FaenhXCL8EqPMpLmA"
bot = telegram.Bot(token = chat_token)
text = "듣고 계시나요?"
bot.sendMessage(chat_id="1800637190", text=text)