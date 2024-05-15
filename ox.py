import random
import telebot
import time
from datetime import datetime, timedelta
import pytz

# Defina o fuso horário para Brasília
timezone = pytz.timezone('America/Sao_Paulo')

token = 'SEU_TOKEN'
token = '6109226718:AAHsI7CYGCg_V-uKfCk1v7QrLb90-A75W-Y'
chat_id = '-1002041997124'
bot = telebot.TeleBot(token)

while True:
    try:
        nu1 = random.randrange(2, 9)
        nu2 = random.randrange(2, 9)
        # Obtém a hora atual em Brasília
        current_time = datetime.now(timezone)

        # Adiciona 3 minutos ao tempo atual
        expiration_time = current_time + timedelta(minutes=3)

        # Formata a hora como uma string legível
        expiration_time_str = expiration_time.strftime('%H:%M')

        # Nomes dos jogos
        nomes_jogos = ["Fortune Tiger", "Ox", "Mouse", "Rabbit", "Dragon"]
        emojis_jogos = ["🐯", "🐀", "🐂", "🐇", "🐉"]

        entrada = f'''🟤💰 Entrada Fortune Tiger Confirmada! 💰🟤

{emojis_jogos[2]}<a href="https://mundialsbet.com/casino/pgsoft/fortune-ox">{nomes_jogos[1]}</a>
🕑 <b>Válido até:</b> {expiration_time_str} 
👉 <b>{nu1}x Normal</b>
⚡️ <b>{nu2}x Turbo</b>
🚥 <b>Intercalando</b>

🔗<a href="https://mundialsbet.com"><b>Cadastre-se Aqui!!</b></a>
'''
        finalizada = f'''🟫🔹 <b>Entrada Finalizada</b> 🔹🟫
            ✅🤎 GREEN! 🤎✅'''

        bot.send_message(chat_id=chat_id, text=entrada, parse_mode='HTML', disable_web_page_preview=True)
        time.sleep(300)
        bot.send_message(chat_id=chat_id, text=finalizada, parse_mode='HTML', disable_web_page_preview=True)
        time.sleep(300)
        print('Sinal Enviado THE DOG HOUSE')
        print('GREEN Enviado THE DOG HOUSE')

    except Exception as e:
        print(f'Ocorreu um erro: {e}')
        print('Reiniciando o código...')
        time.sleep(10)
        continue
