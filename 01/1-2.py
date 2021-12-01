# Enumerates over a sublist that starts at window_size, then compares that value
# with the value at 3 (window_size) positions earlier.
# In the example below, the window for A and B share 2 values that are irrelevant for the comparison.
# A   <- depths[i]
# A B
# A B
#   B <- depth

counter = 0
window_size = 3
        
with open('input') as file:
    depths = [int(i) for i in file]
    for i, depth in enumerate(depths[window_size:]):
        if depth > depths[i]:
            counter += 1

print(counter)