import os

def create_file():
    open('cache.txt', 'a').close()
    
    with open('cache.txt', 'w') as file:
        file.write('False')
        
def retrieve_from_file():
    with open('cache.txt', 'r') as file:
        value = file.read()
        
        return value
    
if not os.path.exists('cache.txt'):
    create_file()
    
value = retrieve_from_file()

print(value)
    
