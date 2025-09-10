# My first GitHub project
# A simple prime number checker written while learning Python :)

def prime_number_checker():
    x = int(input("Write a number: "))
    
    if x < 2:
        return "{} is not a prime number".format(x)

    for y in range(2, x):
        if x % y == 0:
            return "{} is not a prime number".format(x)
    
    return "{} is a prime number".format(x)

print(prime_number_checker())

    
    

      
        
      
      
    
    
      
