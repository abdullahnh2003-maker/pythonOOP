from hero import Hero

class Tank(Hero):
    def __init__(self , name ,level , hp, mana):
        #super() = memanggil class parent (hero)
        # set role secara mage
        super().__init__(name ,level , hp, mana , role="Tank")
        # print(f"💨 Hero {self.name} telah disummon")

    def critical(self, target):
        dmg = 30
        print(f"{self.name} menggunakan: GIGANTIC SLASH!!")
        print(f"👹{target.name} terkene critical {dmg} DMG!")
        self.attack(target)
        target.damaged(dmg)
        