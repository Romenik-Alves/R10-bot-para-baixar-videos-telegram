import logging
from telegram import Update, ForceReply, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import requests

# Substitua 'YOUR_TOKEN_HERE' pelo token do seu bot
TOKEN = '7620885240:AAE5ZV18bnUqDHP63kapm3srNuEU7Sr###'

# Configuração de logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Função para iniciar o bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Olá! Envie um vídeo para baixá-lo.')

# Função para baixar o vídeo
async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await context.bot.get_file(update.message.video.file_id)
    file_url = file.file_path
    response = requests.get(file_url)
    file_name = update.message.video.file_name
    with open(file_name, 'wb') as f:
        f.write(response.content)
    await update.message.reply_text(f'Vídeo baixado como {file_name}')

# Inicializar o bot
application = ApplicationBuilder().token(TOKEN).build()

# Adicionar handlers
application.add_handler(CommandHandler('start', start))
application.add_handler(MessageHandler(filters.VIDEO, download_video))

# Iniciar o bot
application.run_polling()
