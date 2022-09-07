from faker import Faker
fake = Faker()

class Usuario_faker():
	def __init__(self):		
		self.usuario = {
				"nombre" : fake.name(),
				"edad" : fake.random_int(0, 100),
				"email": fake.email(),
		 		"pais": fake.country(),
				"text": fake.text(),
				"Numero telefonico": fake.phone_number()
			}
	def saludar_usuario(self):
		return "hola " + self.usuario["nombre"]
			
objeto = Usuario_faker()
