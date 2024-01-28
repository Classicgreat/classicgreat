import telebot
import requests

token="6986062237:AAEtRLUsUoXpuoAleCubfdEZmKwnpjVSsEg"
keyboard=["meny","exit"]

bot=telebot.TeleBot(token)

def getinfo(ip:str)->dict:
    url=f"https://ipinfo.io/{ip}/geo"
    r=requests.get(url).json()
    b=""
    for i in r:
        if i!="readme":b=b+str(i)+" "+str(r[i])+"\n"
    return b

def generator_keyboards(ListNameBTN,NumberColumns=2):
    keyboards=telebot.types.ReplyKeyboardMarkup(row_width=NumberColumns,resize_keyboard=True)
    btn_names=[telebot.types.KeyboardButton(text=x) for x in ListNameBTN]
    keyboards.add(*btn_names)
    return keyboards

def getip(message):
    ip=message.text
    info=getinfo(ip)
    bot.send_message(message.chat.id, info)

@bot.message_handler(commands=["start"])
def start(message):
    #print(message)
    msg=bot.send_message(message.chat.id,"hello",reply_markup=generator_keyboards(keyboard))
    #bot.reply_to(message,"Сверху лох")
    bot.register_next_step_handler(msg, getip)

@bot.message_handler(func=lambda m:m.text)
def text(message):
    global keyboard
    text=message.text
    if text=="meny":
        bot.send_message(message.chat.id, "ses")
    elif text=="exit":
        bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=GFq6wH5JR2A")
        keyboard=["sas","sos"]
    elif text=="sas":
        bot.send_message(message.chat.id, "good")

if __name__=="__main__":
    bot.infinity_polling()