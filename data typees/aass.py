# This function converts a tuple to a list
def convert_tuple_to_list(input_tuple):
    # Use the built-in list() function to convert the tuple
    return list(input_tuple)

# Main part of the program
def main():
    # Define a tuple
    my_tuple = (10, 20, 30, 40, 50)

    # Display the original tuple
    print("Original Tuple:", my_tuple)

    # Convert the tuple to a list
    my_list = convert_tuple_to_list(my_tuple)

    # Display the converted list
    print("Converted List:", my_list)

# Check if the script is being run directly
if __name__ == "__main__":
    main()