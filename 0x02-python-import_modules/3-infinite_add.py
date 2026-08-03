#!/usr/bin/python3

def infinite_add(argv):
    
    total = 0

    for i in range(1, len(argv)):
        total += int(argv[i])

    print(total)


if __name__ == "__main__":
    import sys
    infinite_add(sys.argv)
    

   
