#Starting Test
import re
import sys

# file_to_read = "C:/Users/OscarRico/Documents/GitHub/file3.txt";
file_to_read = input("Enter the file path to use: ")
#C:/Users/OscarRico/Documents/GitHub/outputP1F3.txt
output_file = input("Enter the file path to use as output: ")
f= open(file_to_read, "r")
if f.mode == "r":
    fl1 = f.readline()
    fl1Arr = fl1.split()
    fl2 = f.readline()
    fl3 = f.readline()
    fl4 = f.readline()
    if len(fl1Arr) == 3:
        if 0 > int(fl1Arr[0]) > 50: sys.exit("Error: M1 need to be a number between 2 and 50")
        if 0 > int(fl1Arr[1]) > 50: sys.exit("Error: M2 need to be a number between 2 and 50")
        if 3 > int(fl1Arr[2]) > 5000: sys.exit("Error: N need to be a number between 3 and 5000")
    else:
        sys.exit('Error: the first line can only have 3 integers M1, M2 and N not more neither less')
    if len(fl2.strip()) != int(fl1Arr[0]):
        sys.exit("Error: the given character count for the first instruction is %s but the firts function have %s "
                 "characters"%(str(fl1Arr[0]), str(len(fl2.strip()))))
    if len(fl3.strip()) != int(fl1Arr[1]):
        sys.exit("Error: the given character count for the second instruction is %s but the second function have %s "
                 "characters"%(str(fl1Arr[1]), str(len(fl3.strip()))))
    if not re.search(r'^[A-Za-z0-9]+$', fl4):
        sys.exit("Error: The four line containing the message can only contain characters that fits the regex ["
                 "a-zA-Z0-9]")
    nfl4 = re.sub(r"(.)\1+", r"\1", fl4)
    if int(fl1Arr[2]) == int(len(nfl4.strip())):
        responses = ("No", "Si")
        f = open(output_file, "w+")
        f.write(responses[fl2.strip() in nfl4.strip()]+"\n")
        f.write(responses[fl3.strip() in nfl4.strip()]+"\n")
        f.close()
    else:
        print("Error: the number of characters of the message dont match")
else:
    print("can't read file, check permissions")