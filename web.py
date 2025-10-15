# web.py
# 🌐 Mini servidor web Flask para exibir status do bot

from flask import Flask
import threading

# cria o app Flask
app = Flask(__name__)

# variável global que receberá referência ao bot
bot_instance = None

@app.route('/')
def home():
    if bot_instance and bot_instance.is_ready():
        guilds_count = len(bot_instance.guilds)
        return f"""
        <h1>🤖 OimaBot</h1>
        <p>Status: Online ✅</p>
        <p>Servidores conectados: {guilds_count}</p>
        """
    else:
        return "<h1>🤖 OimaBot</h1><p>Status: Iniciando...</p>"

def run():
    app.run(host='0.0.0.0', port=8080)

def start_web(bot):
    global bot_instance
    bot_instance = bot
    thread = threading.Thread(target=run)
    thread.start()
