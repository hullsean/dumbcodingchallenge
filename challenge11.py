

#
# add elements 3 through 10 to an array myVector
# I guess this tests your knowledge that with a for
# loop, you i=10 is where the loop stops (non-inclusive)
# So there are 7 elements between 3 & 10, not 8.
# [3],[4],[5],[6],[7],[8],[9]   <--- YES!
# [3],[4],[5],[6],[7],[8],[9],[10]   <--- NO!
#
def main():
  myVector = []

  for i in range(3,10):
    myVector.append(i)

  print(len(myVector))

main()
