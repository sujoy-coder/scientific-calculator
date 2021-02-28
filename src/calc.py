from math import radians,pi,e,degrees
import math

class Calc:
	''' operation starts from Left to Right side, according to the given arguments '''
	def __init__(self, *args):
		self.ans = 0
		self.pi_ = pi
		self.e_ = e 

	@staticmethod
	def isFloat(num):
	    try:
	        num = float(num)
	        if num%1 == 0.0:
	            return False
	        else:
	            return True
	    except:
	        return False

	def add(self, *args):
		try:
			res = 0
			for x in list(map(float, args)):
				res += x
			self.ans = res
			return self.ans
		except Exception as e:
			return 'Syntax Error'

	def sub(self, *args):
		try:
			flag = True
			res = 0
			for x in list(map(float, args)):
				if flag:
					flag = False
					res = x
					continue
				res -= x
			self.ans = res
			return self.ans
		except Exception as e:
			return 'Syntax Error'

	def mul(self, *args):
		try:
			res = 1
			for x in list(map(float, args)):
				res *= x
			self.ans = res
			return self.ans
		except Exception as e:
			return 'Syntax Error'

	def div(self, x= None, y= None, *args):
		''' this method takes only 2 arguments and returns their dividal result... '''
		try:
			x = float(x)
			y = float(y)
			res = x / y
			self.ans = res 
			return self.ans
		except Exception as e:
			return 'Math Error'

	def fact(self, x= None, *args):
		try:
			if Calc.isFloat(x):
				return 'Math Error'
			else:
				x = int(float(x))
				res = 1
				if x < 0:
					return 'Math Error'
				elif x == 0:
					self.ans = res 
					return self.ans
				for i in range(1,x+1):
					res *= i
				self.ans = res 
				return self.ans
		except Exception as e:
			return 'Math Error'

	def power(self, x= None, y= None, *args):
		try:
			x = float(x)
			y = float(y)
			res = x**y
			self.ans = res 
			return self.ans
		except Exception as e:
			return 'Syntax Error'

	def perm_(self, n= None, r= None, *args):
		''' Formula : nPr = n! / (n-r)! '''
		try:
			if Calc.isFloat(n) or Calc.isFloat(r):
				return 'Math Error'
			else:
				res = self.fact(n)/self.fact(int(float(n))-int(float(r)))
				self.ans = res
				return self.ans
		except Exception as e:
			return 'Syntax Error'

	def comb_(self, n= None, r= None, *args):
		''' Formula : nCr = n! / (r! * (n-r)!) '''
		try:
			if Calc.isFloat(n) or Calc.isFloat(r):
				return 'Math Error'
			else:
				res = self.fact(n)/(self.fact(int(float(n))-int(float(r))) * self.fact(r))
				self.ans = res
				return self.ans
		except Exception as e:
			return 'Syntax Error'

	def log_(self, x= None, *args):
		''' Log with base 10'''
		try:
			x = float(x)
			self.ans = math.log10(x)
			return self.ans
		except Exception as e:
			return 'Math Error'

	def ln_(self, x= None, *args):
		''' Log with base e'''
		try:
			x = float(x)
			self.ans = math.log(x)
			return self.ans
		except Exception as e:
			return 'Math Error'

	def sin_(self, x= None, *args):
		try:
			x = float(x)
			self.ans = math.sin(radians(x))
			return self.ans
		except Exception as e:
			return 'Math Error'

	def cos_(self, x= None, *args):
		try:
			x = float(x)
			self.ans = math.cos(radians(x))
			return self.ans
		except Exception as e:
			return 'Math Error'

	def tan_(self, x= None, *args):
		try:
			x = float(x)
			self.ans = math.tan(radians(x))
			return self.ans
		except Exception as e:
			return 'Math Error'

	def per_(self, x= None, *args):
		try:
			x = float(x)
			self.ans = x/100
			return self.ans
		except Exception as e:
			return 'Syntax Error'

	def asin_(self, x= None, *args):
		try:
			x = float(x)
			self.ans = degrees(math.asin(x))
			return self.ans
		except Exception as e:
			return 'Math Error'

	def acos_(self, x= None, *args):
		try:
			x = float(x)
			self.ans = degrees(math.acos(x))
			return self.ans
		except Exception as e:
			return 'Math Error'

	def atan_(self, x= None, *args):
		try:
			x = float(x)
			self.ans = degrees(math.atan(x))
			return self.ans
		except Exception as e:
			return 'Math Error'

	def sqrt_(self, x= None, *args):
		try:
			x = float(x)
			self.ans = math.sqrt(x)
			return self.ans
		except Exception as e:
			return 'Math Error'

	def unary_minus(self, x= None, *args):
		try:
			x = float(x)
			self.ans = (-1)*x
			return self.ans
		except Exception as e:
			return 'Math Error'

	def exp_(self, x= None, *args):
		try:
			x = float(x)
			self.ans = self.e_**x 
			return self.ans
		except Exception as e:
			return 'Syntax Error'


