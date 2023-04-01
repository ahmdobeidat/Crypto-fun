from fractions import Fraction
from decimal import Decimal
def encrypt_text(input_str, list1, list2):
    """
    Maps characters from input_str to values in list2 based on their position in list1,
    and returns the numerator and denominator of the fraction representing the decimal value
    of the resulting mapped and concatenated string with '0.' at the beginning.
    """
    # Generate a list of mapped values using a list comprehension
    mapped_vals = [list2[list1.index(char)] for char in input_str]
    
    # Concatenate the mapped values into a single string with '0.' at the beginning
    mapped_str = '0.' + ''.join(mapped_vals)
    
    # Convert the mapped string to a decimal number
    mapped_decimal = Fraction(mapped_str)
    
    # Return the numerator and denominator of the decimal number as a tuple
    return mapped_decimal.numerator, mapped_decimal.denominator

# Define two lists of strings to map together
list1 = [' ' ,'a', 'b', 'c', 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]

list2 = ['00','01', '02', '03', '04' , '05' , '06' , '07' , '08' , '09' , '10' , '11' , '12' , '13' , '14' , '15' , '16' , '17' , '18' , '19' , '20' , '21' , '22' , '23' , '24' , '25' , '26' ]

# Call the encrypt_text() function with an input string and the two mapping lists
input_str = input('Enter text you want to encrypt: ')
A, B = encrypt_text(input_str, list1, list2)

# Print the numerator and denominator of the resulting fraction
print(f"A={A} B={B}")
