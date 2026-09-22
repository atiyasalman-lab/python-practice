ungrouped data
import statistics
data = [1,2,3,1,7,8]

mode_value = statistics.multimode(data) # multimode use for multi frequency.. for 1 freq, use only statistics.mode
print("Modes are ->", mode_value)



ungrouped data
data = [1,2,3,1,1,7,8]
max_count = 0

for i in data:
    count = data.count(i)

    if count > max_count:
        max_count = count
        mode = i
print("Mode is", mode)
print(count)

def modes(data):
    max_count = 0
    modes = []

    for i in data:
        count = data.count(i)
        if count > max_count:
            max_count = count
            modes = [i]
        elif count == max_count:
            if i not in modes:
                modes.append(i)

        
    return modes
data = [1,2,3,7,7,1,8]
print("Modes are", modes(data))


