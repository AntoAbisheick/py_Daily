#Output 1->a=2->b=3->c
a = ['a','b','c']
#variable outside the loop
x =""
for i in range(0,len(a),1):
  x+=str(i+1)
  x+="->"
  x+=str(a[i])
  x+="="
print(x[0:len(x)-1])

#last sting value remove
x =""
for i in range(0,len(a),1):
  x+=str(i+1)
  x+="->"
  x+=str(a[i])
  x+="="
x=x[0:-1]
print(x)

#loop condition modify
for i in range(0,len(a),1):
  if i == len(a)-1:
    print(i+1,"->",a[i],sep="",end="")
  else:
    print(i+1,"->",a[i],"=",sep="",end="")





