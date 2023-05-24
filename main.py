#enter answer here

n = str(input(""))
three = n.split()
one = int(three[0])
two = int(three[1])
tree = int(three[2])
if one > 0 and two > 0 and tree > 0 and (one+two+tree)==180:
    print("Yes")
else:
    print("No")
