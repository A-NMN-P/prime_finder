"""
Created on Mon Jul 31 22:45 2023
Finished on Tue Aug 1 11:50 2023

@author: Ahmed Numan Pervane

Name of Project : Prime Number Finder: function/ Libary Format

That project find the prime numbers and gives the dividers of the none prime numbers.

For more informationi look the ReadMe file

"""
# Head of the function

def isPrime(num: int, dividers: bool):
    
    Prime = True
    notPrime = False
    
    flag1 = True
    
    while(flag1):
        try: 
            given_Num = int(num)   # Take input from the function as num.
            is_div_true = bool(dividers)
        except ValueError or TypeError:
            print("\n-----INVALID INPUT! Try again-----")
            print("num or dividers: don't have got the true value or type.\n")
            flag1, flag2 = False, False
            break
        else:

            it_is_prime=[]          # Creat a list for decide the prime or not. Store the values of divider of given number includes its value and other divider except 1. 
            it_isnot_prime=[]       # Creat a list for store the values of non-divider of given number.
            list_of_divider = []    # Creat a list for store dividers except given number itself.
          
            flag2 = True
            
            if given_Num == 2:
                flag2 = False
                if dividers:
                    return Prime, list_of_divider
                else:
                    return Prime
            # if it is less than 2 then not enter the first loop and display the given number and say that is not a valid input
            elif given_Num<2:
                print(f"{given_Num} is not a prime, and 1,0, or negative integers not counted in primes as defination")
                flag2 = False
                list_of_divider.append(False)
                if dividers:
                    return notPrime, list_of_divider
                else:
                    return notPrime             
            elif not flag2 == 1 :
                print("SOMETHING WENT WRONG!\n Change the given variables.")
                flag1,flag2 = False, False
                return ValueError
            
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
                    if dividers:
                        return Prime, list_of_divider
                    else:
                        return Prime
                
                else:   # otherwise the length of it_is_prime list is none 1 than execute the else condition.                  
                    # If the given number is not the prime then find its dividers via for loop. dividers must be included from it_is_prime list.
                    if is_div_true is True:
                        for divider in it_is_prime:
                            if not divider == given_Num:    # Make an exception from the given nuber in the list of it_is_prime to not display it.
                                if not given_Num%divider:
                                    list_of_divider.append(divider) # Added the dividers to the list of dividers
                        if dividers:
                            return notPrime, list_of_divider
                        else:
                            return notPrime
                    else:
                        if dividers:
                            return notPrime, list_of_divider
                        else:
                            return notPrime
 

def Prime_Finder(initilizer : int(2) , limit: int, prime_list: bool, noneprime_list: bool, division_list: bool, step : int(1) ):
    flager = True
    while flager:
        try: 
            init            =   int(initilizer)
            lim             =   int(limit)
            step            =   int(step)
            p_list_bool     =   bool(prime_list) 
            unp_list_bool   =   bool(noneprime_list)
            div_list_bool   =   bool(division_list)
            if initilizer >=2:
                flager,flagTest = True, True
                
            else:
                flager, flagTest = False, False
                break
            
        except ValueError or TypeError:
            print("\n-----INVALID INPUT(s)! Try again-----")
            print("Some arguments are not satisfying. They don't have got the true value or type.\n")
            flager, flagTest = False, False
            continue
        
        else:
            flagTest = True
            
            counterTest = init
            
            prime_numbers = []
            unprime_numbers = []
            dividers =  []
            dividers_main_list = []
            
            while flagTest:
                
                
                if ((p_list_bool or unp_list_bool) is True and div_list_bool is True):
                    p, div = isPrime(counterTest, div_list_bool)
                   
                elif ((p_list_bool is True or unp_list_bool is True) and div_list_bool is False):
                    p = isPrime(counterTest, div_list_bool)
                    div = []
                    
                elif ((p_list_bool or unp_list_bool) is False and div_list_bool is True):
                    p, div = isPrime(counterTest, div_list_bool)
                    p = False
                    
                elif ((p_list_bool or unp_list_bool) is False and div_list_bool is False):
                    p, div = False, []
         
                if p_list_bool:
         
                    if p:
         
                        prime_numbers.append(counterTest)
                    
                if unp_list_bool:
         
                    if not p:
         
                        unprime_numbers.append(counterTest)

                if div_list_bool:
         
                    
                    if len(div) > 0 and type(div[:]) is not bool:
         
                        dividers.append(div)
                        dividers_main_list.append({counterTest : dividers[-1]})

                if counterTest >= limit:
         
                    if p_list_bool is True and unp_list_bool is False and div_list_bool is False:
                        return prime_numbers
                

                    elif p_list_bool is False and unp_list_bool is True and div_list_bool is False:
                        return unprime_numbers
    
    
                    elif p_list_bool is False and unp_list_bool is False and div_list_bool is True:
                        return dividers_main_list
                    
                    
                    elif p_list_bool is True and unp_list_bool is True and div_list_bool is False:
                        return prime_numbers, unprime_numbers
                    
    
                    elif p_list_bool is True and unp_list_bool is False and div_list_bool is True:
                        return prime_numbers, dividers_main_list
    
    
                    elif p_list_bool is False and unp_list_bool is True and div_list_bool is True:
                        return unprime_numbers, dividers_main_list
                    
                    
                    elif (p_list_bool and unp_list_bool and div_list_bool) is True:
                        return prime_numbers, unprime_numbers, dividers_main_list
                    
                    
                    else: 
                        print('ERROR! System interupted.\nError type: unknown. Please handle that by yourself.')
                        flager, flagTest = False, False
                        break
                
                else:
                    counterTest += step
                    continue

      
            
            
