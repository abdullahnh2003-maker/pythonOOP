# import inin untk typehint bisa bekerja
from __future__ import annotations
from moster import Moster

class Hero:
    #self = diri sendiri/internal
    #__init__ = dipanggil 2 kali
    def __init__(self, name: str, level: int, hp: int, mana: int, role: str):
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

    def damaged(self,damage: int):
        self.__hp -= damage
        print(f"💥{self.name} terkena {damage} damage!\n")
        if self.__hp == 0:
            print(f"🚫 {self.name} tereliminasi!")

    def attack(self , enemy: Moster):
        print(f"⚔️ {self.name} menyerang {enemy.name}!")

    def heal(self, amount: int):
        self.__hp += amount 
        print(f"💊{self.name} mendapat heal + {amount}\n")

    def critical(self, target: Moster):
        print(f"👹{self.name} terkena 0 DMG!")

    # getter : mengambil attriibutt yg privat
    def get_hp(self):
        return self.hp

    # setter : memperbarui atribut yg privat
    # tambah validasi jgn sampai lewat max 100 hp
    def set_hp(self, add_hp):
        self.__hp += add_hp
    
    # @property = alternatif getter dan setter modern
    @property
    def hp(self):
        return self._hp
    
    # setter =>/ nama property setter
    @hp.setter
    def hp(self, value):
        if value < 0: #validasi hp minus
            value = 0
        
        self._hp = value