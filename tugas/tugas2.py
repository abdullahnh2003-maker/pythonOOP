class Hero:
    def __init__(self, name, job, hp, hero_type="hero"):
        self.name = name
        self.job = job
        self.hp = hp
        self.type = hero_type
        print(f"✨ {self.name} memasuki arena!")

    def __str__(self):
        status = "💚 hidup"
        if self.hp <= 0:
            status = "☠️  mati"

        return f"[{self.name}] | hp: {self.hp} | status: {status}"
    


    def ulti(self, enemy):
        # dmg = 50
        print(f"{self.name} menyerang {enemy.name} damage ")
        # enemy.take_damage(dmg)

    def take_damage(self, damage):
        # TODO:
        self.hp -= damage
        print(f"{self.name} menerima damage {damage}")

        if self.hp <= 50 and self.name == "lord":
          print("😈 Raja Iblis memasuki RAGE MODE!")


    def heal(self, nambah):
        # TODO:
        self.hp += nambah
        print(f"{self.name} nambah darah {nambah}")
        # - heal sesuai role
        pass

    def tabrak(self, enemy):
        print(f"{self.name} menyerang {enemy.name}")
    
   

    def attack(self , enemy):
        print(f"⚔️ {self.name} menyerang {enemy}!")

    def critical(self, enemy):
        dmg = 40
        print(f"💥 {self.name} CRITICAL ke {enemy.name} ({dmg} DMG)")
        enemy.take_damage(dmg)

        
    def ngamuk(self):
     if self.hp <= 50:
        print("😈 Raja Iblis memasuki RAGE MODE (serius)!!!")


alpha = Hero(f"alpha", "jungler", 100)
miya = Hero(f"miya", "goldliner", 100)
jonson = Hero(f"jonson", "roamer", 100)
vale = Hero(f"vale", "midliner", 100)
zilong = Hero(f"zilong", "solo push", 100)
turtle = Hero(f'turtle', "moster mini", 200)
lord = Hero(f"lord", "apajalah", 300)
print("----------------------")

print('----party hero----')
party = [alpha, miya, jonson, vale, zilong]
print(f"komandan: pasukan siap")
print(f"total {len(party)} pahlawan \n")

print(f'muncul {turtle} ke arena \n')

print('---pertempuran pertama---')
zilong.attack(turtle)
turtle.take_damage(20)
vale.attack(turtle)
turtle.take_damage(30)
alpha.ulti(turtle)
vale.ulti(turtle)
turtle.take_damage(100)
print(turtle)
print(f'\n karena darah turtle sisa 50 dia berubah menjadi lord')
print(lord)

print('\n ---peperangan ke 2 ---')
alpha.attack(lord)
lord.take_damage(10)
miya.attack(lord)
lord.take_damage(15)
jonson.tabrak(lord)
lord.take_damage(30)
vale.ulti(lord)
alpha.ulti(lord)
miya.ulti(lord)
lord.take_damage(130)
lord.attack(party)
jonson.take_damage(50)
vale.take_damage(50)
alpha.take_damage(50)
miya.take_damage(50)
zilong.take_damage(50)
print(lord)
print(vale)
print(alpha)
print(miya)
print(jonson)
print(zilong)
jonson.heal(20)
miya.heal(20)
alpha.heal(20)
zilong.heal(20)
vale.heal(20)
lord.heal(10)

jonson.tabrak(lord)
lord.take_damage(30)
alpha.critical(lord)
lord.heal(5)
print(lord)

lord.attack(miya)
miya.take_damage(70)
print(miya)

print('serangan terakhir dari alpha dan vale')
vale.ulti(lord)
alpha.ulti(lord)
lord.take_damage(60)
print(lord)
print(miya)
print(vale)
print(alpha)
print(jonson)
print(zilong)

print('\n selesai peperangan yg mengorbankan 1 hero yg gugur pada medan peperangan')