from collections import deque
from functools import reduce
from .operators import *
from .calc import Calc

class Solver(Calc):
	def __init__(self):
		self.postfix_list = []
		self.infix_list = []
		super().__init__()

	@staticmethod
	def precedence(op):
		if op in operators_with_precedance_one:
			return 1
		elif op in operators_with_precedance_two:
			return 2
		elif op in operators_with_precedance_three:
			return 3
		elif op in operators_with_precedance_four:
			return 4
		elif op in operators_with_precedance_five:
			return 5
		else:
			return -1

	def operator_mapping(self, operator= None, a= None, b= None, *args):
		# it should maps/returns --> ans = a (x) b | ans = (x) a --> type of ans is str()
		if operator == '+':
			self.ans = self.add(a,b)
		elif operator == '-':
			self.ans = self.sub(a,b)
		elif operator in ['*','X']:
			self.ans = self.mul(a,b)
		elif operator == '/':
			self.ans = self.div(a,b)
		elif operator == 'log':
			self.ans = self.log_(a)
		elif operator == 'ln':
			self.ans = self.ln_(a)
		elif operator == 'P':
			self.ans = self.perm_(a,b)
		elif operator == 'C':
			self.ans = self.comb_(a,b)
		elif operator == '!':
			self.ans = self.fact(a)
		elif operator == '^':
			self.ans = self.power(a,b)
		elif operator == 'sin':
			self.ans = self.sin_(a)
		elif operator == 'cos':
			self.ans = self.cos_(a)
		elif operator == 'tan':
			self.ans = self.tan_(a)
		elif operator == '%':
			self.ans = self.per_(a)
		elif operator == 'asin':
			self.ans = self.asin_(a)
		elif operator == 'acos':
			self.ans = self.acos_(a)
		elif operator == 'atan':
			self.ans = self.atan_(a)
		elif operator == 'sqrt':
			self.ans = self.sqrt_(a)
		elif operator == 'exp':
			self.ans = self.exp_(a)
		elif operator == 'um':
			self.ans = self.unary_minus(a)
		else:
			return 'Syntax Error'
		return str(self.ans)

	def constant_mapping(self, constant= None, *args):
		if constant == 'pi':
			return str(self.pi_)
		else:
			return 'Syntax Error'

	def get_infix_list(self, infix= None):
		''' split the string according to the all-operators List '''
		try:
		    temp_str = ''
		    for x in infix:
		        if x not in all_operators:
		            temp_str += x
		        else:
		            self.infix_list.append(temp_str)
		            self.infix_list.append(x)
		            temp_str = ''
		    if temp_str:
		        self.infix_list.append(temp_str)
		    # removing extra space in the expression the from list
		    while True:
		        try:
		            self.infix_list.remove('')
		        except:
		            break
		    return self.infix_list
		except Exception as e:
			return 'Syntax Error'

	def modify_infix_list(self):
		try:
			temp_stack = deque()
			if self.infix_list[0] == '-':
				self.infix_list[0] = 'um'
			# when get '(,-' in expression modify that here...
			for i in range(len(self.infix_list)):
				if len(temp_stack)>0 and self.infix_list[i]=='-' and temp_stack[-1]=='(':
					self.infix_list[i] = 'um'
					temp_stack.append(self.infix_list[i])
				else:
					temp_stack.append(self.infix_list[i])
			self.infix_list = list(temp_stack)
			return self.infix_list
		except Exception as e:
			return 'Syntax Error'

	def infix_to_postfix(self):
		'''  it converts infix_list to a postfix_list '''
		try:	
			stk = deque()
			for x in self.infix_list:
				if x in constant_terms:
					temp = self.constant_mapping(x)
					self.postfix_list.append(temp)
				elif x == '(':
					stk.append(x)
				elif x == ')':
					try:
						temp = stk.pop()
						while temp != '(':
							self.postfix_list.append(temp)
							temp = stk.pop()
					except:
						# return error due to missmatch of breakts '(' or ')'
						self.postfix_list.clear()
						self.postfix.append('Syntax Error')
						return self.postfix_list
				elif x in all_operators:
					while (len(stk) != 0) and (Solver.precedence(stk[-1]) >= Solver.precedence(x)):
						temp = stk.pop()
						self.postfix_list.append(temp)
					stk.append(x)
				else:
					self.postfix_list.append(x)
			while True:
				if len(stk) != 0:
					temp = stk.pop()
					# if temp is ( we append to postfix but to avoid it we can apply a cond.
					self.postfix_list.append(temp)
				else:
					break
			return self.postfix_list			
		except Exception as e:
			return 'Syntax Error'

	def evaluate_postfix_list(self):
		''' it evaluates the postfix list into final answer '''
		try:
			stk2 = deque()
			for x in self.postfix_list:
				if x in all_operators:
					if x in unary_operator:  
						a = stk2.pop()
						temp = self.operator_mapping(operator= x, a= a)
					elif x in binary_operator:
						b = stk2.pop()
						a = stk2.pop()
						temp = self.operator_mapping(operator= x, a= a, b= b)
					else:
						temp = 'Syntax Error'

					if temp in ['Syntax Error','Math Error']:
						return temp
					else:
						stk2.append(temp)
				else:
					stk2.append(x)
			# calculation of final answer with stk2 all element product()
			stk2 = map(float,stk2)
			self.ans = reduce(lambda r, t: r*t, stk2)
			return self.ans
		except Exception as e:
			#print(e)									# --> debug statement
			return 'Syntax Error'

	def solve(self, infix= None, *args):
		''' This is the method for interaction with user 
			inputs: infix_expression
			outputs: final_answer
		'''
		try:
			self.get_infix_list(infix= infix)
			self.modify_infix_list()
			self.infix_to_postfix()
			#print(self.infix_list,self.postfix_list)    # --> debug statement
			final_answer = self.evaluate_postfix_list()
			#print(self.infix_list,self.postfix_list)    # --> debug statement
			self.postfix_list.clear()
			self.infix_list.clear()
			return final_answer
		except Exception as e:
			# print(self.infix_list,self.postfix_list)  # --> debug statement
			self.postfix_list.clear()
			self.infix_list.clear()
			return 'Syntax Error'


