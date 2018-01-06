
import sys

def main():

  x = 30

# yest it is
  if (x > 29):
    sys.stdout.write("hi")
# yes it is true (non zero)
  if (x):
    sys.stdout.write("lo")
# nope
  else: 
    sys.stdout.write("ng")
# yes it is 
  if (x < 31):
    sys.stdout.write("ok")

  return 0

main()
