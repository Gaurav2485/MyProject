class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

	def get_temperature(self):
		return self._temperature

	def set_temperature(self, value):
		if value < -273:
			raise ValueError("Temperature below -273 is not possible")
		self._temperature = value

  	 def to_fahrenheit(self):
       return (self._temperature * 1.8) + 32

man = Celsius()
man._temperature = 37
print(man._temperature)
print(man.to_fahrenheit())