
# Process called exhaustive enumeration

# Applies to a problem where …
#  You are able to guess a value for solution
#  You are able to check if the solution is correct

# You can keep guessing until
#  Find solution or
#  Have guessed all values

# Given an int, call it x, want to see if there is another int which is its
# square root
# Start with a guess and check if it is the right answer
# To be systematic, start with guess = 0, then 1, then 2, etc

# Implementation of Newton-Raphson method
def squareRoot():
    guess = 0
    neg_flag = False
    x = int(input("Enter a positive integer: "))
    if x < 0:
        neg_flag = True
    while guess**2 < x:
        guess = guess + 1
    if guess**2 == x:
        print(f'Square root of {x} is {guess}')
    else:
        print(f'{x} is not a perfect square')
        if neg_flag:
            print(f'Just checking... did you mean {-x} ?')

def main():
    squareRoot()

if __name__ == '__main__':
    main()