class GF:
    def car(self):
        return "old_car"


class F(GF):
    def car(self):
        return "Honda_City"

class S(F):
    def car(self):
        return "Lamborginy"

son = S()
print(son.car())
