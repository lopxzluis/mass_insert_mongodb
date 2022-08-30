from faker import Faker
fake = Faker()

class documento:
	def __init__(self):
		pass

	def datos_faker():
		
		usuario = {
			"nombre" : fake.name(),
			"edad" : fake.random_int(0, 100),
			"email": fake.email(),
			"pais": fake.country(),
			"text": fake.text(),
			"Numero telefonico": fake.phone_number()
		}
		
		return usuario

