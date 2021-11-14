import os

class _Getch:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return str(msvcrt.getch(), "utf-8")


getch = _Getch()



class effects:
	def damage(player, amount):
		actual = amount - player.ar
		if actual > 0:
			player.hp = player.hp - amount
	def heal(player, amount):
		player.hp = player.hp + amount
	def gain_ap(player, amount):
		player.ap = player.ap + amount
	def gain_mp(player, amount):
		player.mp = player.mp + amount
	def gain_ar(player, amount):
		player.ar = player.ar + amount
	def gain_pen(player, amount):
		player.pen = player.pen + amount
	def gain_mana(player, amount):
		player.mana = player.mana + amount
	def gain_gold(player, amount):
		player.gold = player.gold + amount
	
class items:
	class potions:
		def sheal(player):
			effects.heal(player, player.hp / 8)
		def heal(player):
			effects.heal(player, player.hp / 6)

class abilities:
	class attacks:
		def basic(attacker, defender):
			effects.damage(defender, attacker.ap)
		def lifesteal(attacker, defender):
			reduced = attacker.ap / 5
			actual = attacker.ap - reduced
			effects.damage(defender, actual)
			heal = actual / 5
			effects.heal(attacker, heal) 
		def slash(attacker, defender):
			actual = attacker.ap * 2
			selfdmg = actual / 4
			effects.damage(defender, actual)
			effects.damage(attacker, selfdmg)
		def combine(attacker, defender):
			actual = attacker.ap + attacker.mp
			actual = actual / 2
			hpred = defender.hp / 50
			actual = actual - hpred
			defender.hp = defender.hp - actual
	class stacking:
		def ap(attacker, defender):
			actual = attacker.ap / 3
			gain = actual / 5
			effects.damage(defender, actual)
			effects.gain_ap(attacker, gain)
		def ar(attacker, defender):
			actual = attacker.ap / 3
			gain = actual / 2
			effects.damage(defender, actual)
			effects.gain_ar(attacker, gain)
	class heals:
		def mp(user):
			if user.mana > 20:
				effects.heal(user, user.mp)
				effects.gain_mana(user, -20)
	class conversion:
		def ap_mp(user):
			ap = user.ap
			mp = user.mp
			add = ap / 5
			effects.gain_ap(user, 0 - add)
			effects.gain_mp(user, add)
			
		

class player:
	def __init__(self, name, abilities, ap, mp, ar, hp, pen, mana, gold):
		self.name = name
		self.abilities = abilities
		self.ap = ap
		self.mp = mp
		self.ar = ar
		self.hp = hp
		self.pen = pen
		self.mana = mana
		self.gold = gold
	def print(self):
		print("Name: ", self.name)
		print("Abilities: ", self.abilities)
		print("Attack power", self.ap)
		print("Magic power", self.mp)
		print("Armor: ", self.ar)
		print("Health: ", self.hp)
		print("Penetration", self.pen)
		print("Mana: ", self.mana)
		print("Gold: ", self.gold)

nigma = player("nigga", "xd", 80, 10, 10, 500, 0, 100, 0)
ligma = player("ligma", "xd", 10, 80, 10, 500, 0, 100, 0)

players = []
players.append(nigma)
players.append(ligma)

attacks = []
attacks.append(abilities.attacks.basic)
attacks.append(abilities.attacks.lifesteal)
attacks.append(abilities.attacks.slash)
attacks.append(abilities.attacks.combine)

stacks = []
stacks.append(abilities.stacking.ap)
stacks.append(abilities.stacking.ar)


while True:
	for num, player in enumerate(players):
		effects.gain_gold(player, 20)
		for player in players:
			print("-----------------------------------")
			player.print()
		print("-----------------------------------")
		player = players[num]
		if num == 0:
			enemy = players[1]
		else:
			enemy = players[0]
		print(str(num) + "-" + player.name, " choose action:")
		print("1 Attack")
		print("2 Stack")
		print("3 Heal")
		print("4 Convert")
		choice = getch()
		if choice == "1":
			print(">Choose Attack: ")
			print(" 1 Basic")
			print(" 2 Lifesteal")
			print(" 3 Slash")
			print(" 4 Combine")
			ab = int(getch())
			fn = attacks[ab - 1]
			fn(player, enemy)
		if choice == "2":
			print(">Choose stacking method")
			print(" 1 Attack power > Attack power")
			print(" 2 Attack power > Armor")
			ab = int(getch())
			fn = stacks[ab - 1]
			fn(player, enemy)
		if choice == "3":
			abilities.heals.mp(player)
		if choice == "4":
			abilities.conversion.ap_mp(player)
		os.system("cls")
		



