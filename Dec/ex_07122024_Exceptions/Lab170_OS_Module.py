import os

print(os.getcwd())
#
# result:
# D:\Preeti\3.Python\PyATB5xLearning\venv\Scripts\python.exe D:\Preeti\3.Python\PyATB5xLearning\Dec\ex_07122024_Exceptions\Lab170_OS_Module.py
# D:\Preeti\3.Python\PyATB5xLearning\Dec\ex_07122024_Exceptions

files = os.listdir('.')
print(f"Files in current directory: {files}")

# result:
# D:\Preeti\3.Python\PyATB5xLearning\Dec\ex_07122024_Exceptions
# Files in current directory: ['Lab166_Exception.py', 'Lab167_Exception_1.py', 'Lab168_Exception_2.py', 'Lab169_exception_4.py', 'Lab170_OS_Module.py', '__init__.py']


# os.mkdir('testPreeti')
# # Create a new directory

file_exist = os.path.exists("Testdata.txt")
print(file_exist)
#
# Result:
# D:\Preeti\3.Python\PyATB5xLearning\venv\Scripts\python.exe D:\Preeti\3.Python\PyATB5xLearning\Dec\ex_07122024_Exceptions\Lab170_OS_Module.py
# D:\Preeti\3.Python\PyATB5xLearning\Dec\ex_07122024_Exceptions
# Files in current directory: ['Lab166_Exception.py', 'Lab167_Exception_1.py', 'Lab168_Exception_2.py', 'Lab169_exception_4.py', 'Lab170_OS_Module.py', 'Testdata.txt', 'testPreeti', '__init__.py']
# True
#
# Process finished with exit code 0