i= 0;
while i < 60:
    print(i);
    i += 1;

h = 0;
m = 0;
while m <= 60:
    print(h,":",m);
    if m == 59:
        h += 1;
        m = -1;
    if h == 24:
       break;
    m += 1;
    
