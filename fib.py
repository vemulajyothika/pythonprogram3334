def is_palidrome(s):
   s = s.replace(" ","").lower()
   return s == s[::-1]
string = input("Enter a string: ")
if is_palindrome(string):
    print(f'"(string)"is a palindrome.')
else:
          print(f'"(string)" is not a palindrome.')
