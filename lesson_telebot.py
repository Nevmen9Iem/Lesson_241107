import random
import telebot
from google.cloud import bigquery
from google.oauth2 import service_account

bot = telebot.TeleBot("")
credentials = service_account.Credentials.from_service_account_file(
    "C:/Users/Dreimond/Downloads/Telegram Desktop/itstep-382618-558382b49c6f.json")
project_id = "itstep-382618"
client = bigquery.Client(credentials=credentials, project=project_id)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Anigil9torna9 pushka")


####
##@bot.message_handler(content_types=["text"])
##def info(message):
##    if message.text.lower()=="sum":
##        query_job=client.query("""SELECT round(sum(bb.payment_sum)) as koli4estvo
##                                 FROM `itstep-382618`.itstep_bot.data_base as bb""")
##        results=query_job.result()
##        bot.send_message(message.chat.id,results)


@bot.message_handler(content_types=['text'])
def info(message):
    if message.text.lower() == "sum":
        query_job = client.query("""
                                SELECT 
                                round(sum(tb.payment_sum),2) AS sum_total
                                FROM `itstep-382618`.itstep_bot.data_tb AS tb  
                               """)
        results = query_job.result()
        bot.send_message(message.chat.id, results)
    ##    elif message.text.lower()=="group":
    ##        query_job=client.query("""
    ##                                SELECT
    ##                                tb.period,
    ##                                round(sum(tb.payment_sum),2) AS sum_total
    ##                                FROM `itstep-382618`.itstep_bot.data_tb AS tb
    ##                                GROUP BY tb.period
    ##                                ORDER BY 2 DESC
    ##                                LIMIT 5
    ##                               """)
    ##        results=query_job.result()
    ##        bot.send_message(message.chat.id,results)

    ##
    elif message.text.lower() == "group":
        query_job = client.query("""
                                SELECT
                                bb.period, 
                                round(sum(bb.payment_sum)) as koli4estvo
                                FROM `itstep-382618`.itstep_bot.data_tb as bb
                                group by bb.period 
                                order BY 2 DESC 
                                limit 5  
                               """)
        results = query_job.result()
        bot.send_message(message.chat.id, results)
    elif message.text.lower() == "group1":
        query_job = client.query("""
                                SELECT
                                bb.period, 
                                round(sum(bb.payment_sum)) as koli4estvo
                                FROM `itstep-382618`.itstep_bot.data_tb as bb
                                group by bb.period 
                                order BY 2 DESC 
                                limit 5  
                               """)
        results = query_job.result()
        print(list(results))


##


###
@bot.message_handler(commands=["close"])
def close(message):
    bot.send_message(message.chat.id, "<em><b>ohrana otmena</b></em>", parse_mode="html")


@bot.message_handler(content_types=["text"])
def user_text(message):
    if message.text == "Hi":
        bot.send_message(message.chat.id, "Hi, Hi " + message.from_user.first_name, parse_mode="html")  ##or last or id
        # bot.send_message(message.chat.id,"Hi, Hi "+message.from_user.id,parse_mode="html")
    elif message.text == "Num":
        num = random.randrange(1, 1000)
        bot.send_message(message.chat.id, num)
    elif message.text == "photo":
        ph = open("C:/Users/Dreimond/Downloads/images (4).jpg", 'rb')  # rb read and pokazatb
        bot.send_photo(message.chat.id, ph)
    elif message.text == "show":
        bot.send_sticker(message.chat.id,
                         sticker="CAACAgIAAxkBAANBZuMxJjMi9vc4vbKR7NeWhsdN694AAoRGAAKGu6FKsSa54ta5PEY2BA")
    else:
        bot.send_message(message.chat.id, "Error", parse_mode="html")


@bot.message_handler(content_types=['sticker'])
def user_sticker(message):
    sticker_id = message.sticker.file_id
    bot.send_message(message.chat.id, sticker_id)


bot.infinity_polling()