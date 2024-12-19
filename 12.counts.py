input_string = "Raja"
input_string = input_string.lower()
char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] += 1  
    else:
        char_count[char] = 1
for char, count in char_count.items():
    print(f"'{char}': {count}")
