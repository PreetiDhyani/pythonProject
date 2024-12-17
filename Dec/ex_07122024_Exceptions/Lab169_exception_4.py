from typing import final

try:
   num1= int(input("Ent num 1")) # value error occurs when trying to pass alphabet
   num2= int(input("Ent num 2"))
   result = num1/num2 # ZeroDivisionError: division by zero _when trying to divide by zero
except Exception as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("Output is ", result)
finally:
    print("this will always executed")