import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, nombre): 
        persona = config.model_bot.select_tip(nombre) # Selecciona el registro que coincida con nombre
        return config.render.update(persona) # Envia el registro y renderiza update.html
    
    def POST(self, email):
        formulario = web.input() # almacena los datos del formulario web
        tip_de = formulario['tip_de'] # alamcena el nombre escrito en el input
        tip = formulario['tip']
        tiempo = formulario['tiempo']
        config.model_bot.update_tip(tip_de, tip, tiempo) # actuliza los valores
        raise web.seeother('/') # redirecciona al index
