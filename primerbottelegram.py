import telebot as tl
from config import *

bot = tl.TeleBot(TOKEN)

@bot.message_handler(commands=["start","help","ayuda"])
def cmd_start(message):
    bot.reply_to(message,"Hola Mundo")
@bot.message_handler(commands=["saluda"])
def cmd_saluda(message):
    if message.chat.id == 824356451:
    #if message.chat.name == "Abraham"
        bot.reply_to(message,"Hola"+str(message))

@bot.message_handler(commands=["documento"])
def cmd_documento(message):
    documento = open("CursosIntersemestrales2023_1_v3.docx","rb")
    bot.send_document(message.chat.id,documento,caption="archivo resultados")


@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    if message.text and message.text.startswith("/"):
        bot.send_message(message.chat.id,"Ese comando no esta disponible")
    else:
        bot.send_message(message.chat.id,"Contestando mensaje de texto")
    # texto con formato html
    
    texto_html = "<b>Negritas</b>"
    bot.send_message(message.chat.id,texto_html,parse_mode="html")

    # texto con formato markdown
    
    texto_markdown = "[Enlace](https://proteco.fi-b.unam.mx/)"
    texto_markdown = "[Enlace](https://www.youtube.com/watch?v=Zxk1Jpq_8fk&list=RDZxk1Jpq_8fk&start_radio=1&ab_channel=meena%E2%99%A1)"
    
    bot.send_message(message.chat.id,texto_markdown,parse_mode="MarkdownV2",disable_web_page_preview=True)
    
    
@bot.message_handler(content_types=["photo"])
def bot_mensajes_fotos(message):
    bot.send_message(message.chat.id,str(message))
    foto = open("junta.jpg","rb")
    bot.send_photo(message.chat.id,foto,"resulta")
    


    

if __name__ == "__main__":
    
    bot.set_my_commands([tl.types.BotCommand("start","Hola mundo"),tl.types.BotCommand("documento","devuelve un documento con los resultados"),tl.types.BotCommand("saluda","Te saluda")])
    print("Iniciando bot")
    bot.infinity_polling()
    print("Fin")


