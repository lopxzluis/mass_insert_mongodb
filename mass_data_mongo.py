from ejemplo_faker import documento
from config import client, db, usuarios
def mass_insert(numero):
	success = {}
	failure = 0
	for x in range(numero):
		try:
			result = usuarios.insert_one(documento.datos_faker())
			success[result.inserted_id]= True		
		except Exception as e: 
			print(e)
			failure += 1
	return "Datos agredados exitosamente: {}. Fallos de insersion: {}".format(len(success), failure)