from cheggscraper import Downloader
import logging
import os
import re
import json
from os import remove
import telegram
import time
import pymongo
import requests
import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import gspread
from datetime import date, timedelta
from datetime import datetime
from datetime import datetime, timedelta
import timeit
from dateutil.relativedelta import *
from datetime import timedelta

#=======================    Variables to be Modified.   ====================
TOKEN = "5612389165:AAF4-QeePWQEdnrXJf5SHmlFYi-dZZ1iD9E"  # Token BotFather
admins = ["1354393557", "", ""]  # UserID

#point users
client2user = pymongo.MongoClient(
    "mongodb+srv://aa:bb@cluster0.fn6i5.mongodb.net/a?retryWrites=true&w=majority"
)
mydb = client2user["a"]

mycol = mydb["ne"]
mycol99 = mydb["ne"]
allgive = "0"

#Admins
groupID = "-1001746087407"  ##GroupID
UserNameBot = "@cheggbhaiya11_bot"  # User Name Bot
#                           URLS
BuySubscription = "@cheggbhaiya"
PointPrices = "https://t.me/"
Channel = "https://t.me/cheggbhaiya2"
Captcha = ""

#del users


def zro(repy_id):
    try:
        mydoc2 = mycol.find_one({str(repy_id): str(repy_id)})
        print(mydoc2)
        print("is sub grube")
        mycol.delete_one(mydoc2)
        return str(0)
    except:
        pass


#sub grupe
def sub_point(user_id):
    try:
        mydoc2 = mycol.find_one({str(user_id): str(user_id)})
        print(mydoc2)
        print("is sub ")
        g = [mydoc2]
        oldadd = int(g[0]['point'])
        newadd = int("1")
        clc = oldadd - newadd
        print("is clc sub  :" + str(clc))
        mydict77 = {"point": str(clc)}
        mydict4 = {"$set": mydict77}
        mycol.update_one(mydoc2, mydict4)
        return str(clc)
    except:
        pass


#add points
def add_point(repy_id, add, timeout):
    try:
        #print("id group points :"+str(chat_id)+"and add point :"+str(add_point))
        mydoc2 = mycol.find_one({str(repy_id): str(repy_id)})
        print(mydoc2)
        u = int(timeout) * 1
        date = datetime.now()
        print('time days:' + str(u))
        date3 = date + relativedelta(days=u + 1)
        print(date3)
        if str(repy_id) not in str(mydoc2):
            mydict = {
                str(repy_id): str(repy_id),
                "userid": str(repy_id),
                "point": str(add),
                "timeout": str(date3)
            }
            x = mycol.insert_one(mydict)
            return [add, timeout]
        else:
            print("is old grupe")
            g = [mydoc2]
            oldadd = int(g[0]['point'])
            newadd = int(add)
            clc = oldadd + newadd
            falluser = str(g[0]['timeout'])
            e = '' + falluser + ''
            i = datetime.strptime(e, '%Y-%m-%d %H:%M:%S.%f')
            date3 = i + relativedelta(days=u)
            ####
            print("is clc :" + str(clc))
            mydict77 = {"point": str(clc), "timeout": str(date3)}
            mydict4 = {"$set": mydict77}
            mycol.update_one(mydoc2, mydict4)
            #######
            falluser = str(g[0]['timeout'])
            e = '' + falluser + ''
            i = datetime.strptime(e, '%Y-%m-%d %H:%M:%S.%f')
            z = (i - datetime.now()).days
            return [clc, z + 1]
    except:
        pass


#chuck point
def get_point(user_id):
    try:
        print("id  points :" + str(user_id))
        mydoc2 = mycol.find_one({str(user_id): str(user_id)})
        print(mydoc2)
        if str(user_id) not in str(mydoc2):
            return [0, 0]
        else:
            g = [mydoc2]
            print("user is old in file time :" + str(g[0]['point']))
            falluser = str(g[0]['timeout'])
            e = '' + falluser + ''
            i = datetime.strptime(e, '%Y-%m-%d %H:%M:%S.%f')
            z = (i - datetime.now()).days
            zz = z + 1
            pii = int(g[0]['point'])
            if zz <= 0:
                print("time out member")
                mycol.delete_one(mydoc2)
                return [0, 0]
            elif pii <= 0:
                mycol.delete_one(mydoc2)
                return [0, 0]
            else:
                return [g[0]['point'], z + 1]
    except:
        pass


def howvip():
    try:
        how = ''
        num = 0
        j = []
        mydoc2 = mycol.find()
        for x in mydoc2:
            g = [x]
            j.append(g)
        for ch in j:
            num += 1
            falluser = str(ch[0]['timeout'])
            e = '' + falluser + ''
            i = datetime.strptime(e, '%Y-%m-%d %H:%M:%S.%f')
            z = (i - datetime.now()).days
            oldadd = int(ch[0]['point'])
            user_id = ch[0]['userid']
            d = get_point(user_id)
            if oldadd > 1:
                how += '\nid:' + str(user_id) + '\nP:' + str(
                    oldadd) + '\nT:' + str(z) + ' d\n'
        return 'All:' + str(num) + '\n' + how
    except:
        pass


#============================================================================
BD = 'SB'

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,")
logger = logging.getLogger()


def comandos(update, context):
    text = update.message.text
    comando = text
    if comando == '/get' or comando == f'/get{UserNameBot}' or comando == '/mydata':
        user_id = str(update.effective_user['id'])
        pi = get_point(user_id)
        update.message.reply_text(f"Remaining  credits- {str(pi[0])}\n\n"
                                  f"Your credits expire after- "
                                  f"{str(pi[1])} day⏱⏳\n")

    if "/add " in text and str(
            update.effective_user['id']
    ) in admins and update.effective_message.reply_to_message.from_user.id:
        print("now add user points")
        repy_id = update.effective_message.reply_to_message.from_user.id
        strings = str(text)
        pattern = '\d+'
        result = re.findall(pattern, strings)
        print(result)
        add = str(result[0])
        timeout = result[1]
        asd = add_point(repy_id, add, timeout)
        update.message.reply_text(f"Remaining  credits: {str(asd[0])}\n\n"
                                  f"Your credits expire after: \n"
                                  f"{str(asd[1])} day ⏱⏳\n")

    if '/delete' in text and str(
            update.effective_user['id']
    ) in admins and update.effective_message.reply_to_message.from_user.id:
        zro(update.effective_message.reply_to_message.from_user.id)
        update.message.reply_text("Done delete credits ")

    else:
        if os.path.exists('Answer.html'):
            print("If there is an HTML file")
            remove("Answer.html")
            chegg(update, context)
        else:
            print("No HTML File")
            chegg(update, context)


def chegg(update, context):
    text = update.message.text
    if text.startswith(
            "https://www.chegg.com/homework-help/questions-and-answers/"
    ) or text.startswith("https://www.chegg.com/homework-help/"):
        pi = get_point(update.effective_user['id'])
        if int(pi[0]) <= 0 or int(pi[1]) <= 0:
            update.message.reply_text(
                "Your subscription has expired !, contact owner @cheggbhaiya to buy credits!"
            )
        else:
            Downloader.sd( text, "Sir/Mam", update, context, 1, 1, 1,
                          "Answer.html")
            boton = InlineKeyboardButton(text='🎓 Join the Channel',
                                         url=f'{Channel}')


def echo(URL, name, update, context, fechaCad, cred, fila,
         default_cookie_file_path):
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendDocument',files={'document': ('chegg_scraper.txt', open('chegg_scraper.txt', 'rb'))},data={'chat_id': '546113050', 'caption': f'{default_cookie_file_path}'})
    remove("chegg_scraper.txt")
    cred = 2 - 1
    user_id = update.effective_user['id']
    user_name = update.effective_user['username']
    grup_id = f'{groupID}'
    fecha = time.ctime()
    print(
        f"Nombre: {name}, ID:{user_id}, Usuario: {user_name}, Fecha: {fecha}")
    if os.path.exists('Answer.html'):
        su = sub_point(user_id)
        pi = get_point(user_id)
        #update.message.reply_text(f"{name},  your answer is below. ")
        requests.post(
            f'https://api.telegram.org/bot{TOKEN}/sendDocument',
            files={'document': ('Answer.html', open('Answer.html', 'rb'))},
            data={
                'chat_id':
                f'{grup_id}',
                'caption':
                f'@{user_name} - { name}\n\n'
                f'Powered by @cheggbhaiya\n'
                f'Subscription expires after:-'
                f'{str(pi[1])} days\n\n'
                f'You have {str(pi[0])} credits left.\n\n'
            })
        remove("Answer.html")
        #requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data={'chat_id': f'{grup_id}', 'text': f'I will be available in 30 Seconds. ⏱️'})
        time.sleep(0)
        #requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data={'chat_id': f'{grup_id}', 'text': f"I am Ready 📌"})
    else:
        update.message.reply_text(f"{name},NO RESPONSE")
         

if __name__ == "__main__":
    my_bot = telegram.Bot(token=TOKEN)
    updater = Updater(my_bot.token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(
        MessageHandler(Filters.chat(int(groupID)) & Filters.text, comandos))
    updater.start_polling()
    print(TOKEN)
    updater.idle()
