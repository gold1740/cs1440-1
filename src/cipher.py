import sys
if len(sys.argv) <= 1:
	print("no file specified")
	exit(1)

# interpret rotation
if len(sys.argv) <= 2:
	rotation = "all"
else:
	rotation = int(sys.argv[2])


if rotation != "all":
    print("=======================")
    print("Rotated by", rotation, "positions")
    print("=======================")
    file = open(sys.argv[1])
    while True:
        a = file.readline()
        if a == "":
            file.close()
            break
        else:
            newLine = ""
            for i in a:
                z = 122 if i.islower() == True else 90
                if not i.isalpha():
                    newChar = i
                elif ord(i) + rotation <= z:
                    newChar = chr(ord(i) + rotation)
                else:
                    newChar = chr(ord(i) + rotation - 26)
                newLine += newChar
            print(newLine)

else:
    print("\n\nWhen no rotation distance is specified all 26 possible rotations are tried\n\n")
    for rotation in range(26):
         file = open(sys.argv[1])
         while True:
            a = file.readline()
            if a == "":
                file.close()
                break
            else:
                newLine = ""
                for i in a:
                    z = 122 if i.islower() == True else 90
                    if not i.isalpha():
                        newChar = i
                    elif ord(i) + rotation <= z:
                        newChar = chr(ord(i) + rotation)
                    else:
                        newChar = chr(ord(i) + rotation - 26)
                    newLine += newChar
                print(newLine)
