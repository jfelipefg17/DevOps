# Constants
TITLE_COURSE = "Python Course"

# Dynamic
value = 10
print(value)
value = "Felipe"
print(value)
value = True
print(value)
value = 23.45
print(value)

# Logic and rational values
number1 = 10
number2 = 14

result = number2 > number1
print(result)
result = number2 >= number1
print(result)
result = number2 < number1
print(result)
result = number2 <= number1
print(result)
result = number2 == number1
print(result)
result = number2 != number1
result2 = not((False or True) and (True or False))
aux = type(result2)

# Change type of the variable
age = int(input("Enter your age: "))
print(type(age))

aux1, aux2, aux3 = "Felipe", "Andres", "Pedro"

# List
my_list = [10, 34, 24, 454, 46, 90, 90, 89]
list2 = [12.3, 34.5, 12.5]
list3 = ["Hola", "Felipe", "Florez", "Andres"]

first_element = my_list[0]
last_element = list3[2]
list2[1] = 36.4
print(list2)

list4 = list3[0:2]
list5 = list3[0:100]
list6 = my_list[0:]
list7 = list3[:3]
list8 = my_list[0:7:2]
list9 = my_list[:]
list10 = my_list[::2]
print(list4)
print(list5)
print(list6)
print(list7)
print(list8)
print(list9)
print(list10)

my_list.append(35)
len(my_list)
my_list.insert(2, 2000)
my_list.extend(list6)
my_list.remove(10)
del my_list[1]
my_list.clear()

listt = [10, 34, 24, 454, 46, 90, 90, 89]

listt.sort()
listt.sort(reverse=True)

print(min(listt))
print(max(listt))

aux4 = 10 in listt

print(listt.index(10))

# Matrix
matrix = [[10, 20], [20, 40]]
print(matrix)
matrix2 = [listt, my_list]
print(matrix2)

# Tuple
tuple1 = (10, 20, 30, 40, 50, 60)
print(tuple1)
tuple3 = ("Hola", 10, True, [1, 3, 4, 6, 7])
print(tuple3)

print(tuple1[0])
sub_tuple = tuple1[0:2]
print(sub_tuple)

# Moving into tuples and lists
list_to_tuple = tuple(my_list)
tuple_to_list = list(tuple1)

# Zip
zip1 = zip(tuple1)
tuple_back = tuple(zip1)


# This program calculates the area and perimeter of a rectangle.
# Define variables for the length and width of the rectangle
length = 5
width = 3

# Calculate the area of the rectangle
area = length * width

# Calculate the perimeter of the rectangle
perimeter = 2 * (length + width)

# Print the calculated area and perimeter
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)

# Function to calculate area of rectangle
def calculate_area(length, width):
    return length * width

# Function to calculate perimeter of rectangle
def calculate_perimeter(length, width):
    return 2 * (length + width)

# Function to handle invalid inputs
def handle_invalid_input():
    print("Invalid input. Please enter valid numbers.")

# Main function
def main():
    try:
        # Input length and width from user
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))

        # Check if inputs are valid (positive numbers)
        if length <= 0 or width <= 0:
            raise ValueError

        # Calculate area and perimeter
        area = calculate_area(length, width)
        perimeter = calculate_perimeter(length, width)

        # Print results
        print("The area of the rectangle is:", area)
        print("The perimeter of the rectangle is:", perimeter)

    except ValueError:
        handle_invalid_input()

# Execute the main function
if __name__ == "__main__":
    main()
