# Step 1
A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
C = int(input("Enter the third number: "))

# Step 2
if A > B:
    largest = A
else:
    largest = B

# Step 3
if largest > C:
    largest_number = largest
elif largest < C:
    largest_number = C
else:
    largest_number = largest

# Step 5
print("The largest number is:", largest_number)
