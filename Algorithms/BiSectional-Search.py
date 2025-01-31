def bisection_root(x):

    #Initialize veriables
    epsilon = 0.01
    low = 0
    high = x
    ans = (high + low)/2.0

    #Check if our guess is close enough
    while abs(ans**2 - x) >= epsilon:

        #update low or high
        #depends on guess too small or too large
        if ans**2 < x:
            low = ans
        else:
            high = ans
        
        #new value for guess
        ans = (high + low)/2.0
        
    return ans

def main():
    print(bisection_root(22))

if __name__ == '__main__':
    main()