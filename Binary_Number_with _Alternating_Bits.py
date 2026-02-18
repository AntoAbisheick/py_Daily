n = 5
s = bin(n)[2:]
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        print("False")
        break
else:
    print("False")


# ^,XOR,Returns 1 if bits are different.
# &,AND,Returns 1 if both bits are 1.
# |,OR,Returns 1 if at least one bit is 1.
# >>,Right Shift,Moves bits to the right (divides by 2).
# <<,Left Shift,Moves bits to the left (multiplies by 2).

n = n ^ (n >> 1)
if(n & (n + 1) == 0):
    print("True")
else:
    print("False")