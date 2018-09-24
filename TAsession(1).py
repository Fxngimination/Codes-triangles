sym = ("*")
mult = 1
count = 6
# while mult <= count:
#     print (sym*mult)
#     mult = mult+1


while mult<= count:
    print (" " * ( count - mult) + "*" * mult);
    mult = mult+1

row = 5
for i in range(0,row):
    print(""*(row + 1-i)+"*"* (i+1))
    for i in range(row,0-1,-1):
    print(""*(row + 1-i)+ "*"* (i+1))