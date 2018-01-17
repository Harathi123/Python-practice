import random
import string



def rand_pswrd_gen(chars, size):
    """ 
    Function to generate random password containing uppercase letters or lower case letters, digits and punctuations.
    Args: param1: chars which contain all the upper and lower case letters, digits and punctuations.
          param2: required size of the password.
      
    Returns: The function returns the password.
    """
    rand_pswrd = ''.join(random.sample(chars, size))
    return rand_pswrd

chars = string.digits + string.ascii_letters + string.punctuation    
password = rand_pswrd_gen(chars, int(raw_input('How many characters in the password')))

print "Randomly generated password is :", password