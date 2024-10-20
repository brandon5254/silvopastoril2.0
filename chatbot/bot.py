import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
import random

bot = telebot.TeleBot("7996201736:AAEwdMHRSCb78FAvXxH6d-QmM3GfcwXaiq4")

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(
        message,
       """
        ¡Hola! Bienvenido a nuestra plataforma tecnológica para la gestión eficiente de sistemas silvopastoriles.
        
        Estos son los comandos disponibles para ayudarte a mejorar la sostenibilidad de tu producción:
        \n /count - Contar palabras o caracteres de un texto
        \n /start - Ver este mensaje de bienvenida
        \n /sensor_data - Recibir datos en tiempo real de tus sensores IoT
        \n /optimize - Consejos de optimización basados en inteligencia artificial para tu producción ganadera
        \n /visualize - Ver visualizaciones interactivas de tus datos de suelo, vegetación y animales
        
        Estamos aquí para ayudarte a incrementar la productividad y preservar el medio ambiente. 🌱🐄
        """
    )


@bot.message_handler(commands=["sensor_data"])
def get_sensor_data(message):
    # Datos simulados (simulación de sensores IoT)
    ciudad = "Cali"
    temperatura = round(random.uniform(20.0, 35.0), 1)  # Temperatura aleatoria entre 20 y 35 grados Celsius
    humedad = random.randint(40, 100)  # Humedad aleatoria entre 40% y 100%
    velocidad_viento = round(random.uniform(0.0, 10.0), 1)  # Velocidad del viento aleatoria entre 0 y 10 m/s
    descripcion = "Cielo parcialmente nublado"

    # Mensaje de respuesta con los datos simulados
    respuesta = (
        f"🌤 Datos en tiempo real del clima en {ciudad} (Simulación):\n\n"
        f"🌡️ Temperatura: {temperatura}°C\n"
        f"💧 Humedad: {humedad}%\n"
        f"🌬️ Velocidad del viento: {velocidad_viento} m/s\n"
        f"☁️ Condición: {descripcion}\n"
    )

    bot.reply_to(message, respuesta)


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
