import telegram

bot = telegram.Bot(token = '5038045836:AAHlx2ieZK4LH5yhzPEqhO8LI9TasoMenpI')

# for i in bot.getUpdates():
#     print(i.message)

bot.sendMessage(chat_id = 5000538977, text = "테스트 입니다.")