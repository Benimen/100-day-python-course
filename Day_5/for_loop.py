
# List
random_numbers_list = [123, 88, 55, 23, 734, 98, 37, 25 ,78, 95, 64, 34, 76, 45]

# Copy list to another variable
test_list = random_numbers_list.copy()

# For loop looking in random_number_list
for max_number in random_numbers_list:

    # Looking at max value of test_list and putting it in another variable
    max_number = max(test_list)
   
    # Prints current max value from test_list
    print(max_number, end=" ")

    # Removes current max value from test_list
    test_list.remove(max_number)



# Chatgpt version

# random_numbers_list = [123, 88, 55, 23, 734, 98, 37, 25, 78, 95, 64, 34, 76, 45]

# # Sort the list in descending order
# sorted_list = sorted(random_numbers_list, reverse=True)

# # Print each element in the sorted list
# for number in sorted_list:
#     print(number, end=" ")