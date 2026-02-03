
class Moster:
    def __init__(self,name,level, hp, mana):
        self.name =name
        self.leve =level
        self.hp =hp
        self.mana =mana
        print(f"💨 Moster {self.name} telah disummon")

    def __str__(self):
        status = "💚 hidup"
        if self.hp <= 0:
            status = "💔 mati"

        return f"[Moster] | hp: {self.hp}  |status: {status}"

    def damaged(self,damage):
        self.hp -= damage
        print(f"💥{self.name} terkena {damage} damage!\n")
        if self.hp == 0:
            print(f"🚫 {self.name} tereliminasi!")