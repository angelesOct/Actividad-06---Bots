import web # importa la libreria web.py
import application.models.model_bot as model_bot # importa el modelo_personas 


render = web.template.render('application/views/bot/', base='master') # configura la ubicacion de las vistas