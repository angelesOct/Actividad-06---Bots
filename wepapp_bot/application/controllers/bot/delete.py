import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, nombre): 
        tips = config.model_bot.select_tip(nombre) # Selecciona el registro que coincida con nombre
        return config.render.delete(tips) # Envia el registro y renderiza delete.html
    
    def POST(self, nombre):
        formulario = web.input() # Crea un objeto formuario con los datos enviados con el formulario
        nombre = formulario['tip_de'] # Obtine el nombre almacenado en el formulario
        config.model_bot.delete_tip(nombre) # Borra el registro del nombre seleccionado
        raise web.seeother('/') # Redirecciona a raiz
