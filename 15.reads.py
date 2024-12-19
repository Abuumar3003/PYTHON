# Function to extract characters from even levels (even indices)
def even_level_substring(input_string):
    # Extract characters at even indices using slicing
    even_level_string = input_string[::2]
    return even_level_string

# Input string
input_string = "Sunrises in the east"

# Call the function to get the substring with even level characters
result = even_level_substring(input_string)

# Output the result
print("The substring with characters at even levels is:", result)
