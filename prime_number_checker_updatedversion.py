def prime_number_checker():
    try:
        x = int(input("Write a number: "))
        
        if x < 2:
            print("{} is not a prime number".format(x))
            return prime_number_checker()

        for y in range(2, x):
            if x % y == 0:
                print("{} is not a prime number".format(x))
                return prime_number_checker()
        
        print("{} is a prime number".format(x))
        return prime_number_checker()
    
    except ValueError:
        print("That was not a valid number. Please try again.")
        return prime_number_checker()

print(prime_number_checker())
## Updates
#- Added infinite loop functionality - program auto-restarts after each check
#- Implemented input validation - handles non-numeric inputs without crashing
#- Added user-friendly error messages for invalid inputs
#- Maintained original prime checking algorithm - no changes to core logic
    
