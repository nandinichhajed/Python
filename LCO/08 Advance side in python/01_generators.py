import random
h = ["hulk", "batman", "superman", "haul"]

for i in h:
    print(i)
    
# anything that can generate an iterator is called generator
# anything on which you can run a for in loop is an itetrable 
# if u want to create your own itetrable u need to use generator
g = range(6)
print(g)

def magic():
    for i in range(6):
        yield random.randint(1, 20)
        
for number in magic():
    print("The value is: ", number)