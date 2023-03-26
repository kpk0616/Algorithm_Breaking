import sys

n = int(sys.stdin.readline())

for i in range(0,n):
    reversed_str = ""
    input = sys.stdin.readline().split()
    for str in input:
        reversed_str += str[::-1]
        reversed_str += " "
    print(reversed_str)