from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging 
import web

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Database connection
db = web.database(
    dbn = 'mysql',
    host = 'localhost',
    db = 'bot',
    user = 'angiebot',
    pw = 'angiebot.2019',
    port = 3306
    )

#beautyByAngie_bot
token = '675117576:AAE88bs3wNH8FybiV_tGkPiTT3xWtM9R9kc' 
lista = []

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    username = update.message.from_user.username #Almacena el nombre de usuario
    nombres = db.select('tips', what='tip_de')
    for i in nombres:
        print "Send nombre_tip to {}".format(username)
        lista.append(i)
    update.message.reply_text('Hola {} este bot te dara tips de belleza!! Usa el comando /tip_de \n seguido de la opcion que elijas... \n los tips son los siguientes\n'.format(username))
    update.message.reply_text(lista)

def help(bot, update):
    username = update.message.from_user.username
    nombres = db.select('tips', what='tip_de')
    for i in nombres:
        print "Send nombre_tip to {}".format(username)
        lista.append(i)
    update.message.reply_text('Hola {} este bot te dara tips de belleza!! Usa el comando /tip_de \n seguido de la opcion que elijas... \n los tips son los siguientes\n'.format(username))
    update.message.reply_text(lista)

def search(update):
    text = update.message.text.split()
    username = update.message.from_user.username
    try:
        tips = (text[1])
        print "Send tip_de to {}".format(username)
        print "Key search {}".format(tips)
        result = db.select('tips', where='tip_de=$tips', vars=locals())[0]
        print result
        respuesta =  str(result.tip) + ",\n " + str(result.tiempo)
        #response = "Sending Info " + str(result[0]) + ", " + str(result[1]) + ", " + str(result[2])
        #print response
        update.message.reply_text('Hola {}\n Aqui esta la informaion que desea:\n{}'.format(username, respuesta))
    except Exception as e:
        print "Error: "
        print "Error 2 {}".format(e.args)
        update.message.reply_text('El comando {} es incorreto'.format(tips))

def tip_de(bot, update):
    search(update)

def echo(bot, update):
    update.message.reply_text(update.message.text)
    print update.message.text
    print update.message.date
    print update.message.from_user
    print update.message.from_user.username
    
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

    
def main():
    try:
        print 'Angie init token'
        
        updater = Updater(token) #Llamar al token para poder establecer conexion

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        print 'Angie init dispatcher'

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("tip_de", tip_de))        

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, echo))

        # log all errors
        dp.add_error_handler(error)

        # Start the Bot
        updater.start_polling()

        # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        print 'Angie ready'
        updater.idle()
    except Exception as e:
        print "Error 100: ", e.message

if __name__ == '__main__':
    main()
