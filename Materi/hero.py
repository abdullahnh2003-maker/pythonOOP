class Hero:
    #self = diri sendiri/internal
    #__init__
    def __init__(self,name,level, hp, mana , role):
        self.name =name
        self.leve =level
        self.hp =hp
        self.mana =mana
        self.role = role
        print(f"💨 Hero[{self.role}] {self.name} telah disummon")
    # mengganti print objek dr bentuk memori 0x100..
    #menjadi format string, biar lbh enak dibaca
    def __str__(self):
        status = "💚 hidup"
        if self.hp == 0:
            status = "💔 mati"

        return f"[{self.name}] | hp: {self.hp}  |status: {status}"

    def damaged(self,damage):
        self.hp -= damage
        print(f"💥{self.name} terkena {damage} damage!\n")
        if self.hp == 0:
            print(f"🚫 {self.name} tereliminasi!")

    def attack(self , enemy):
        print(f"⚔️ {self.name} menyerang {enemy.name}!")

    def heal(self, amount):
        self.hp += amount 
        print(f"💊{self.name} mendapat heal + {amount}\n")

    def critical(self, target):
        print(f"👹{self.name} terkena 0 DMG!")

    #panggil/summon heronya (buat objek)
# alucard = Hero("alucard", 10 ,100,100)
# eudora = Hero("eudora",10,100,100)
# print(alucard, eudora)
# print("-----BATTLE START----")
# alucard.attack(eudora)
# eudora.damaged(90)
# print(eudora)
# eudora.heal(50)
# print(eudora)
# #serang balik
# eudora.attack(alucard)
# alucard.damaged(80)
# alucard.damaged(5)
# print(alucard)
# alucard.heal(10)
# print(alucard)
# alucard.damaged(5)
# alucard.damaged(5)
# print(alucard)
# eudora.damaged(60)
# print(eudora)
# eudora.heal(3)
# eudora.critical(2)
# print(eudora)
# print(alucard)
