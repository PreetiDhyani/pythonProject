# import math
# math.exp(1000) #OverflowError: math range error

import math
try:
   math.exp(1000) #OverflowError: math range error
except Exception as e:
    print(e)

#
# reult:
# D:\Preeti\3.Python\PyATB5xLearning\venv\Scripts\python.exe D:\Preeti\3.Python\PyATB5xLearning\Dec\ex_07122024_Exceptions\Lab167_Exception_1.py
# math range error
#
# Process finished with exit code 0

