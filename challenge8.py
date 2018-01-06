
# python's True & False integer values take their history 
# from Unix, where you have the true and false commands 
# at the command line.  Along with $? 

import sys

def main():
  x= 1

  # True is 1 and False is 0
  if (True > False):
    # yes it does
    if(x == True):
      # yes false is zero so less than 1
      if(False < x):
        print 2
      # false is not equal to or greater than x
      else:
        print 5
    # True is 1, not another value
    else:
      print 1
  # reserved word True is always greater than reserved word False
  else:
    print 3

  return 0

main()
