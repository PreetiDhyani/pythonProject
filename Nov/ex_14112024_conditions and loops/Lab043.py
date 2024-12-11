# Write a program to take a user age and let him know f he can go to the club

# Logic building formula

# Step 1
# user input i/p  data type
# o/p --> String -> Userif he can go or not


#step 2. Rough logic

# age >21 > printt can go
# age <21 > print can't go

# step 3. write the logic

age = input("Enter your age\n")
age = int(age)

if age >= 21:
    print ("can go to club")
else:
    print("can't  go to club")

    # Step 4. Check for the edge cases
    # we should consider edge cases such as:
    # negative ages or extremely high values> program will break
    # non-numeric input-ABC
    # aGE which is valid. >130


    # Step 5. Optimize teh code.
    # Handle all the edges
