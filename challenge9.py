
#
# this test is dumb.  We append 5 elements to an array
# then return & print the arr in order.
# what's complicated here?

def array_populate(myArray):
  myArray.append(1)
  myArray.append(5)
  myArray.append(19)
  myArray.append(21)
  myArray.append(14)

def main():
  arr = []
  array_populate(arr)
  print (arr)

main()
