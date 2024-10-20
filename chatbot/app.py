from flask import Flask
import threading
from bot import main as telegram_bot

app = Flask(__name__)

@app.route('/index.html')
def home():
    return "¡Aplicación Flask corriendo!"

# Iniciar el bot de Telegram en un hilo separado
def run_bot():
    import asyncio
    asyncio.run(telegram_bot())

if __name__ == "__main__":
    # Ejecutar el bot en un hilo
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

    # Iniciar la aplicación Flask
    app.run(debug=True)
