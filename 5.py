class TooYoungException(Exception):
    def __init__(self,age):
        self.age=age
class TooOldException(Exception):
    def __init__(self,age):
        self.age=age
try:
    age=int(input("Enter Age:"))
    if age<18:
        raiseYoungException("Plz wait some time ")
    elif age>65:
        raiseTooOldException("Your age too old")
    else:
        print("we will find one girl soon")
except YoungException as e:
	print("Plz wait some time ")
except OldException as e:
	print("Your age too old ")
