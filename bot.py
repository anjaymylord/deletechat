from telegram import Update
from telegram.ext import Updater, CommandHandler
import re

# Fungsi yang akan dipanggil saat perintah /start diberikan
def start(update: Update, context):
    update.message.reply_text('Halo! Saya adalah bot penghapus pesan di grup Telegram.')

# Fungsi yang akan dipanggil saat perintah /hapus diberikan
def hapus(update: Update, context):
    # Mendapatkan id grup
    chat_id = update.message.chat_id

    # Menghapus pesan dari message ID 6881 hingga 6890
    start_message_id = 
    end_message_id = 

    for message_id in range(start_message_id, end_message_id + 1):
        context.bot.delete_message(chat_id=chat_id, message_id=message_id)

# Fungsi utama
def main():
    # Konfigurasi updater
    updater = Updater('6301743167:AAFvcEHznXoz8dzH9SQD4nEZMGdJ-N_v5uU', use_context=True)

    # Mendapatkan objek dispatcher dari updater
    dp = updater.dispatcher

    # Menambahkan handler untuk perintah /start
    dp.add_handler(CommandHandler("start", start))

    # Menambahkan handler untuk perintah /hapus
    dp.add_handler(CommandHandler("hapus", hapus))

    # Memulai bot
    updater.start_polling()

    # Menjalankan bot sampai pengguna menekan Ctrl-C
    updater.idle()

# Memanggil fungsi utama
if __name__ == '__main__':
    main()
