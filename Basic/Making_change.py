#Making change giving machine in indian rs
note_2000 = 2000
note_500 = 500
note_200 = 200
note_100 = 100
note_50 = 50
note_20 = 20
note_coin_10 = 10
coin_5 = 5
coin_2 = 2
coin_1 = 1

cash = int(input("Enter the ammount: "))

print("",cash//note_2000,"2000")
cash = cash%note_2000

print("",cash//note_500,"500")
cash = cash%note_500

print("",cash//note_200,"200")
cash = cash%note_200

print("",cash//note_100,"100")
cash = cash%note_100

print("",cash//note_50,"50")
cash = cash%note_50

print("",cash//note_20,"20")
cash = cash%note_20

print("",cash//note_coin_10,"10")
cash = cash%note_coin_10

print("",cash//coin_5,"5")
cash = cash%coin_5

print("",cash//coin_2,"2")
cash = cash%coin_2

print("",cash//coin_1,"1")
cash = cash%coin_1

