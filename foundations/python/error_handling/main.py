"""Exercise 1"""
try:
    int_ = int(input("Enter a number: "))
    print(int_)
except ValueError:
    print( "input can only be a number")
    
    
"""Exercise 2"""

def giv_num():
    try:
        
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        c = a / b 
        print(a, b)
        print(c)
    except ValueError:
        print("Enter a valid number")

    except ZeroDivisionError:
        print("input cannot be zero")
giv_num()



    
"""Exercise 3"""
wam = [1, "a", 3, 4, 0]    

def try_list(item, index):
    
    try:
        
        print(item[index])
    except TypeError:
        print("This index does not exit, enter a valid index")
    except IndexError:
        print("Index probably out of range, enter a valid index")

try_list(wam, "hello")



"""Exercise 4"""


student = {
    "name": "John",
    "age": 25,
    "course": "Computer Science"
}

# def fetch_dic():
#     dic = input("Enter the dictionary name: ")
#     key_ = input("Enter the key: ")
#     # key_ = f""{key_}""
#     try:
#         dic[key_] 
#     except KeyError:
        
#         print( "Key not valid, enter another one")
key_ = input("Enter a key: ")
try:
    print(student[key_])
except KeyError:
    print("Enter a valid key")
# finally:
#     print('a')


    """Exercise 5"""
def validate_age(age):
    if age < 0:
        raise ValueError("Age can't be negative")
    elif age > 120:
        raise ValueError("Sorry you're not qualify, you,re aged")
    else:
        return f"Valid age, you're {age}"
validate_age(25)