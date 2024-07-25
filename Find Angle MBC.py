# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab = int(input()) 
bc = int(input())

angle_degrees = round(math.degrees(math.atan(ab/bc)))

t = chr(176) 
print(angle_degrees, end='') 
print(t)
