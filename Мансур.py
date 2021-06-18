import telebot
from telebot import types
import requests

TOKEN = '1720458307:AAFhGB66NVV35UgdvsJhmrRgUprmuoZxEpI'

WEATHER_TOKEN = 'ec92b34a0720e9ae01f7c775538e6589'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['test', 'start', 'help', 'weather', 'film', 'find', 'profile', 'calculate'])
def start_bot(message):
    if message.text.lower() == '/start':
        keyboard = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton('Шутка',callback_data= 'joke')
        google = types.InlineKeyboardButton(
            'гугл',
            url='https://google.ru')
        test = types.InlineKeyboardButton('Тест', callback_data='test')
        keyboard.add(btn)
        keyboard.add(google)
        keyboard.add(test)
        
        bot.send_message(message.chat.id,
                        'всем привет!\n Я новый бот',
                        reply_markup=keyboard)
    

    if message.text.lower() == '/start':
        bot.send_message(message.chat.id, 'вот список команд\n/help\n/weather\n/film\n/find\n/profile\n/calculate')
        
        
    elif message.text.lower() == '/weather':
        bot.send_message(message.chat.id, 'вы в разделе погода')
        bot.send_message(message.chat.id, 'введите названия города')
        bot.register_next_step_handler(message, weather_menu)
        
    elif message.text.lower() == '/help':
        bot.send_message(message.chat.id, 'вы сами разберетесь')
        bot.send_message(message.chat.id, 'я в вас верю')
    
    elif message.text.lower() == '/film':
        bot.send_message(message.chat.id, 'какой жанр вы хотите посмотреть')
        
    elif message.text.lower() == '/find':
        bot.send_message(message.chat.id, 'что вы хотите найти?')
        
    elif message.text.lower() == '/profile':
        bot.send_message(message.chat.id, 'вы хотите заполнить профиль?')
        bot.send_message(message.chat.id, 'тогда скажите свое имя')
        bot.register_next_step_handler(message, enter_name)
        
    elif message.text.lower() == '/calculate':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('плюс')
        btn2 = types.KeyboardButton('минус')
        btn3 = types.KeyboardButton('делить')
        btn4 = types.KeyboardButton('умножить')
        btn5 = types.KeyboardButton('степень')
        keyboard.add(btn1)
        keyboard.add(btn2)
        keyboard.add(btn3)
        keyboard.add(btn4)
        keyboard.add(btn5)
        bot.send_message(message.chat.id,
                         'выберите действие:',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, calculate_choose)
def calculate_choose(message):
    if message.text.lower() == 'плюс':
        bot.send_message(message.chat.id, "что вы хотите сложить?")
        bot.send_message(message.chat.id, "введите два числа через пробел")
        bot.register_next_step_handler(message, calculate_result_plus)
    elif message.text.lower() == 'минус':
        bot.send_message(message.chat.id, "что вы хотите вычеслить?")
        bot.send_message(message.chat.id, "введите два числа через пробел")
        bot.register_next_step_handler(message, calculate_result_minus)
    elif message.text.lower() == 'делить':
        bot.send_message(message.chat.id, "что вы хотите разделить")
        bot.send_message(message.chat.id, "введите два числа через пробел")
        bot.register_next_step_handler(message, calculate_result_divide)
    elif message.text.lower() == 'умножить':
        bot.send_message(message.chat.id, "что вы хотите умножить?")
        bot.send_message(message.chat.id, "введите два числа через пробел")
        bot.register_next_step_handler(message, calculate_result_multiply)
    elif message.text.lower() == 'степень':
        bot.send_message(message.chat.id, "что вы хотите возвести в степень?")
        bot.send_message(message.chat.id, "введите два числа через пробел")
        bot.register_next_step_handler(message, calculate_result_stepen)
def calculate_result_plus(message):
    nums = message.text.split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    bot.send_message(message.chat.id, f"результат {num1 + num2}")
def calculate_result_minus(message):
    nums = message.text.split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    bot.send_message(message.chat.id, f"результат {num1 - num2}")
def calculate_result_divide(message):
    nums = message.text.split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    bot.send_message(message.chat.id, f"результат {num1 / num2}")
def calculate_result_multiply(message):
    nums = message.text.split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    bot.send_message(message.chat.id, f"результат {num1 * num2}")
def calculate_result_stepen(message):
    nums = message.text.split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    bot.send_message(message.chat.id, f"результат {num1 ** num2}")

@bot.message_handler(content_type=['text'])
def enter_name(message):
    name = message.text
    bot.send_message(message.chat.id, f"твое имя {name}")
    bot.send_message(message.chat.id, f"какой у тебя возраст?")
    bot.register_next_step_handler(message, enter_age)
@bot.message_handler(content_type=['text'])
def enter_age(message):
    vozrast = message.text
    bot.send_message(message.chat.id, f"тебе {vozrast} лет")
    bot.send_message(message.chat.id, f"какой у тебя номер телефона?")
    bot.register_next_step_handler(message, enter_number)
@bot.message_handler(content_type=['text'])
def enter_number(message):
    nomer = message.text
    bot.send_message(message.chat.id, f"твой номер телефона: {nomer}")
    bot.send_message(message.chat.id, f"где вы живете")
    bot.register_next_step_handler(message, enter_place)
@bot.message_handler(content_type=['text'])
def enter_place(message):
    zhizn = message.text
    bot.send_message(message.chat.id, f"вы живете в {zhizn}")
    bot.send_message(message.chat.id, f"какой у вас любимый фильм?")
    bot.register_next_step_handler(message, enter_film)
@bot.message_handler(content_type=['text'])
def enter_film(message):
    kino = message.text
    bot.send_message(message.chat.id, f"ваш любимый фильм {kino}")
    bot.send_message(message.chat.id, f"вы создали свой профиль")
    
    
@bot.callback_query_handler(func=lambda x: x.data == 'joke')
def joke_fn(message):
    bot.send_message(message.from_user.id, 'https://youtu.be/JyD13ifbAN4')
    
    
@bot.callback_query_handler(func=lambda x: x.data == 'test')
def test_btn(message):
    keyboard = types.InlineKeyboardMarkup()
    btn7 = types.InlineKeyboardButton('100 м',callback_data='ere1')
    btn8 = types.InlineKeyboardButton('600 м', callback_data='ere2')
    btn9 = types.InlineKeyboardButton('700 м', callback_data='ere1')
    keyboard.add(btn7)
    keyboard.add(btn8)
    keyboard.add(btn9)
    bot.send_message(message.from_user.id, 'Вопрос: Cколько метров эйфелевая башня?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda x: x.data == 'ere1')
def answer1(message):
    bot.send_message(message.from_user.id, 'вы идиот!')
@bot.callback_query_handler(func=lambda x: x.data == 'ere2')
def answer2(message):
    bot.send_message(message.from_user.id, 'верный ответ')


def weather_menu(message):
    city = message.text
    API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}'
    r = requests.get(API_URL)
    w = r.json()
    bot.send_message(message.chat.id, f"в городе: {w['name']}")
    bot.send_message(message.chat.id, f"Температура: {w['main']['temp']-273.15}")
    bot.send_message(message.chat.id, f'Скорость ветра: {w["wind"]["speed"]}м/c')
    bot.send_message(message.chat.id, f'Давление: {w["main"]["pressure"]}Па' )
    bot.send_message(message.chat.id, f'Влажность: {w ["main"]["humidity"]}%')
    
    
    
    
    
    
    
    
    
    
    
    
    
bot.polling()