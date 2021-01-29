# Reads a list of numbers from a file and computes the number of evn and odd numbers.
# The first number in the file represents the length of the list.


# Open file and read the length of the list
input_file = open('even_odd_counter.in', 'r')
nlines = int(input_file.readline())
print("nlines =", nlines)

# Read the list from the file
input_list = []
for i in range(nlines):
    input_list += [int(input_file.readline())]
print("The list is", input_list)


# Compute the number of even and odd numbers
even_list = []
odd_list = []
for n in input_list:
    if n%2 == 0:
        even_list += [n]
    else:
        odd_list += [n]


# Display the results
print("Even numbers =", len(even_list))
print("Odd numbers =", len(odd_list))

# Close the file
input_file.close()