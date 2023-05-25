# Palindrome-Checker

This project is a Python application for testing palindromes using the stack and queue abstract data types (ADTs).
It provides a set of functionalities to determine if words or phrases are palindromes and also explores the possibility of 
creating new palindromes by decomposing phrases.

Getting Started
**To run the program, follow these steps:**

Clone the repository to your local machine.
Navigate to the palindrome directory.
Run the Palindrome.py file.


**Functionality**
The application consists of the following components:

**Stack Implementation**
The stack is implemented using the LinkedList data structure.
The Node class is utilized for creating nodes in the stack.


**Queue Implementation**
The queue is implemented using the LinkedList data structure.
The Node class is used for creating nodes in the queue.


Proper error handling is implemented for cases where peek or pop operations are called on an empty stack, 
also to handle cases where peek or dequeue operations are called on an empty queue.

**Palindrome Testing**
The stackToReverseString() function is implemented using the stack ADT. It converts a given input into a reversed string.
The reverseStringAndRemoveNonAlpha() function uses the stack ADT to reverse a given string while removing any non-alphabetic characters.
The isPalindrome() function checks whether a word or phrase is a palindrome by utilizing both the stack and queue ADTs.
The explorePalindrome() function, as a challenge, lists all possible backwards decompositions of a phrase, aiming to create new palindromes. 

