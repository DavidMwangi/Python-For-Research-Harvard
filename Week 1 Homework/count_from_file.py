import count_letters

file = open("sample.txt", "r")

for line in file:
    
    print(line)
    
    address_counter = count_letters.counter(line)

print(address_counter)