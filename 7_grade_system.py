fee = input("enter fare charges ").strip();
balance = input("enter card balance ").strip();
card_balance = int(balance);
fare_charge = int(fee);



if card_balance >= fare_charge:
  print("Welcome");
  print("New Card Balance =", card_balance - fare_charge);
elif card_balance > 0:
  print("Insufficient Balance");
  print("Available Balance =", card_balance);
else:
  print("Card Empty");
  
input();
