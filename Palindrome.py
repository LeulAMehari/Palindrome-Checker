# AUthor: Leul Adane
# Finished 02/28/2023
# Purpose: This is a palindrome testing application in Python 
#          using the stack and queue Abstract data type.

from Stack import Stack
from Queue import Queue

def stackToReverseString(MyStack):
   #find length of string and add it to the stack to reverse it
   # toString
   string = ""
   while MyStack.peek() != None:
      i = MyStack.pop()
      string+=i

   return string
   # Return a string

def reverseStringAndRemoveNonAlpha(stringToReverse):
   # Add all Alpha characters from stringToReverse to onlyAphasString
   onlyAphasString = ""
   for character in stringToReverse:
      if character.isalpha():
         onlyAphasString+=character
   return onlyAphasString


def isPalindrome(stringToTest):
   # Push stringToTest onto myStack
   myStack = Stack()
   for i in stringToTest:
      myStack.push(i)

   # Push stringToTest onto myQueue
   myQueue = Queue()
   for i in stringToTest:
      myQueue.enqueue(i)

   check = True
   
   # Compare the string and queue by popping and dequing
   while myStack.peek() != None:
      stackData = myStack.pop()
      queueData = myQueue.dequeue()
      if stackData != queueData:
         # print(stringToTest + " is NOT a palindrome")
         check = False
         return check
         break
   if check == True:
      # print(stringToTest + " is a palindrome")
      return check
   
def explorePalindrome(stringToTest):
   #delete from right side and test for palindrome
   #convert stringToTest to a list
   listFromString = []
   listFromString[:0] = stringToTest
   newListRight = listFromString.copy()
   for i in newListRight:
      newListRight.pop()
      if len(newListRight) >= 3:
         # convert newListRight back to a string and call isPlindrome
         joinedString = ""
         joinedString=joinedString.join(newListRight)
         if isPalindrome(joinedString) == True:
            print("The substring : " + joinedString + " is a palindrome. Tested by removing from right.")
      else:
         break 

   #delete from left side and test for palindrome
   newListLeft = listFromString.copy()
   i=0
   while i < len(newListLeft):
      newListLeft.pop(0)
      if len(newListLeft) >= 3:
         # convert newListLeft back to a string and call isPlindrome
         joinedString = ""
         joinedString=joinedString.join(newListLeft)
         if isPalindrome(joinedString) == True:
            print("The substring : " + joinedString + " is a palindrome. Tested by removing from left.")
      else:
         break
      i+=1 

   #delete from both sides and test for palindrome
   newListBoth = listFromString.copy()
   i=0
   while i < len(newListBoth):
      newListBoth.pop(0)
      newListBoth.pop()
      if len(newListBoth) > 3:
         # convert newListBoth back to a string and call isPlindrome
         joinedString = ""
         joinedString=joinedString.join(newListBoth)
         if isPalindrome(joinedString) == True:
            print("The substring :  " + joinedString + " is a palindrome. Tested by removing from both sides.")
      else:
         break
      i+=1 


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~   User Input and Function Calling   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# asks for user input
userInput = input("Enter Here: ")
while userInput == "":
    print("The input is empty")
    userInput = input("Please enter the input here: ")
# pushes user input into a stack
num_stack = Stack()
num_stack.push(userInput)

# reverses the stack and receives a string
mystring = stackToReverseString(num_stack)

# pass the reversed string to revmove non-alpha characters.
onlyAphasString = reverseStringAndRemoveNonAlpha(mystring)

#pass the stripped string to isPalindrome
if isPalindrome(onlyAphasString) == True:
   print(onlyAphasString + " is a palindrome")
   #Check to see if there is a palindrome in the palindrome
   if isPalindrome(onlyAphasString) == True:
   print(onlyAphasString + " is a palindrome")
   #Check to see if there is a palindrome in the palindrome
   if (len(onlyAphasString))>1:
      explorePalindrome(onlyAphasString)

