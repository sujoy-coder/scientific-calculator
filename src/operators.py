# list of all operators
all_operators = ['+','-','*','/','log','ln','P','C','!','^','sin','cos','tan','%','(',')','asin','acos','atan','X','sqrt','um','exp']

# operators with type of operation
unary_operator = ['log','ln','%','!','sin','cos','tan','asin','acos','atan','sqrt','um','exp']
binary_operator = ['+','-','*','/','P','C','^','X']

# operators with corresponding precedance
operators_with_precedance_one = ['+','-']
operators_with_precedance_two = ['*','X','/']
operators_with_precedance_three = ['^','P','C']
operators_with_precedance_four = ['um']
operators_with_precedance_five = ['log','ln','%','!','sin','cos','tan','asin','acos','atan','sqrt','exp']

# list of all constant terms ['e' is elemeniated]
constant_terms = ['pi']

# error type list
errors = ['Syntax Error','Math Error','Wrong Input']