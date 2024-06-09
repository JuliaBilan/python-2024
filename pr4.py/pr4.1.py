class TimeSignature:
    def get_description(self):
        return 'Time signature'

class TwoFour(TimeSignature):
    def get_description(self):
        return "2/4"
    
class FourEight(TimeSignature):
    def get_description(self):
        return "4/8"
    
class ThreeFour(TimeSignature):
    def get_description(self):
        return "3/4"

class FourFour(TimeSignature):
    def get_description(self):
        return "4/4"

class ThreeEight(TimeSignature):
    def get_description(self):
        return "3/8"
     
class SixEight(TimeSignature):
    def get_description(self):
        return "6/8"

class Polka (TwoFour, FourEight):
    pass
class Sonata (FourFour, ThreeFour, ThreeEight):
    pass
class Marsh (TwoFour, FourEight):
    pass
class Walts (ThreeFour, SixEight):
    pass

sonata = Sonata()
polka = Polka()

print("Sonata", sonata.get_description())
print("Polka", polka.get_description())
