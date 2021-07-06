def class segment:
	def __init__(self,pin0,pin1,pin2,pin3,pin4,pin5,pin6,startVal = 0):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(pin0,GPIO.OUT)
		GPIO.setup(pin1,GPIO.OUT)
		GPIO.setup(pin2,GPIO.OUT)
		GPIO.setup(pin3,GPIO.OUT)
		GPIO.setup(pin4,GPIO.OUT)
		GPIO.setup(pin5,GPIO.OUT)
		GPIO.setup(pin6,GPIO.OUT)
		self.a = pin0
		self.b = pin1
		self.c = pin2
		self.d = pin3
		self.e = pin4
		self.f = pin5
		self.g = pin6
		self.segmentVal = startVal
		
	def countup():
		self.segmentVal = self.segmentVal + 1 
		if self.segmentVal == 10:
			self.segmentVal = 0
		self.Display(self.segmentVal)
		
	def countdown():
		self.segmentVal = self.segmentVal - 1 
		if self.segmentVal == -1:
			self.segmentVal = 9
		self.Display(self.segmentVal)
		
	def Display(self,count):
		if count == 0:
			self.__zero()
		elif count == 1:
			self.__one()
		elif count == 2:
			self.__two()
		elif count == 3:
			self.__three()
		elif count == 4:
			self.__four()
		elif count == 5:
			self.__five()
		elif count == 6:
			self.__six()
		elif count == 7:
			self.__seven()
		elif count == 8:
			self.__eight()
		elif count == 9:
			self.__nine()
		
	def __zero(slef):
		GPIO.output(self.a,GPIO.HIGH)
		GPIO.output(self.b,GPIO.HIGH)
		GPIO.output(self.c,GPIO.HIGH)
		GPIO.output(self.d,GPIO.HIGH)
		GPIO.output(self.e,GPIO.HIGH)
		GPIO.output(self.f,GPIO.HIGH)
		GPIO.output(self.g,GPIO.LOW)
		
	def __one(self):
		GPIO.output(self.a,GPIO.LOW)
		GPIO.output(self.b,GPIO.HIGH)
		GPIO.output(self.c,GPIO.HIGH)
		GPIO.output(self.d,GPIO.LOW)
		GPIO.output(self.e,GPIO.LOW)
		GPIO.output(self.f,GPIO.LOW)
		GPIO.output(self.g,GPIO.LOW)
		
	def __two(self):
		GPIO.output(self.a,GPIO.HIGH)
		GPIO.output(self.b,GPIO.LOW)
		GPIO.output(self.c,GPIO.HIGH)
		GPIO.output(self.d,GPIO.HIGH)
		GPIO.output(self.e,GPIO.LOW)
		GPIO.output(self.f,GPIO.HIGH)
		GPIO.output(self.g,GPIO.HIGH)
		
	def __three(self):
		GPIO.output(self.a,GPIO.HIGH)
		GPIO.output(self.b,GPIO.HIGH)
		GPIO.output(self.c,GPIO.HIGH)
		GPIO.output(self.d,GPIO.HIGH)
		GPIO.output(self.e,GPIO.LOW)
		GPIO.output(self.f,GPIO.LOW)
		GPIO.output(self.g,GPIO.HIGH)
		
	def __four(self):
		GPIO.output(self.a,GPIO.LOW)
		GPIO.output(self.b,GPIO.HIGH)
		GPIO.output(self.c,GPIO.HIGH)
		GPIO.output(self.d,GPIO.LOW)
		GPIO.output(self.e,GPIO.LOW)
		GPIO.output(self.f,GPIO.HIGH)
		GPIO.output(self.g,GPIO.HIGH)
		
		
	def __five(self):
		GPIO.output(self.a,GPIO.HIGH)
		GPIO.output(self.b,GPIO.LOW)
		GPIO.output(self.c,GPIO.HIGH)
		GPIO.output(self.d,GPIO.HIGH)
		GPIO.output(self.e,GPIO.LOW)
		GPIO.output(self.f,GPIO.HIGH)
		GPIO.output(self.g,GPIO.HIGH)
		
	def __six(self):
		GPIO.output(self.a,GPIO.HIGH)
		GPIO.output(self.b,GPIO.LOW)
		GPIO.output(self.c,GPIO.HIGH)
		GPIO.output(self.d,GPIO.HIGH)
		GPIO.output(self.e,GPIO.HIGH)
		GPIO.output(self.f,GPIO.HIGH)
		GPIO.output(self.g,GPIO.HIGH)
		
		
	def __ssven(self):
		GPIO.output(self.a,GPIO.HIGH)
		GPIO.output(self.b,GPIO.HIGH)
		GPIO.output(self.c,GPIO.HIGH)
		GPIO.output(self.d,GPIO.LOW)
		GPIO.output(self.e,GPIO.LOW)
		GPIO.output(self.f,GPIO.LOW)
		GPIO.output(self.g,GPIO.LOW)
	
	
	def __eight(self):
		GPIO.output(self.a,GPIO.HIGH)
		GPIO.output(self.b,GPIO.HIGH)
		GPIO.output(self.c,GPIO.HIGH)
		GPIO.output(self.d,GPIO.HIGH)
		GPIO.output(self.e,GPIO.HIGH)
		GPIO.output(self.f,GPIO.HIGH)
		GPIO.output(self.g,GPIO.HIGH)
		
	def __nine(self):
		GPIO.output(self.a,GPIO.HIGH)
		GPIO.output(self.b,GPIO.HIGH)
		GPIO.output(self.c,GPIO.HIGH)
		GPIO.output(self.d,GPIO.LOW)
		GPIO.output(self.e,GPIO.LOW)
		GPIO.output(self.f,GPIO.HIGH)
		GPIO.output(self.g,GPIO.HIGH)
		
