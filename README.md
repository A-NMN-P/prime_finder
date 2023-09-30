# prime_finder
That code will decide a number is prime or not. Which that code includes two functions: isPrime and Prime_Finder. isPrime function is use to decide the given number is prime or not and if it is not a prime number -in your request- it gives you the dividers. Prime_Finder is take 6 atributes, 3 of them int other 3 is bool. 

I have shared the basic version of the prime finder. Ready to copy and paste


"""

Created on Mon Jul 31 22:45 2023
Finished on Tue Aug 1 11:50 2023

@author: Ahmed Numan Pervane

Name of Project : Prime Number Finder

That project find the prime numbers and gives the dividers of the none prime numbers.

"""


'''

That comment code side is begining of the code.
That comment have provide the none-imported function
which is just operates under the included project as 
works on your project. You are free to copy.

But the function version is alot simplier and more efficienct
than the user keyboard input version (the commeted code).

You may use the code regardless.


by Ahmed Numan Pervane

Mechatronics Engineer

'''


#----------EXAMPLE CODE----------#

from prime_finder import Prime_Finder, isPrime

prime, noneprime, divider = Prime_Finder(initilizer = 2, limit = 10, prime_list=True, unprime_list=True, division_list=True, step = 1)

print("Prime Numbers: ", prime)

print("None Prime Numbers: ", noneprime)

print("Dividers: ", divider)





# user inputter copy-past code:

# Main Code Block:

    flag1 = True
    
    while(flag1): # Main while loop:
        
        print("Give a number for the testing of prime or not.\n")   # Inform the user about program.
    
        # Debugging the str valued inputs.
        try: 
            given_Num = int(input("Your given number: "))   # Take input from the user by keyboard.
       
        except ValueError:
            print("\n","INVALID INPUT! Try again.")
            print("User input", ': ', "has not got the true value.", '\n')
            flag2 = 0
            continue
        # execution part
        else:
            flag2 = True
    
            if type(given_Num) is int:
                flag2 = True
            
            elif type(given_Num) is not int:
                flag1, flag2 = True, False
    
            # check the given interger is 2 or less. 
            # if it is 2 then just show up it as a prime number.
            if given_Num == 2:
                print("2 is a prime number")
                flag2 = False
            
            # if it is less than 2 then not enter the first loop and display the given number and say that is not a valid input
            elif given_Num<2:
                print(f"{given_Num} is not a prime, and 1,0, or negative integers not counted in primes as defination")
                flag2 = False
             
            elif not flag2 == 1 :
                print("SOMETHING WENT WRONG!\n Restart and change the given variable.")
                flag1,flag2 = False, False
                break
            
            
            it_is_prime =     []          # Creat a list for decide the prime or not. Store the values of divider of given number includes its value and other divider except 1. 
            it_isnot_prime =  []       # Creat a list for store the values of non-divider of given number.
            list_of_divider = []    # Creat a list for store dividers except given number itself.
            
            # Start counter loop for decision of the primeness of number.
            while(flag2):   # First while loop.
                counter = 2
                # second loop for handle the given number to decide prime or not.
                while counter <= given_Num: # Second/Counter while loop
                 
                    primeness = given_Num % counter     # Primeness is defined as the counter is a divider or not if counter is divider then primeness is 0 otherwise it is 1.
                    
                    # if-else condition for added the counter to true list.
                    if not primeness:
                        it_is_prime.append(counter)
                        
                    else:
                        it_isnot_prime.append(counter)
                 
                    counter += 1    # 1 added to counter.
                  
                if len(it_is_prime) == 1:   # length of the list of it_is_prime must be 1 including the given number.
                    print(f"{given_Num} is a prime number.\n")
                
                else:   # otherwise the length of it_is_prime list is none 1 than execute the else condition.
                    print(f"{given_Num} is not a prime number.\n")
                    
                    # If the given number is not the prime then find its dividers via for loop. dividers must be included from it_is_prime list.
                    for divider in it_is_prime:
                        if not divider == given_Num:    # Make an exception from the given nuber in the list of it_is_prime to not display it.
                            if not given_Num%divider:
                                list_of_divider.append(divider) # Added the dividers to the list of dividers
                                
                    print(f'list of the dividers:\n{list_of_divider}\n')    # Diplay the dividers to user.
                      
                    
                go_stay = input("Do you want to continue? (y/n): ").lower() # Ask to user want to continue or not, then get the input from user.
                
                # if-else condition to respect the user desires
                if go_stay == 'y':
                    flag1, flag2 = True, False  # if user says yes, then the close the first while loop but still continue the main while loop for take inputs again.
                    
                else:
                    if not go_stay == 'n':
                        print('Keybord Interupted. System closed.') # if the user enters the none of the y or n then interupte the program and display the print.
                    flag1, flag2 = False, False # if user says no, then the close the main and first loop to not operate.
    
