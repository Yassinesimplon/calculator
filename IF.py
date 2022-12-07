print("welcome in my calculatrice <3")
op= int(input("input ur choice : \n 1 for +\n 2 for*\n 3 for / \n 4 for -\n"))


x=input("number one=")
y=input("number two =")

if op == 1 :

   resultat=(int(x)+int(y))
   print("le resultat  de :"+x+ "+" +y+"="+str(resultat))
elif op == 2 :
  resultat=(int(x)*int(y))
  print("le resultat  de :"+x+ "*" +y+"="+str(resultat))
elif op == 3 :
  resultat=(int(x)/int(y))
  print("le resultat  de :"+x+ "/" +y+"="+str(resultat))
elif op == 4 :
   resultat=(int(x)+-int(y))
   print("le resultat  de :"+x+ "-" +y+"="+str(resultat))
else : 
    print("no result")



