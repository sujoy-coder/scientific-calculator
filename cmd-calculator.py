from src.operators import errors
from src.solver import Solver

# it store all the previous valid answers till app is running...
valid_answer_previous = 0

def helper():
	print('Available Math Functions :')
	print('1. asin(x) --> returns the sin inverse of x')
	print('2. acos(x) --> returns the cos inverse of x')
	print('3. atan(x) --> returns the tan inverse of x')
	print('4. 5P2 --> returns permudations results of 5P2 i.e. 20')
	print('5. 5C2 --> returns combinations results of 5C2 i.e. 10')
	print('6. x! --> returns the factorial of x')
	print('7. sqrt(x) --> returns squre root value of x')
	print('8. sin(x) --> returns sin of angle x where x is in degrees')
	print('9. cos(x) --> returns cos of angle x where x is in degrees')
	print('10. tan(x) --> returns tan of angle x where x is in degrees')
	print('11. x% --> returns percentage of x in fraction value')
	print('12. log(x) --> returns logarithm value of x with base 10')
	print('12. ln(x) --> returns logarithm value of x with base e=2.71828182 i.e. natural log')
	print('13. x^(y) --> returns the value of x to power y')
	print('14. \'+\' --> it is used for addition of numbers')
	print('15. \'-\' --> it is used for subtraction of numbers')
	print('16. \'*\' or \'X\' --> it is used for multiplication of numbers')
	print('16. \'/\' --> it is used for dividation of numbers')
	print('17. exp(x) --> returns Exponential of x')
	print('*** NOTE :')
	print('1. constant terms ==> \'pi\' value is = 3.141592')
	print('2. use \'(\' and \')\' brackets only for complex expression')
	print('3. use command \'ans\' to get the previous answer')
	print('')
	
def isFloat(num):
    try:
        num = float(num)
        if num%1 == 0.0:
            return False
        else:
            return True
    except:
        return False

def integer_modification(num):
    ''' when the integer length is grater than 10 then this method modify that large
        integer into a 10-12 digits integer
    type(num) --> str | e.g. = '213.0'
    '''
    int_num = int(float(num))
    length = len(str(int_num))
    if(length<=10):
    	num = int_num
    	return num
    else:
        if int_num > 0:
            fraction_num = int_num/(10**(length-1))
            fraction_num = round(fraction_num,10)
            num = f'{fraction_num}e+{length-1}'
        else:
            fraction_num = int_num/(10**(length-2))
            fraction_num = round(fraction_num,10)
            num = f'{fraction_num}e+{length-2}'
        return num

def run_calculator_in_command_line():
	print('--------- ** Run A Scientific Calculator Using Command Line ** ---------')
	print('** Enter the command "-h" or "help" to show available calculator functions...\n')
	problem = Solver()
	global valid_answer_previous
	while True:
		infix = input('---> ')
		if infix in ['exit','quit']:
			break
		elif infix == 'ans':
			print(valid_answer_previous)
		elif infix in ["help","-h"]:
			helper()
		else:
			try:
				temp_ans = problem.solve(infix)
				if temp_ans in errors:
					print(temp_ans)
				else:
					if isFloat(temp_ans):
						temp_ans = float(temp_ans)
					else:
						temp_ans = integer_modification(temp_ans)
					valid_answer_previous = temp_ans
					print(temp_ans)
			except:
				print('Wrong Input')
                #print('')

if __name__ == '__main__':
	run_calculator_in_command_line()

