##hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
##
### Step 1: write a line of code that prompts the user
### to replace the middle number with an integer number entered by the user.
##hat_list[2] = int(input("Insert a number into the hat: "))
##
### Step 2: write a line of code that removes the last element from the list.
##del hat_list[4]
### Step 3: write a line of code that prints the length of the existing list.
##print("Length of the hat_list: ", len(hat_list))
##print(hat_list)
##
###================================================
##my_list = [10, 1, 8, 3, 5]
##total = 0
##
##for i in range(len(my_list)):
##    total += my_list[i]
##
##print(total)
##
##my_list = [10, 1, 8, 3, 5]
##total = 0
##
##for i in my_list:
##    total += i
##
##print(total)
###================================================
##
### step 1
##beatles = []
##
##print("Step 1:", beatles)
##
### step 2
##beatles.append("John Lennon")
##beatles.append("Paul mcCartney")
##beatles.append("George Harrison")
##
##print("Step 2:", beatles)
##
### step 3
##extra_beatles = ["Stu_sutcliffe","Pete_best"]
##
##for i in extra_beatles:
##        beatles.append(i)
##        
##print("Step 3:", beatles)
##
### step 4
##del beatles[3]
##del beatles[3]
##
##print("Step 4:", beatles)
##
### step 5
##beatles.insert(0, "Ringo Starr")
##print("Step 5:", beatles)
##
##
### testing list legth
##print("The Fab", len(beatles))
my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

