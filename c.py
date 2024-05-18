# # Example data
# line = "Apple|Banana|Grapes|Orange|Pineapple"
# line2 = "a|b|c|d|e"

# # Split the lines by '|'
# parts1 = line.split('|')
# parts2 = line2.split('|')

# # Calculate the maximum lengths for each part
# max_length1 = max(len(part) for part in parts1)
# max_length2 = max(len(part) for part in parts2)

# # Print the lines with parts aligned in the same column
# for part1, part2 in zip(parts1, parts2):
#     print("{:<{}} | {:<{}}".format(part1, max_length1, part2, max_length2))


# Example data
a, b, c, d, e = "Apple", "Banana", "Grapes", "Orange", "Pineapple"
x, y, z, g = "a", "b", "c", "d"

# Combine all the variables
all_variables = [a, b, c, d, e, x, y, z, g]

# Calculate the maximum width
max_width = max(len(variable) for variable in all_variables)

# Print the first line
print("|".join("{:<{}}".format(variable, max_width) for variable in [a, b, c, d, e]))

# Print the second line
print("|".join("{:<{}}".format(variable, max_width) for variable in [x, y, z, g]))
