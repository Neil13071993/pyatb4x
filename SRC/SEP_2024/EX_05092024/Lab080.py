class son():
    gold = "2kg"

class Father(son):
    diamond = "2 karat"

class grandfather(Father):
    btc = "10btc"

gf_obj = grandfather()
print(gf_obj.btc)