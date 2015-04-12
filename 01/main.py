for i in range (1,10):
    s = ""
    for j in range (i,10):
        s += str.format ("{0:1}*{1:1}={2:<3}",i,j,i*j)
    print(s)
    for k in range(1,i+1):
      print(end='       ')
    
