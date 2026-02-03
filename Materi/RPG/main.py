from hero import Hero
from mage import Mage
from warrior import Warrior
from fighter import Fighter
from tank import Tank
from maksman import MM
from moster import Moster

print("---summon semua hero---")
alucard = Warrior("alucard",10,100,100)
alok = Mage("alok",1,100,100)
Guenever = Fighter("Guenever",1,100,100)
hanabi = MM("hanabi",1,100,100)
tigreal = Tank("tigreal",1,100,100)

print("---summon moster---\n")
salamander = Moster("salamander",100,1000,1000)

print("---mulai duild party---\n")

party = [alucard, alok, Guenever, hanabi, tigreal]
print(f"komandan: pasukan siap")
print(f"total {len(party)} pahlawan")

# print('---raid game---')
# alucard.critical(salamander)
# alok.critical(salamander)
# alok.cast_spell(salamander)

# # pasang cheat hp +1000
# alucard.hp = 1000
# alucard.name = "bambang"
# # ambila hp doang
# print(f"hp alucard: {alucard.get_hp()}")
# alucard.set_hp(100)

# print(alucard)
# print(alok)
# print(Guenever)
# print(hanabi)
# print(tigreal)
# print(salamander)

running = True
while running:
    print(salamander)
    print("1. attack, 2. heal, 3. exit")
    
    aksi = int(input(">>pilih aksi:"))
    if aksi == 1:
        dmg = 10
        # alucard.attack(salamander)
        # alok.attack(salamander)
        # Guenever.attack(salamander)
        # hanabi.attack(salamander)
        # tigreal.attack(salamander)
        salamander.damaged(dmg * 4)
        for party in party:
            party.attack(salamander)
            salamander.damaged(dmg)
        # cek jika hp 0 = brakhir pertandingan
        # if (salamander.hp == 0):
        #     print('moster sudah mati')
        #     running = False
    elif aksi == 2:
        alok.heal(10)
        
    elif aksi == 3:
        print('game berakhir')
        running = False