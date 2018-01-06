
#
# I looked at this and though, ok 17 characters, simple.
# then I looked again and saw the single quote.  This is a great
# example of where pencil & paper fails.  Is that a syntax error?
# will it screw up the string?  Only god knows the answer.  lol
#

import sys

def main():

  aString = "What's even real?"

  stringLetters = len(aString)

  if(stringLetters > 15):
    print 20
  elif(stringLetters == 15):
    print 15
  else:
    print 1

  return 0

main()
