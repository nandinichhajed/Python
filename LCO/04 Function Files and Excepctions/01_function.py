print("Hello")

#function - methods

def nandini():
    "function docString"
    print("I want to learn python")
    print("I am doing it")
    return

# return is something which marks the function as complete

def greetings( name ):
    "function docString"
    print("Hello,", name)
    return


def user_creation(name, email, phone=0):
    print("Name is: ", name)
    print("email is: ", email)
    print("phone is: ", phone)
    return


user_creation("nandini", "nandini@example.com", 989898)
