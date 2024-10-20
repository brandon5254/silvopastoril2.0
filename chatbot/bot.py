import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

bot = telebot.TeleBot("7996201736:AAEwdMHRSCb78FAvXxH6d-QmM3GfcwXaiq4")

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(
        message,
        """
        Hola, soy tu primer bot, estos son los comandos disponibles:
        \n /count - contar palabras o caracteres de un texto
        \n /start - mensaje de bienvenida
        """,
    )

@bot.message_handler(commands=["count"])
def count(message):
    board = ReplyKeyboardMarkup(
        row_width=2, resize_keyboard=True, one_time_keyboard=True
    )
    board.add(KeyboardButton("Contar palabras"), KeyboardButton("Contar caracteres"))
    bot.send_message(message.chat.id, "Elige qué quieres contar:", reply_markup=board)
    bot.register_next_step_handler(message, handle_count_choice)

def handle_count_choice(message):
    if message.text.lower() == "contar palabras":
        bot.send_message(
            message.chat.id, "Envía el texto del que deseas contar palabras"
        )
        bot.register_next_step_handler(message, count_words)
    elif message.text.lower() == "contar caracteres":
        bot.send_message(
            message.chat.id, "Envía el texto del que deseas contar caracteres"
        )
        bot.register_next_step_handler(message, count_characters)

def count_words(message):
    words = message.text.split()
    word_count = len(words)
    bot.reply_to(message, f"El texto tiene {word_count} palabras")

def count_characters(message):
    char_count = len(message.text)
    bot.reply_to(message, f"El texto tiene {char_count} caracteres")

@bot.message_handler(content_types=["text"])
def hola(message):
    if message.text.lower() in ["hola", "hello", "hi"]:
        bot.send_message(
            message.chat.id,
            f"Hola {message.from_user.first_name}, ¿en qué te puedo ayudar?",
        )
    else:
        bot.send_message(
            message.chat.id,
            "Comando no encontrado. Por favor, usa /start para revisar los comandos disponibles",
        )

bot.polling()
