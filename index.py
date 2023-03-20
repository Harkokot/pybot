#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyTelegramBotAPI


# In[3]:


pip install -U python-telegram-bot


# In[1]:


import telebot
from telebot import types
import os

bot = telebot.TeleBot('5334416501:AAG6ajdrdyRzOayULKKp6yq8VTN-o0TeFSI')

#создаем основное меню с кнопками для перехода между разными шагами
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu_1 = types.KeyboardButton('Шаг 1')
menu_2 = types.KeyboardButton('Шаг 2')
menu_3 = types.KeyboardButton('Шаг 3')
menu_4 = types.KeyboardButton('Шаг 4')
menu.add(menu_1, menu_2, menu_3, menu_4)

#создаем функцию, которая реагирует на команду Старт приветствием 
#и выводит основное меню
@bot.message_handler(commands=['start'])
def start(message):
    photo_menu = open('/Users/lufant/Documents/Фото боту/IMG_7134.jpg', 'rb')
    a = (f'<b>Привет, {message.from_user.first_name}!</b>\nЭтот бот поможет '
            f'тебе раскрепоститься перед съемкой. Нажми на тот шаг, с '
            f'которого хочешь начать')
    
    bot.send_photo(message.chat.id, photo_menu)
    bot.send_message(message.chat.id, a, reply_markup=menu, parse_mode='html')

if_not = 'Не совсем тебя понимаю, нажми лучше кнопочку'

buttons = ['Шаг 1', 'Шаг 2', 'Шаг 3', 'Шаг 4',            'Стас Пьеха, Дима Билан', 'Тимати, Егор Крид',            'Король и Шут, Би-2', 'Сходить к психологу',            'Выбрать правильного фотографа', 'Купить курс по обработке фото']

#создаем функцию, которая проверяет нажатие на кнопку: если пользователь 
#ввел текст, которого нет в списке, просим его использовать кнопки
def dec(message):
    if message.text not in buttons:
        bot.send_message(message.chat.id, if_not,         reply_markup=menu, parse_mode='html')

step_2_text_1 = (f'<b>Подумай вместе с фотографом!</b>\nВам нужно создать '
                 f'идею, которая будет подходить именно тебе. Подготовься '
                 f'заранее: найди подходящие позы или попроси фотографа '
                 f'скинуть. Потренируйся позировать у зеркала')
step_2_text_2 = 'Куда дальше?'       

#создаем функцию, которая реагирует на кнопку Шаг 2 и выводит фото 
#с информацией, после ответов возвращает к основному меню
def step_2(message):
    if message.text == 'Шаг 2':
        
        os.chdir('/Users/lufant/Documents/Фото боту')
        with open('IMG_9638.jpg', 'rb') as photo_2:
            bot.send_photo(message.chat.id, photo_2)
        bot.send_message(message.chat.id, step_2_text_1, parse_mode='html')
        bot.send_message(message.chat.id, step_2_text_2,         reply_markup=menu, parse_mode='html')

step_3_text = (f'<b>На съемке включи свою музыку</b>\nПостарайся подобрать '
                    f'треки, которые хорошо отражают атмосферу фотосета.\nК '
                    f'примеру, какие российские исполнители лучше всего '
                    f'подойдут для съемки по такому мудборду?')
        
opros_3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
opros_3_1 = types.KeyboardButton('Стас Пьеха, Дима Билан')
opros_3_2 = types.KeyboardButton('Тимати, Егор Крид')
opros_3_3 = types.KeyboardButton('Король и Шут, Би-2')
opros_3.add(opros_3_1, opros_3_2, opros_3_3)       

answer_3 = (f'<b>Верно!</b>\nМудборд передает мрачную и мистическую '
            f'атмосферу, которая лучше всего отражена в творчестве групп КиШ '
            f'и Би-2.\nПоэтому для фотосета лучше выбрать музыку именно этих '
            f'исполнителей')
wrong_answer_3_1 = (f'<b>Не совсем так.</b>\nЭти два музыканта исполняют '
                    f'легкие, динамичные композиции про любовь, которые плохо '
                    f'впишутся в съемку с мрачной и мистической '
                    f'атмосферой.\nДля нее лучше выбрать песни КиШ и Би-2')
wrong_answer_3_2 = (f'<b>Не совсем так.</b>\nЭти два музыканта исполняют '
                    f'легкие, динамичные рэп-композиции, которые плохо '
                    f'впишутся в съемку с мрачной и мистической '
                    f'атмосферой.\nДля нее лучше выбрать песни КиШ и Би-2')
answer_3_1 = 'Выбери последний шаг'

#создаем функцию с вариантами ответа для функции Шаг 3
def step_3_3(message):
    if message.text == 'Король и Шут, Би-2':
        os.chdir('/Users/lufant/Documents/Фото боту')
        with open('IMG_3194.jpg', 'rb') as photo_3_1:
            bot.send_photo(message.chat.id, photo_3_1)
        bot.send_message(message.chat.id, answer_3, parse_mode='html')
        bot.send_message(message.chat.id, answer_3_1, reply_markup=menu,         parse_mode='html')
    if message.text == 'Стас Пьеха, Дима Билан':
        os.chdir('/Users/lufant/Documents/Фото боту')
        with open('IMG_5346.jpg', 'rb') as photo_3_2:
            bot.send_photo(message.chat.id, photo_3_2)
        bot.send_message(message.chat.id, wrong_answer_3_1, parse_mode='html')
        bot.send_message(message.chat.id, answer_3_1, reply_markup=menu,         parse_mode='html')
    if message.text == 'Тимати, Егор Крид':
        os.chdir('/Users/lufant/Documents/Фото боту')
        with open('IMG_4655.JPG', 'rb') as photo_3_3:
            bot.send_photo(message.chat.id, photo_3_3)
        bot.send_message(message.chat.id, wrong_answer_3_2, parse_mode='html')
        bot.send_message(message.chat.id, answer_3_1, reply_markup=menu,         parse_mode='html')

#создаем функцию, которая реагирует на кнопку Шаг 3, выводит фото 
#с вопросом и кнопками-вариантами ответа, после ответов возвращает
#к основному меню
def step_3(message):
    if message.text == 'Шаг 3':
        
        os.chdir('/Users/lufant/Documents/Фото боту')
        with open('C.png', 'rb') as photo_3:
            bot.send_photo(message.chat.id, photo_3)
        bot.send_message(message.chat.id, step_3_text,         reply_markup=opros_3, parse_mode='html')
    
    step_3_3(message)
    
step_4_text_1 = (f'<b>Хочешь главное правило фотосетов?</b>\nНе думай о '
                    f'плохом результате. Забудь обо всем, кроме себя и '
                    f'возможности ненадолго прожить жизнь в новом амплуа. '
                    f'Отбрось негатив, и получишь прекрасные кадры')
step_4_text_2 = (f'Напоследок лови гайд по позированию от портретного '
                    f'фотографа Александра Медведева:')
step_4_text_3 = 'Пиши мне в тг @xvoino, расскажу как проходят мои съемки'
video_4 = types.InlineKeyboardMarkup()
url_4 = 'https://www.youtube.com/watch?v=RWglzrKC_hk'
video_4.add(types.InlineKeyboardButton('Смотреть гайд', url=url_4))

#создаем функцию, которая реагирует на кнопку Шаг 4, выводит фото 
#с информацией, ссылкой и упоминанием автора для связи,
#убирает клавиатуру
def step_4(message):
    if message.text == 'Шаг 4':
        
        os.chdir('/Users/lufant/Documents/Фото боту')
        with open('IMG_7049.jpg', 'rb') as photo_4:
            bot.send_photo(message.chat.id, photo_4)
        bot.send_message(message.chat.id, step_4_text_1,                          reply_markup=types.ReplyKeyboardRemove(),                          parse_mode='html')
        bot.send_message(message.chat.id, step_4_text_2, reply_markup=video_4)
        bot.send_message(message.chat.id, step_4_text_3, parse_mode='html')

step_1_text = (f'Возможно, ты переживаешь, что плохо получишься в кадре. '
                f'Хочешь приобрести уверенность перед камерой? Угадай, что '
                f'нужно сделать для этого в первую очередь:')
    
opros_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
opros_1_1 = types.KeyboardButton('Сходить к психологу')
opros_1_2 = types.KeyboardButton('Выбрать правильного фотографа')
opros_1_3 = types.KeyboardButton('Купить курс по обработке фото')
opros_1.add(opros_1_1, opros_1_2, opros_1_3)     
        
answer_1 = (f'<b>Ты абсолютно прав.</b>\nОчень важно выбрать фотографа, '
            f'который подходит по стилю и подходу к работе.\nТы должен '
            f'чувствовать уверенность в результате и комфорт во время '
            f'съемки.\nПойти к психологу хороший вариант, но фотосессия — '
            f'тоже терапия, которая помогает принять себя и свою внешность')
wrong_answer_1 = (f'<b>Не совсем так.</b>\nОчень важно сначала выбрать '
                    f'фотографа, который подходит по стилю и подходу к '
                    f'работе.\nТы должен чувствовать уверенность в '
                    f'результате, тебе должно быть комфортно во время '
                    f'съемки.\nПойти к психологу хороший вариант, но '
                    f'фотосессия — тоже терапия, которая помогает '
                    f'принять себя и свою внешность')
answer_1_1 = 'Куда дальше?'

def step_1_1(message):
    if message.text == 'Выбрать правильного фотографа':
        os.chdir('/Users/lufant/Documents/Фото боту')
        with open('IMG_2935.jpg', 'rb') as photo_1_1:
            bot.send_photo(message.chat.id, photo_1_1)
        bot.send_message(message.chat.id, answer_1, parse_mode='html')
        bot.send_message(message.chat.id, answer_1_1, reply_markup=menu,         parse_mode='html')
    if (message.text == 'Сходить к психологу' or
    message.text == 'Купить курс по обработке фото'):
        os.chdir('/Users/lufant/Documents/Фото боту')
        with open('IMG_7614.jpg', 'rb') as photo_1_2:
            bot.send_photo(message.chat.id, photo_1_2)
        bot.send_message(message.chat.id, wrong_answer_1, parse_mode='html')
        bot.send_message(message.chat.id, answer_1_1, reply_markup=menu,         parse_mode='html')

#создаем основную функцию, которая считывает текст и в зависимости от него
#выводит информацию: если Шаг 1, то фото+информация+кнопки с вариантами
#ответа, если другие шаги — реализует функции этих шагов, если
#пользователь ввел свой текст — реализует функцию с просьбой использовать 
#кнопки
@bot.message_handler(content_types=['text'])
def step_1(message):
    if message.text == 'Шаг 1':

        os.chdir('/Users/lufant/Documents/Фото боту')
        with open('IMG_6078.jpg', 'rb') as photo_1:
            bot.send_photo(message.chat.id, photo_1)
        bot.send_message(message.chat.id, step_1_text, reply_markup=opros_1,         parse_mode='html')     

    step_1_1(message)

    step_2(message)

    step_3(message)

    step_4(message)

    dec(message)
        
bot.polling(none_stop=True)


# In[ ]:




