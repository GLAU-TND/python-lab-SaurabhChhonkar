class MyException(Exception):
    def __init__(self,v):
        self.v=v
def xyz():
    a = int(input("Enter first number: "))
    b = int(input("Enter secand number: "))
    c = a+b
    if c < 150:
        raise MyException('Custom Exception Occurred')
xyz()
