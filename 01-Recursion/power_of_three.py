def power_checker(n):
    # If n==0 return False
    if n<=0:
        return False
    # If n is divisible by 3 return recursive call
    if n%3==0:
        return power_checker(n/3)
    # If n==1 return True
    if n==1:
        return True
    # If still undevisible then return False
    return False 

if __name__ == '__main__':
    n = int(input())
    ans = power_checker(n)
    print(ans)