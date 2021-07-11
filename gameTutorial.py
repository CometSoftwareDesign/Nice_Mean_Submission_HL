"""Tutorial For Python Game"""






def start():
       fname = "Adonis"
       lname = "Leonidas"
       age = 25
       gender = "Male"
       get_info(fname,lname,age,gender)

def get_info(fname,lname,age,gender):
       print("My name is {} {}. I am {} years old and I am a {}.".format(fname,lname,age,gender))




def start2():
       print (get_name())

def get_name():
       name = input("What is your name?")
       return name


def start3():
       print(get_number())

def get_number():
       number = 12
       return number




if __name__ == "__main__":
       start()
