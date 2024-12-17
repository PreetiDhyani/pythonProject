print ("---------start of the program")
try:
   a= int(input("Ent num 1")) # value error occurs when trying to pass alphabet
   b= int(input("Ent num 2"))
   c=a/b # ZeroDivisionError: division by zero _when trying to divide by zero
   print("Result div is", c)
except Exception as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
