from colorama import init, Fore, Back, Style
from hero import Hero
from mage import Mage
from warrior import Warrior
from fighter import Fighter
from tank import Tank
from maksman import MM
from moster import Moster

init(autoreset=True)
# fore = foregroun = warna teks
# Back= backround = warna latar belakang
print(Style.BRIGHT + Fore.WHITE + Back.BLUE + f"---summon semua hero---")
alucard = Warrior("alucard",10,100,100)
alok = Mage("alok",1,100,100)
Guenever = Fighter("Guenever",1,100,100)
hanabi = MM("hanabi",1,100,100)
tigreal = Tank("tigreal",1,100,100)

print(Style.BRIGHT + Fore.WHITE + Back.BLUE + f"---summon moster---\n")
salamander = Moster("salamander",100,1000,1000)

print(Style.BRIGHT + Fore.WHITE + Back.BLUE + f"---mulai duild party---\n")

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
alucard.hp = 240
hanabi.hp = -140
print(f"hp alucard: {alucard.hp}")
print(f"hp hanabi: {hanabi.hp}")
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
    try:
        aksi = int(input(">>pilih aksi:"))
    except ValueError:
        print("❌input eror, hanya boleh angka")

    if aksi == 1:
        dmg = 10
        # alucard.attack(salamander)
        # alok.attack(salamander)
        # Guenever.attack(salamander)
        # hanabi.attack(salamander)
        # tigreal.attack(salamander)
        # salamander.damaged(dmg * 1)
        for party in party:
            party.attack(salamander)
            salamander.damaged(dmg)
        # cek jika hp 0 = brakhir pertandingan
        # if (salamander.hp == 0):
        #     print('moster sudah mati')
        #     running = False
        if (salamander.hp == 0):
            print("Monster dah mati, dahan bee")
            running = False
    elif aksi == 2:
        alok.heal(10)
        
    elif aksi == 3:
        print('game berakhir')
        running = False
    else:
        print("⚠️  pilihan salah, hanya 1-3\n")