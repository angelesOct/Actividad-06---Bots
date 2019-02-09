import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return config.render.insert() # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input() # almacena los datos del formulario
        tip_de = formulario['tip_de'] # alamcena el nombre escrito en el input
        tip = formulario['tip']
        tiempo = formulario['tiempo']
        config.model_bot.insert_tip(tip_de, tip, tiempo) # llama al metodo insert_datos y le paso los datos guardados
        raise web.seeother('/') # redirecciona al index.html
