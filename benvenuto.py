import logging
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Configura il logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)
logger = logging.getLogger(__name__)

WELCOME_CHAT_ID = -1002252785163

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    logger.info(f"Evento NEW_CHAT_MEMBERS ricevuto in chat: {chat_id}")

    # Per ogni nuovo membro che si unisce, invia il messaggio di benvenuto
    for new_member in update.message.new_chat_members:
        user_mention = f"<a href='tg://user?id={new_member.id}'>{new_member.first_name}</a>"
        welcome_text = (
            f"🎉 Benvenutə nella squadra, {user_mention}! un caloroso benvenuto sia da me che dai Mod 🐒🌟\n\n"
            "Grazie per esserti abbonatə al canale! 💜\n"
            "Buona permanenza,\n"
            "⚠️⚠️mi raccomando RISPETTO, rispettate sempre la privacy degli altri e non siate invadenti.\n"
            "Se ci fosse qualcosa di indesiderato siete pregati di contattarmi in privato e avvisare, prenderemo provvedimenti "
            "(idem per chi non rispetta le regole citate) ⚠️⚠️\n"
            "Buon divertimento Giuggiolaaaa 🎮✨"
        )
        await update.message.reply_text(text=welcome_text, parse_mode=ParseMode.HTML)

def main():
    bot_token = "7754195180:AAH8AwXhdEVKkAy9Pa6lBz7buB7-zr2n-u8"  # Sostituisci con il token del tuo bot
    application = ApplicationBuilder().token(bot_token).build()

    # Aggiunge l'handler per gli eventi NEW_CHAT_MEMBERS
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    
    # Avvia il bot in modalità polling
    application.run_polling()

if __name__ == '__main__':
    main()