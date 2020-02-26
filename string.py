my_str='albohphoBiA'
my_str=my_str.casefold()
rev_str=reversed(my_str)
print()
if list(my_str)==list(rev_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
