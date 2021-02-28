from src.operators import errors
from tkinter import messagebox
from src.solver import Solver
from tkinter import *
import tkinter

root = tkinter.Tk()
root.geometry("450x630+550+50")
root.resizable(True,True)
root.title("Scientific Calculator")
try:
    root.iconbitmap(r'./assets/icon_calc.ico')
except:
    pass

# global variables
errors_ = ['Syntax Error','Math Error','Wrong Input']
valid_answer_previous = 0
data = StringVar()
data.set('0')
temp_val = ''

lbl = Entry(
    root,
    text = "0",
    bd = 25,
    justify = "right",
    font = ("Verdana", 20),
    textvariable = data,
    background = "black", # skin color : #F9E79F
    fg = "white",        # black : #000000
)
lbl.pack(expand = True, fill = "both")
# ---------------for diabling the keybords keys--------------------
lbl.bind("<Key>", lambda e: "break")

# --------------nesseary methods---------------
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

def get_answer(expression):
    problem = Solver()
    try:
        temp_ans = problem.solve(expression)
        if temp_ans in errors:
            return str(temp_ans)
        else:
            global valid_answer_previous
            if isFloat(temp_ans):
                temp_ans = float(temp_ans)
            else:
                temp_ans = integer_modification(temp_ans)
            valid_answer_previous = temp_ans
            return str(temp_ans)
    except:
        return 'Wrong Input'

def btn_clicked(var):
	global temp_val
	temp_val += var
	data.set(temp_val)

def clear_screen():
	global temp_val
	temp_val = ''
	data.set(temp_val)

def calculate_result():
    expression = data.get()
    ans_ = get_answer(expression)
    if ans_ in errors_:
        messagebox.showerror("Error :", ans_)
        return
    else:
        global temp_val
        temp_val = ans_
        data.set(temp_val)

def show_previous_answer():
    global valid_answer_previous
    global temp_val
    previous_ans = valid_answer_previous
    temp_val =  str(previous_ans)
    data.set(temp_val)

def back_space():
    try:
        global temp_val
        expression = list(temp_val)
        expression.pop()
        temp_val = ''.join(expression)
        data.set(temp_val)
    except:
        pass


# --------------the frames section--------------------
btnrow1 = Frame(root)
btnrow1.pack(expand = True, fill = "both")

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")

btnrow5 = Frame(root)
btnrow5.pack(expand = True, fill = "both")

btnrow6 = Frame(root)
btnrow6.pack(expand = True, fill = "both")

btnrow7 = Frame(root)
btnrow7.pack(expand = True, fill = "both")

btnrow8 = Frame(root)
btnrow8.pack(expand = True, fill = "both")

btnrow9 = Frame(root)
btnrow9.pack(expand = True, fill = "both")

# --------------------for all buttons--------------------
# row1
btn5 = Button(
    btnrow1,
    text = "(",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#EBF5FB",
    command = lambda : btn_clicked('('),
)
btn5.pack(side = LEFT, expand = True, fill = "both",)

btn6 = Button(
    btnrow1,
    text = ")",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#EBF5FB",
    command = lambda : btn_clicked(')'),
)
btn6.pack(side = LEFT, expand = True, fill = "both",)

btn35 = Button(
    btnrow1,
    text = "←",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#B7FFA6",
    command = lambda : back_space(),
)
btn35.pack(side = LEFT, expand = True, fill = "both",)

btn4 = Button(
    btnrow1,
    text = "AC",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#FFB1A0",
    command = lambda : clear_screen(),
)
btn4.pack(side = LEFT, expand = True, fill = "both",)


# row2
btn1 = Button(
    btnrow2,
    text = "asin()",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#EBF5FB",
    command = lambda : btn_clicked('asin('),
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow2,
    text = "acos()",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#EBF5FB",
    command = lambda : btn_clicked('acos('),
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow2,
    text = "atan()",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#EBF5FB",
    command = lambda : btn_clicked('atan('),
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btn7 = Button(
    btnrow2,
    text = "exp()",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#EBF5FB",
    command = lambda : btn_clicked('exp('),
)
btn7.pack(side = LEFT, expand = True, fill = "both",)


# row3
btn9 = Button(
    btnrow3,
    text = "P",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#EBF5FB",
    command = lambda : btn_clicked('P'),
)
btn9.pack(side = LEFT, expand = True, fill = "both",)

btn10 = Button(
    btnrow3,
    text = "C",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#EBF5FB",
    command = lambda : btn_clicked('C'),
)
btn10.pack(side = LEFT, expand = True, fill = "both",)

btn11 = Button(
    btnrow3,
    text = "x!",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#EBF5FB",
    command = lambda : btn_clicked('!'),
)
btn11.pack(side = LEFT, expand = True, fill = "both",)

btn12 = Button(
    btnrow3,
    text = "√",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#EBF5FB",
    command = lambda : btn_clicked('sqrt('),
)
btn12.pack(side = LEFT, expand = True, fill = "both",)



# row4
btn13 = Button(
    btnrow4,
    text = "sin()",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#EBF5FB",
    command = lambda : btn_clicked('sin('),
)
btn13.pack(side = LEFT, expand = True, fill = "both",)

btn14 = Button(
    btnrow4,
    text = "cos()",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#EBF5FB",
    command = lambda : btn_clicked('cos('),
)
btn14.pack(side = LEFT, expand = True, fill = "both",)

btn15 = Button(
    btnrow4,
    text = "tan()",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#EBF5FB",
    command = lambda : btn_clicked('tan('),
)
btn15.pack(side = LEFT, expand = True, fill = "both",)

btn16 = Button(
    btnrow4,
    text = "％",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    command = lambda : btn_clicked('%'),
)
btn16.pack(side = LEFT, expand = True, fill = "both",)



# row5
btn17 = Button(
    btnrow5,
    text = "log()",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#EBF5FB",
    command = lambda : btn_clicked('log('),
)
btn17.pack(side = LEFT, expand = True, fill = "both",)

btn18 = Button(
    btnrow5,
    text = "ln()",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#EBF5FB",
    command = lambda : btn_clicked('ln('),
)
btn18.pack(side = LEFT, expand = True, fill = "both",)

btn19 = Button(
    btnrow5,
    text = "x^y",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#EBF5FB",
    command = lambda : btn_clicked('^('),
)
btn19.pack(side = LEFT, expand = True, fill = "both",)

btn20 = Button(
    btnrow5,
    text = "÷",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    command = lambda : btn_clicked('/'),
)
btn20.pack(side = LEFT, expand = True, fill = "both",)



# row6
btn21 = Button(
    btnrow6,
    text = "7",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    command = lambda : btn_clicked('7'),
)
btn21.pack(side = LEFT, expand = True, fill = "both",)

btn22 = Button(
    btnrow6,
    text = "8",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    command = lambda : btn_clicked('8'),
)
btn22.pack(side = LEFT, expand = True, fill = "both",)

btn23 = Button(
    btnrow6,
    text = "9",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    command = lambda : btn_clicked('9'),
)
btn23.pack(side = LEFT, expand = True, fill = "both",)

btn24 = Button(
    btnrow6,
    text = "X",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    command = lambda : btn_clicked('X'),
)
btn24.pack(side = LEFT, expand = True, fill = "both",)



# row7
btn25 = Button(
    btnrow7,
    text = "4",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    command = lambda : btn_clicked('4'),
)
btn25.pack(side = LEFT, expand = True, fill = "both",)

btn26 = Button(
    btnrow7,
    text = "5",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    command = lambda : btn_clicked('5'),
)
btn26.pack(side = LEFT, expand = True, fill = "both",)

btn27 = Button(
    btnrow7,
    text = "6",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    command = lambda : btn_clicked('6'),
)
btn27.pack(side = LEFT, expand = True, fill = "both",)

btn28 = Button(
    btnrow7,
    text = "➖",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    command = lambda : btn_clicked('-'),
)
btn28.pack(side = LEFT, expand = True, fill = "both",)



# row8
btn29 = Button(
    btnrow8,
    text = "1",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    command = lambda : btn_clicked('1'),
)
btn29.pack(side = LEFT, expand = True, fill = "both",)

btn30 = Button(
    btnrow8,
    text = "2",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    command = lambda : btn_clicked('2'),
)
btn30.pack(side = LEFT, expand = True, fill = "both",)

btn31 = Button(
    btnrow8,
    text = "3",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    command = lambda : btn_clicked('3'),
)
btn31.pack(side = LEFT, expand = True, fill = "both",)

btn32 = Button(
    btnrow8,
    text = "+",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    command = lambda : btn_clicked('+'),
)
btn32.pack(side = LEFT, expand = True, fill = "both",)



# row9
btn33 = Button(
    btnrow9,
    text = "0",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    command = lambda : btn_clicked('0'),
)
btn33.pack(side = LEFT, expand = True, fill = "both",)

btn34 = Button(
    btnrow9,
    text = ".",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    command = lambda : btn_clicked('.'),
)
btn34.pack(side = LEFT, expand = True, fill = "both",)

btn8 = Button(
    btnrow9,
    text = "∏",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#EBF5FB",
    command = lambda : btn_clicked('pi'),
)
btn8.pack(side = LEFT, expand = True, fill = "both",)

btn36 = Button(
    btnrow9,
    text = "＝",
    font = ("Verdana", 20),
    relief = GROOVE,
    border = 4,
    width = 3,
    bg = "#F9E79F",
    command = lambda : calculate_result(),
)
btn36.pack(side = LEFT, expand = True, fill = "both",)


root.mainloop()

