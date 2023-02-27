import telebot as tl
bot = tl.TeleBot("5882179085:AAEAQdAbeQib9QDZg6fmV4gbzpCWaFWWNqw")
# para ello usaremos primero el comando /start
# para esto se usan decoradores, que son funciones que reciben funciones y devuelven funciones

# este decorador tienen como argumento commands
@bot.message_handler(commands=["start","ayuda","help"]) 
#definimos los comandos que se crearan
def cmd_start(message):
    """Da la bienvenida al usuario del bot"""
    bot.reply_to(message,"Hola Mundo")
@bot.message_handler(commands=["saluda"]) 
#definimos los comandos que se crearan
def cmd_start(message):
    """Da la bienvenida al usuario del bot"""
    bot.reply_to(message,"Esto es un saludo")
    
    


#enviar foto

@bot.message_handler(commands=["foto"]) 
#definimos los comandos que se crearan
def enviar_foto(message):
    """Da la bienvenida al usuario del bot"""
    foto = open("junta.jpg","rb")
    bot.send_photo(message.chat.id,foto,"resultado") 
    
#enviar archivo


@bot.message_handler(commands=["archivo"]) 
#definimos los comandos que se crearan
def enviar_foto(message):
    """Da la bienvenida al usuario del bot"""
    archivo = open("CursosIntersemestrales2023_1_v3.docx","rb")
    # escribiendo
    bot.send_chat_action(message.chat.id,"typing")
    bot.send_document(message.chat.id,archivo,caption="archivo") 


    
        
@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    """gestionar mensajes de texto definidos"""
    if message.text.startswith("/"):
        bot.send_message(message.chat.id,"Comando no disponible")
    else:
        bot.send_message(message.chat.id,"Contestando mensaje")
## texto con formato, html o markdown
    texto_html ='<b>NEGRITA</b>'+'\n'
    texto_html+='<i>CURSIVA</i>'+'\n'
    texto_html+='<U>SUBRAYADO</U>'+'\n'
    texto_html+='<S>TACHADO</S>'+'\n'   
    bot.send_message(message.chat.id,texto_html,parse_mode = "html")#,disable_web_page_preview=True
           
    texto_markdown ='*NEGRITA*'+'\n'
    texto_markdown+='_CURSIVA_'+'\n'
    texto_markdown+='__SUBRAYADO__'+'\n'
    texto_markdown+='~TACHADO~'+'\n'
    texto_markdown+='[Enlace](https://proteco.fi-b.unam.mx/)'+'\n'
    bot.send_message(message.chat.id,texto_markdown,parse_mode = "MarkdownV2",disable_web_page_preview=False)#,disable_web_page_preview=True
    

# #enviar foto

# @bot.message_handler(commands=["foto"]) 
# #definimos los comandos que se crearan
# def enviar_foto(message):
#     """Da la bienvenida al usuario del bot"""
#     foto = open("junta.jpg","rb")
#     bot.send_photo(message.chat.id,foto,"resultado") 
    
# #enviar archivo


# @bot.message_handler(commands=["archivo"]) 
# #definimos los comandos que se crearan
# def enviar_foto(message):
#     """Da la bienvenida al usuario del bot"""
#     foto = open("CursosIntersemestrales2023_1_v3.docx","rb")
#     bot.send_photo(message.chat.id,foto,caption="archivo") 
    
#enviar archivo



# ver comandos



   

if __name__ == '__main__':
    bot.set_my_commands([tl.types.BotCommand("start","hola mundo"),tl.types.BotCommand("archivo","manda un archivo"),tl.types.BotCommand("foto","manda una foto")])
    print("Iniciando bot")
    bot.infinity_polling() # bucle que se pone en escucha de forma infinita
    print("fin")
    
    
