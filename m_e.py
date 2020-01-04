def epsilon(x):
 check = False
 z=x+1
 if z<=1:
   print("machine epsilon: ",x)
   return
  
 else:
   while check==False:
     x=x/10
     z=1+x
     if z<=1:
       check=True
       print("machine epsilon: ",x)
       return


x=0.5
epsilon(x)
