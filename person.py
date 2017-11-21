class Person:
	id_count = 0

	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.id = name+ str(Person.id_count)
		Person.id_count+=1

	def __str__(self):
		return "Name: " + self.name + ", age: " + str(self.age) + ", id: " + str(self.id)

	def __repr__(self):
		return "Name: " + self.name + ", age: " + str(self.age)

	def __eq__(self,person):
		return self.id == person.id

	def __ne__(self,person):
		return self.id != person.id

	def __hash__(self):
		return hash(self.id)
