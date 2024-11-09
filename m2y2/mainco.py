import telebot
import random
import os
 

bot = telebot.TeleBot('7510960627:AAFTtDwFFbswyAWHz-pQ1DMHf668dDOdTsI')

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}! я бот который расскажет вам  о экологии кратко и ясно')

@bot.message_handler(commands=['eco_photo'])
def send_mem(message):
    random_image = random.choice(os.listdir('images'))
    with open(f'images/{random_image}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['ecoinfo'])
def send_ecoinfo(message):
    bot.reply_to(message,
        "Экология — это наука, изучающая взаимодействия между живыми организмами и их окружением. "
        "Она исследует, как природа работает и как все организмы связаны друг с другом. Например, удаление одного "
        "вида насекомых из экосистемы может повлиять на популяции птиц или растений.\n\n"
        "К сожалению, человеческая деятельность, такая как загрязнение и вырубка лесов, часто наносит вред экосистемам. "
        "Экология помогает понять эти воздействия и минимизировать негативные последствия, а также сохранять природный баланс. "
        "Например, избыток удобрений в воде может вызвать цветение, угрожающее рыбам. Экология играет важную роль в "
        "предотвращении таких проблем."
    )

@bot.message_handler(commands=['Greenpeace'])
def send_bye(message):
    bot.reply_to(message, "В нашем мире есть международная неправительственная экологическая организация в, которой находятся такие проблемы, как глобальное изменение климата, сокращение площади лесов, , чрезмерный вылов рыбы и тд")

@bot.message_handler(commands=['ecobook'])
def send_ecobook(message):
    image_path = 'images/ecobook.jpg'  
    if os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            bot.send_photo(message.chat.id, f)
        bot.reply_to(message, 
            "Если вы заинтересовались в этой теме, то прочитайте эту книгу:\n"
            "'Ecology: Sixth Edition' by William Bowman and Sally Hacker.")


bot.polling()
