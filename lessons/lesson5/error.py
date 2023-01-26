#try
#except
#else
#finally
#raise
#assert
#custom exceptions

class TooLowNumberValueError(Exception):
    msg:str

    def __init__(self,msg):
        self.msg = msg

def do_something(a):
    res = int(a)
    if res <2:
        raise TooLowNumberValueError("The number is way too low")
    return res
try:
    print("try")
    assert 2 == 2
    print(do_something(1))

except AssertionError:
    print("AssertionError")
except ValueError as e:
    print("SyntaxError",e.msg)
except TooLowNumberValueError as e:
    print(e.msg)
except SyntaxError:
    print("SyntaxError")
except:
    print("Catch em all")
else:
    print("OK")
finally:
    print("I will always be with you")