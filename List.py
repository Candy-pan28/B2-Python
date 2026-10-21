def find_max(my_list):
    #this function find the maximum value in a list
    max_value = my_list[0] #initialise with the first element
    for item in my_list:
        if item > max_value:
            max_value = item
    return max_value
my_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
max_value = find_max(my_list)
print("The maximum value is:", max_value)
