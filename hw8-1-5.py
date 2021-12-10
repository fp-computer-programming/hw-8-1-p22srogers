# Author: SMR (AMDG) 12/10/21
def palindrome(word):
    if word == word[:: -1]:
        print("The word {0} is a palindrome because {0} spelled backwards is {0}.".format(word))
    else:
        print("The word " + word + " is not a palindrome because " + word + " spelled backwards is " + word[:: -1] + ".".format(word))
palindrome("refer")
palindrome("spaceship")
palindrome("monkey")