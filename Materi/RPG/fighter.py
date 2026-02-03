from hero import Hero

class Fighter(Hero):
    def __init__(self , name ,level , hp, mana):
        #super() = memanggil class parent (hero)
        # set role secara mage
        super().__init__(name ,level , hp, mana , role="Fighter")
        # print(f"💨 Hero {self.name} telah disummon")

    def critical(self, target):
        dmg = 70
        print(f"{self.name} menggunakan: GIGANTIC SLASH!!")
        print(f"👹{target.name} terkene critical {dmg} DMG!")
        self.attack(target)
        target.damaged(dmg)
        