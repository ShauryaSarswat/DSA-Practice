def power_of_two(n):
    # If n==1 return True
    if n==1:
        return True
    # If n==0 return False
    elif n==0:
        return False
    # If n is odd return False
    elif n%2!=0:
        return False
    # Recursive call to function
    return  power_of_two(n/2)

if __name__ == '__main__':
    n = int(input())
    ans = power_of_two(n)
    print(ans)