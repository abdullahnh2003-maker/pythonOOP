from hero import Hero

class Mage(Hero):
    def __init__(self , name ,level , hp, mana):
        #super() = memanggil class parent (hero)
        # set role secara mage
        super().__init__(name ,level , hp, mana , role="Mage")
        # print(f"💨 Hero {self.name} telah disummon")

    def critical(self, target):
        dmg = 50
        print(f"👹{target.name} terkene critical {dmg} DMG!")
        self.attack(target)
        target.damaged(dmg)
        

    def cast_spell(self, target):
        dmg = 10
        print(F"{self.name} menggunakan amgic attack")
        self.attack(target)
        target.damaged(dmg)