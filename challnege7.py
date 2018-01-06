
# 
# this is a dump test


import sys

def Greetings(x):
# str function converts things into strings
# what does it do when it is given a string?
# apparently nothing.  Which is dumb.  Why would 
# you give a string to the str function?
#
  return "Hello, " + str(x) + "!"

def main():
 
  print Greetings("Michael")

  return 0

main()

