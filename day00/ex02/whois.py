import sys

if len(sys.argv) != 2 or not(sys.argv[1].isdigit()):
    print ("ERROR")
    sys.exit(0)

x = int(sys.argv[1])

if x == 0:
    print ("I'm Zero.")
elif (x % 2) == 0:
    print ("I'm Even.")
else :
    print ("I'm Odd.")
