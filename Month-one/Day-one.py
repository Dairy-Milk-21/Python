# ### **🗓️ Week 1: Python Basics & Data Types**  
# #### 📖 **Topics to Learn:**  
# ✅ Installing Python & VS Code  -- Done
# ✅ Variables, Data Types (int, float, str, bool, None)  
# ✅ Input/Output (print, input)  
# ✅ Typecasting  
# ✅ Conditional Statements (`if-else`)  
# ✅ Loops (`for`, `while`)  
# ✅ Operators (Arithmetic, Logical)  

#The four Datatypes I am gonna learn are : int, float, str, bool
#A variable is a box that grasp a value whenever we assign to it.

int_var = 20
float_var = 20.5
string_var = "Twenty"
bool_var = False,True

#An input funtion is a function that asks input from the user
input_var = input("What is your name?: ")
print(f"Hello{input_var}") #Here the f"" is a method for formatted string use.

#Typecasting

int_var = "30"
print(type(int_var))
print(float(int_var))
print(bool(int_var))
print(int(int_var))

#A good example of typecasting
let_x =int( input("Give a number and get the square : ") )
print(f"The square of the number is :{let_x * let_x}")

#Control-Flow: If-else conditioning
let_y = "Donald j.Trump"
let_z = input("Who is the current president of USA? : ")
if let_z == let_y :
    print("Correct!")
else:
    print("Wrong!")

#Control-Flow: While loops
a_var = 1
while(a_var <=100):
    print(a_var)
    a_var+=1
#Control-Flow: For loops
for let_b in range(1,101):
    print(let_b)
    let_b+=1

#Arithmetic operations
