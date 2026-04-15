import telebot 
from telebot import types
import wikipedia
import os

wikipedia.set_lang('ru')

bot = telebot.TeleBot('') #нужно вставить токен

# Создание папки для загруженных файлов
if not os.path.exists('uploaded_files'):
    os.makedirs('uploaded_files')

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Курсовая по АМИБ", callback_data='file1')
    button2 = types.InlineKeyboardButton(text="Инглиш, топики", callback_data='file2')
    button3 = types.InlineKeyboardButton(text="ЯП", callback_data='file3')
    button4 = types.InlineKeyboardButton(text="Электроника и схемотехника", callback_data='file4')
    keyboard.add(button1, button2, button3, button4)
    txt = 'Привет! Я бот, который отправляет файлы по предметам. Выбери что тебе нужно и я тебе пришлю. А также можешь задавать вопросы, я постараюсь на них ответить.)\n\nТы также можешь отправить мне файл, и я его сохраню.'
    bot.send_message(message.chat.id, txt, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def button(call):
    if call.data == 'file1':
        menu1_keyboard = types.InlineKeyboardMarkup()
        sub_button1 = types.InlineKeyboardButton(text="Курсовая по АМИБУ 2 курс 2 сем Андрей", callback_data='submenu1_1')
        sub_button2 = types.InlineKeyboardButton(text="Курсовая работа", callback_data='submenu1_2')
        back_button = types.InlineKeyboardButton(text="Назад", callback_data='back')
        menu1_keyboard.add(sub_button1, sub_button2, back_button)
        bot.send_message(call.message.chat.id, 'Вы выбрали раздел: Курсовая по АМИБ. Выберите подраздел:', reply_markup=menu1_keyboard)

    elif call.data == 'file2':
        menu2_keyboard = types.InlineKeyboardMarkup()
        sub_button1 = types.InlineKeyboardButton(text="инглиш топик 1", callback_data='submenu2_1')
        sub_button2 = types.InlineKeyboardButton(text="инглиш топик 2", callback_data='submenu2_2')
        sub_button3 = types.InlineKeyboardButton(text="инглиш топик 3", callback_data='submenu2_3')
        sub_button4 = types.InlineKeyboardButton(text="инглиш топик 4", callback_data='submenu2_4')
        back_button = types.InlineKeyboardButton(text="Назад", callback_data='back')
        menu2_keyboard.add(sub_button1, sub_button2, sub_button3, sub_button4, back_button)
        bot.send_message(call.message.chat.id, 'Вы выбрали раздел: Инглиш, топики. Выберите подраздел:', reply_markup=menu2_keyboard)

    elif call.data == 'file3':
        menu3_keyboard = types.InlineKeyboardMarkup()
        sub_button1 = types.InlineKeyboardButton(text="ЯП №1 дз C++", callback_data='submenu3_1')
        sub_button2 = types.InlineKeyboardButton(text="ЯП №2 дз C++", callback_data='submenu3_2')
        sub_button3 = types.InlineKeyboardButton(text="ЯП №3 дз C++", callback_data='submenu3_3')
        sub_button4 = types.InlineKeyboardButton(text="ЯП №4 дз C++", callback_data='submenu3_4')
        back_button = types.InlineKeyboardButton(text="Назад", callback_data='back')
        menu3_keyboard.add(sub_button1, sub_button2, sub_button3, sub_button4, back_button)
        bot.send_message(call.message.chat.id, 'Вы выбрали раздел: ЯП. Выберите подраздел:', reply_markup=menu3_keyboard)

    elif call.data == 'file4':
        bot.send_document(call.message.chat.id, open('доклад по схемотехнике.docx', 'rb'))

    elif call.data == 'submenu1_1':
        bot.send_document(call.message.chat.id, open('Курсовая по АМИБУ 2 курс 2 сем Андрей.docx', 'rb'))
    elif call.data == 'submenu1_2':
        bot.send_document(call.message.chat.id, open('Курсовая работа.pdf', 'rb'))

    elif call.data == 'submenu2_1':
        bot.send_document(call.message.chat.id, open('инглиш топик 1.docx', 'rb'))
    elif call.data == 'submenu2_2':
        bot.send_document(call.message.chat.id, open('инглиш топик 2.docx', 'rb')) 
    elif call.data == 'submenu2_3':
        bot.send_document(call.message.chat.id, open('инглиш топик 3.docx', 'rb'))
    elif call.data == 'submenu2_4':
        bot.send_document(call.message.chat.id, open('инглиш топик 4.docx', 'rb'))

    elif call.data == 'submenu3_1':
        bot.send_document(call.message.chat.id, open('ЯП №1 дз C++.txt', 'rb'))
    elif call.data == 'submenu3_2':
        bot.send_document(call.message.chat.id, open('ЯП №2 дз C++.txt', 'rb')) 
    elif call.data == 'submenu3_3':
        bot.send_document(call.message.chat.id, open('ЯП №3 дз C++.txt', 'rb'))
    elif call.data == 'submenu3_4':
        bot.send_document(call.message.chat.id, open('ЯП №4 дз C++.txt', 'rb'))
        
    elif call.data == 'back':
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Курсовая по АМИБ", callback_data='file1')
        button2 = types.InlineKeyboardButton(text="Инглиш, топики", callback_data='file2')
        button3 = types.InlineKeyboardButton(text="ЯП", callback_data='file3')
        button4 = types.InlineKeyboardButton(text="Электроника и схемотехника", callback_data='file4')
        keyboard.add(button1, button2, button3, button4)
        bot.send_message(call.message.chat.id, 'Вы вернулись в главное меню:', reply_markup=keyboard)

@bot.message_handler(content_types=['document'])
def handle_document(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        file_path = os.path.join('uploaded_files', message.document.file_name)

        with open(file_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.send_message(message.chat.id, f"Файл {message.document.file_name} успешно сохранён на сервере.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка при сохранении файла: {str(e)}")

@bot.message_handler(content_types=['text'])
def talk(message):
    if message.text.lower() in ["привет",'здравствуйте', 'hello']:
        bot.send_message(message.chat.id, "Здравствуйте, как ваши дела?")
    elif message.text.lower() in ['хорошо', 'отлично', 'прекрасно', 'замечательно', 'нормально']:
        bot.send_message(message.chat.id, "Я рад за вас!)")
    else:
        try:
            txt = message.text
            page = wikipedia.page(txt)
            bot.send_message(message.chat.id, page.summary)
        except wikipedia.exceptions.PageError:
            bot.send_message(message.chat.id, "Извините, я не нашел информацию по этому запросу")

# Запуск бота
bot.polling(none_stop=True)
