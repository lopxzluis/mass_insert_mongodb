from ejemplo_faker import Usuario_faker
from config import usuarios
def mass_insert(numero):
	success = {}
	failure = 0
	for x in range(numero):
		try:
			usuario_faker = Usuario_faker()
			result = usuarios.insert_one(usuario_faker.usuario)
			success[result.inserted_id]= True		
		except Exception as e: 
			print(e)
			failure += 1
	return "Datos agredados exitosamente: {}. Fallos de insersion: {}".format(len(success), failure)