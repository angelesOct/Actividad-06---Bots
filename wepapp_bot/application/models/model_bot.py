import config as config # importa el archivo config

db = config.db # crea un objeto db del objeto db creado en config

'''
Metodo para seleccionar todos los registros de la tabla persornas
'''
def select_tips():
    try:
        return db.select('tips') # Selecciona todos los registros de la tabla personas
    except Exception as e:
        print "Model select_tips Error {}".format(e.args)
        print "Model select_tips Message {}".format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el nombre dado
'''
def select_tip(tip):
    try:
        return db.select('tips',where='tip_de=$tip', vars=locals())[0] # selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_tip Error {}".format(e.args)
        print "Model select_tip Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro usando los datos de las tablas
'''
def insert_tip(tip_de, tip, tiempo):
    try:
        return db.insert('tips', tip_de=tip_de, tip=tip, tiempo=tiempo) # inserta un registro en personas
    except Exception as e:
        print "Model insert_tip Error {}".format(e.args)
        print "Model insert_tip Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el nombre recibido
'''
def delete_tip(tip):
    try:
        return db.delete('tips', where='tip_de=$tip',vars=locals()) # borra un registro de personas
    except Exception as e:
        print "Model delete_tip Error {}".format(e.args)
        print "Model delete_tip Message {}".format(e.message)
        return None

'''
Metodo para actualizar los datos, del nombre recibido
'''
def update_tip(tip_de, tip, tiempo): # actualiza el email de personas que coincidan con el nombre
    try:
        return db.update('tips',
            tip=tip,
            tiempo=tiempo,
            where='tip_de=$tip_de',
            vars=locals())
    except Exception as e:
        print "Model update_tip Error {}".format(e.args)
        print "Model update_tip Message {}".format(e.message)
        return None
