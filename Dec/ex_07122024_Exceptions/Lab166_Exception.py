# print ("---------start of the program")
#
# a= int(input("Ent num 1")) # value error occurs when trying to pass alphabet
# b= int(input("Ent num 2"))
# c=a/b # ZeroDivisionError: division by zero _when trying to divide by zero
# print("Result div is", c)

# to cope up this, we will try TRY AND EXCEPT

print ("---------start of the program")
try:
   a= int(input("Ent num 1")) # value error occurs when trying to pass alphabet
   b= int(input("Ent num 2"))
   c=a/b # ZeroDivisionError: division by zero _when trying to divide by zero
   print("Result div is", c)
except Exception as e:
    print(e)


print ("---------End of the program")


# result:
# D:\Preeti\3.Python\PyATB5xLearning\venv\Scripts\python.exe D:\Preeti\3.Python\PyATB5xLearning\Dec\ex_07122024_Exceptions\Lab166_Exception.py
# ---------start of the program
# Ent num 1ee
# invalid literal for int() with base 10: 'ee'
# ---------End of the program
#
# Process finished with exit code 0