scores = [6,7,22,10,20,12,14,55,56,87,50,5.1];

n = len(scores);

Er = sum(scores);

print("sum of scores:",Er);

print("total no of scores:",n);

print("average score:",Er/n);

avg = Er/n;
for score in scores:
      if score >= avg:
          print (score);

input();


