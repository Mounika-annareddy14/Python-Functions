"""
Functions - is a small , reusable block of code that does one specific job

1.Built-in functions
        we can directly use that functions
2.Standard library
    writen by pyton team
        first we need to import from library
        later we can use them
3.External Library
    written by community
        install
        import
        use them
4 User defined functions
        written by us
        define and use
"""

# Built-in Functions
print(len('Python'))

# Library functions
import math
print(math.ceil(5.6))

#user defined functions
def my_routine():
    print("WakeUp")
    print("Make Coffe")
my_routine()

"""Parameters:
        Names used in fuction defination that describe what data the function expects
Arguments:
        Actual values passed in a  function call that are assigned to parameters
         
Difference
parameters          |     Arguments

define in function       define in function call
defination

placeholder              real value fills placeholder

defines what             provide function with values
function expects         
"""

def clean_text(name): #parameter
    print(name.strip().lower())
clean_text("  MouniKA  ")  # Arguments
clean_text("")


"""Global Variable
        created the outside function can be accessed anywhere
Local Variables
        created  inside the  function can be accessed only inside the function """

case_rule='lower' #Global variable
def clean_text(name): #parameter we cant access outside
    cleaned = name.strip()  #Local Variable
    if  case_rule=='lower':
        cleaned=cleaned.lower()
    print('Raw:',name)
    print('Cleaned:',cleaned)

clean_text("    MounikA      ")
# print(case_rule) #Blobal variable
# print(cleaned) #local variable
# print(name) #parameter

"""Postional Argumets:
        Values passed to the function  based on their order
Keyword Arguments:
        Values pass to the function based on theri names
Default parameter:
        parameter that has alrady a value so if u dont pass anything in python uses that value automatically"""

def full_name(first_name,last_name,country='n/a'):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name +" " + "From" + " "+  country)
full_name("MounikA    ", "Annareddy  ",'India') #positinol
full_name(country='India',last_name='Annareddy   ',first_name='   Mounika') #Keyword

#Mix arguments
#while mix arguments first must have positional
full_name("moUnikA  ",last_name='Annareddy',country='DE')

#default parameter
full_name('Mounika ','Annareddy')


"""
*args   positinal arguments
       only values
       same type of information
       type : tuple:
**kawrgs
      Keyword arguments
      names and values
      different type of information
      type:Dictionary
"""
#positinal
def sum_(*args):
    print(sum(*args))

sum_((1,2,3))
sum_((4,5,6,8,98,87))


#keyword
def user_profile(**kwargs):
    print(kwargs)

user_profile(
    first_name='Mounika',
    last_name='Annareddy',
    age=23,
    profession="Data Scientist"
)

user_profile(
    age=23,
    country = 'India'
)

"""Return"""
def clean_text(name):
    cleaned = name.strip().lower()
    return cleaned
cln_name = clean_text("Mounika  ")
print(cln_name)

def clean_text(name):
    lo_clean = name.strip().lower()
    up_clean = name.strip().upper()
    return lo_clean,up_clean
lo_clean,up_clean = clean_text('Mounikaa ')
print(lo_clean,up_clean)

def clean_text(name):
    if not name:
        return None
    else:
        cleaned = name.strip().lower()
        return cleaned
cln_name = clean_text("")
print(cln_name)


"""Action functiom"""
def write_log(message):
    with open(r'C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\\Python-functions\\app.log','a') as file:
        file.write(message +'\n')

write_log("App started")
write_log('User logged in')
write_log('App stopped')

"""Transformation"""
#clean a email and store in datastructure
def clean_email(email):
    cl_email = email.strip().lower()
    username,domain = cl_email.split("@")
    return {"username":username,
            "Domain":domain}
print(clean_email('mounikaannareddy@gmail.com'))

"""Validation"""
def is_valid_password(password):
    return len(password)>=8
print(is_valid_password("123"))
print(is_valid_password("123456789"))


def is_valid_email(email):
    return "@" in email and "." in email

print(is_valid_email('annaredyy'))
print(is_valid_email('annareddy@gmail.com'))



"""Lambda Functions
a tiny function which does not have name(annyomus function)
"""
multiple = lambda x: x *2
print(multiple(2))

add = lambda x,y : x+y
print(add(1,2))

check = lambda i: i in "python"
print(check('n'))

"""map,reduce,filter"""
prices = ['$19.24','$67.2','$1.02']
print(list(map(lambda p: float(p.replace('$','')),prices)))

"""Filter"""
scores = [100,255,677,790]

print(list(filter(lambda s:s>=500,scores)))
