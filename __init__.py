from SPF import *

print("Welcome to the Symmetric Polynomial Factorization (SPF) tool! Please enter a polynomial in the format '[coeff][var1, var2, ...] + [coeff][var1, var2, ...]' etc. Type 'exit' to quit.")

while True:
    string = input(">> ")
    if string == "exit":
        break
    try:
        pol = Polynomial.to_Polynomial(string)
        print(SPF(pol))
    except Exception as e:
        print(f"Error: {e}")