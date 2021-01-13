import schedule
import time
import config
import telebot
import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://weather.rambler.ru/v-voronezhe')
html = BS(r.content, 'html.parser')
bot = telebot.TeleBot('1409804866:AAHjRy-UDUfsgJivrGc8sUpFYvsyHa25ou4')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('/start')

for el in html.select('#header-space'):
    t_min = el.select('._1HBR')[0].text
    u = el.select('.UJ_C')[0].text
    night = el.select('.P2oi')[0].text
    text = el.select('.Hixd')[0].text

@bot.message_handler(commands=['start', 'help'])
def main(message):
    bot.send_message(message.chat.id, "Привет, погода на сегодня в Воронеже:\n" +
    t_min + ', ' + u + ', '+ night + '\n' + text, reply_markup=keyboard1)

if __name__ == '__main__':
    bot.polling(none_stop=True)
def job():
    print("/start")
    schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)