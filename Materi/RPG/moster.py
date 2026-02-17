
class Moster:
    def __init__(self,name: str,level: int, hp: int, mana: int):
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
            return False
        return True
    
    # tipe data saat return =>typedata
    def is_alive(self, status: bool) -> int:
        if self.hp > 0:
            return 1
        
        return 0
