#While loops
# If the value of x is less than 5 it will print out the value until the value of x is 5, however with each loop/iteration that it goes through, it will add 1 to the previous value of x
#in the first iteration the value of x = 0  so we print out 0
#then it will add 1 and provide us with out next value of x which is 1 and since it is less than 5, it will print out that value of 1
#then it will add 1 to 1 and we will have 2 which is less than 5 so it will print out that value and it will go through this process 
#until our printed value is 5. At which point it will not print out that value and the loop will stop.



x = 0
while x < 5:
    print(x)
    x = x + 1

# A for loop iterating through the numbers 1-4
numbers = [0,1,2,3,4]
for num in numbers:
    print(num)

# The same code as the iterator above, simplified
for num in range(5):
    print(num)

