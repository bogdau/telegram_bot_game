import telebot
from telebot import types


token=''
bot=telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Hi, it is the Bot which provide some info about games! ')
    
@bot.message_handler(commands=['button'])
def button_message(message):
    # bot.send_message(message.chat.id,'Choose the game in button')
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Roblox")
    item2=types.KeyboardButton("Minecraft")
    item3=types.KeyboardButton("GTA san andreas")
    item4=types.KeyboardButton("GTA V")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id,'Choosse what u want',reply_markup=markup)
    
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Button":
        # bot.send_message(message.chat.id,'Choose the game in button')
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Roblox")
        item2=types.KeyboardButton("Minecraft")
        item3=types.KeyboardButton("GTA san andreas")
        item4=types.KeyboardButton("GTA V")
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id,'Choosse what u want',reply_markup=markup)
    elif message.text=="Roblox":
        img = open("roblox.png", 'rb')
        bot.send_photo(message.chat.id, img, caption='''Roblox is an online game platform and
game creation system developed by Roblox Corporation that allows
users to program and play games created by themselves or other users.
It was created by David Baszucki and Erik Cassel in 2004, and released
to the public in 2006. As of August 2020, the platform has over 164
million monthly active users, including half of all American children under the age of 16.''')
    elif message.text=="Minecraft":
        bot.send_message(message.chat.id,'Bye')
    elif message.text=="GTA san andreas":
        bot.send_message(message.chat.id,'GTA san andreas')
    elif message.text=="GTA V":
        bot.send_message(message.chat.id,'GTA V')
    else:
        # bot.send_message(message.chat.id,'Choose the game in button')
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Roblox")
        item2=types.KeyboardButton("Minecraft")
        item3=types.KeyboardButton("GTA san andreas")
        item4=types.KeyboardButton("GTA V")
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id,'Choosse what u want',reply_markup=markup)
        
bot.infinity_polling()
