def bigger(a,b,c):
  if a>b:
    if a>c:
     print(a)
    else: 
     print(c)
  elif b>a:
   if b>c :
    print(b)
   else: 
    print(c)

a = int(input("enter the first no."))
b = int(input("enter the second no."))
c = int(input("enter the third no."))

bigger(a,b,c)

  