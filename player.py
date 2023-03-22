def isPalindrome(str):
  for i in range(0, int(len(str)/2)):
    if str[i] != str[len(str)-i-1]:
      return False
  return True

stringading ='hello'

apexstringading = 'racecar'
answer1 = isPalindrome(apexstringading)
answer2 = isPalindrome(stringading)
# isPalindrome(stringading)

# isPalindrome(apexstringading)
if (answer2):
  print("yessir")
else:
  print("nossir")

if (answer1):
  print("yessir")
else:
  print("nossir")