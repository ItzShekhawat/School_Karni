"""
    Author : Karni Singh Shekhawat   
    Data : 18/11/2020 
"""

import random
import sympy
import logging

def control_input(input_num):
    
    return sympy.isprime(input_num)


#------------------------------------------------------------------------------------
def lcm(p, q):

   if p > q:
       greater = p
   else:
       greater = q

   while(True):
       if((greater % p == 0) and (greater % q == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

#-------------------------------------------------------------------------------------
def chooseC(m):
    """
    Chooses a random number, 1 < c < m, and checks whether or not it is 
    coprime with the m, that is, gcd(c, m) = 1
    """
    while (True):
        for c in range(m, 2, -1):
        #print(c)

            if Euclidean_Algorithm(c, m) == 1:
                break

    return c



def gcd(c, m):
    """
    Performs the Euclidean algorithm and returns the gcd of c and m
    """
    if (m == 0):
        return c
    else:
        return gcd(c, c % m)

#--------------------------------------------------------------------------------------

def chooseD(c, m):
    """
        Chooses a random number, 0 <= d < m, and checks whether or not it is 
        coprime with the m, that is, gcd(c, m) = 1
    """
    k = 1
    while True:
 
        if isinstance( ((1 + (k*m))/c), int) ==  True:
            d = ((1 + (k*m))/c)
            break
        else:
            k = k+1 


    return d


def Euclidean_Algorithm(a, b):

    if a!=b:
        #.....
        if a > b:
            a = a-b
        else:
            b = b-a
    else:

        return a


#--------------------------------------------------------------------------------------


def main():
    while True:

        p_digit = int(input("Insert the p digit {It should be a prime number} : "))
        q_digit = int(input("Insert the q digit {It should be a prime number} : "))

        if control_input(p_digit) != True:
            logging.error(f"The number {p_digit} inserted isn't a prime number, retry")
        elif control_input(q_digit) != True:
            logging.error(f"The number {q_digit} inserted isn't a prime number, retry")
        else:
            break
    
    n_num = p_digit * q_digit
    print(n_num)
    m_num = lcm(p_digit-1, q_digit-1)
    print(m_num)
    c_num = chooseC(m_num)
    print(c_num)
    d_num = chooseD(c_num, m_num)
    print(d_num)

    # ------------------------------------- Find keys ----------------------------------

    pubblic_key = (n_num, c_num)

    private_key = (m_num, d_num)

    print(f" pubblic_key = {pubblic_key}, private_key = {private_key} ")

    massage = input("Input message : ")









    return
"""
for i in range (65,91):
    char2number[chr(i)] = i - 65
    number2char[i-65] = chr(i)
"""

if __name__ == "__main__":
    main()