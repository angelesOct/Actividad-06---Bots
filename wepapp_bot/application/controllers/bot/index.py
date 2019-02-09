import web
import config as config


class Index:
    def __init__(self):
        pass

    def GET(self):  
        nombre = config.model_bot.select_tips().list() # Selecciona todos los registros de personas
        return config.render.index(nombre) # Envia todos los registros y renderiza index.html
