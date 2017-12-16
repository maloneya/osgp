class Person:
	def __init__(self,name,age,owner_location):
		self.name = name
		self.age = age
		self.owner_location = owner_location
		self.posts = []
		self.id = name+'@'+owner_location


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
