class Hero:
    #self = diri sendiri/internal
    #__init__ = dipanggil 2 kali
    def __init__(self,name,level, hp, mana , role):
        self.name =name
        self.leve =level
        self.__hp =hp
        self.mana =mana
        self.role = role
        print(f"💨 Hero[{self.role}] {self.name} telah disummon")
    # mengganti print objek dr bentuk memori 0x100..
    #menjadi format string, biar lbh enak dibaca
    def __str__(self):
        status = "💚 hidup"
        if self.__hp <= 0:
            status = "💔 mati"

        return f"[{self.name}] | hp: {self.__hp}  |status: {status}"

    def damaged(self,damage):
        self.__hp -= damage
        print(f"💥{self.name} terkena {damage} damage!\n")
        if self.__hp == 0:
            print(f"🚫 {self.name} tereliminasi!")

    def attack(self , enemy):
        print(f"⚔️ {self.name} menyerang {enemy.name}!")

    def heal(self, amount):
        self.__hp += amount 
        print(f"💊{self.name} mendapat heal + {amount}\n")

    def critical(self, target):
        print(f"👹{self.name} terkena 0 DMG!")

    # getter : mengambil attriibutt yg privat
    def get_hp(self):
        return self.hp
    
    # tambah validasi jgn sampai lewat max 100 hp
    def set_hp(self, add_hp):
        self.__hp += add_hp


