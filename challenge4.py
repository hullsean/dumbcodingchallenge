
# this future syntax allows you to access functionality 
# not officially available yet in current version of python
from __future__ import print_function


# kind of an interesting problem, shows recursion comprehension
# but also has syntax trickery, which I'm not a fan of.  Paper
# and pencil don't lend themselves to catching syntax errors.
# that's what an interpreter or compiler is for, people!
def divide_two_ten(arg):
  """arg: int"""

# first time through arg is 20
#  -- drop out at case #2 recurse arg 10
# second time through arg is 10
#  -- drop out at case #2 recurse arg 5
# third time through arg is 5
#  -- drop out at case #3 recurse arg 0
# fourth time through arg is 0
#  -- drop out at case #1 return arg 0 and don't recurse
#
# if we're at zero, don't recurse anymore (call it case #1)
  if arg == 0:
    return 0
# if we can divide by two with no remainder (call it case #2)
  if arg % 2 == 0:
    arg //= 2
# last case divide by 10 (drop remainder)  (call it case #3)
# trickery here, don't think 10 // 5 but 5 // 10.
  else:
    arg //= 10
  print (arg, end = "")
  return divide_two_ten(arg)



def func(arg):
  print("%d%d" % (divide_two_ten(arg), arg), end = "")

def main():
  func(20)

main()
