# I opted for an updated inheritance heiracrhy instead of duck typing so I just built off of the existing weapons subclass.
# I felt this a good way to go because it is easy to add new weapon types and weapon moves in the future
# Added unique output for each type of legendary Item and added a new item type for categorizing items. I used a default __str__ in the Item 
# for legendary Items that is over ridden by __str__ in each subclass depending on the Item type. The output is accompanied by some unicode emojis 
# I found online.
# Please read my note for the examples provieded I added at the bottom for my view methoed and the implmentation of "item" AND "item_type"
# I added nots to my view method for this because it didnt align with the given examples but this way you can view a specific item or all of that type. 
# Sorry for all of the notes.

import random


class Item:
    def __init__(self, name, description="", rarity='common', item_type="general"):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.item_type = item_type  
        self._ownership = None
    
    def __str__(self):
        if self.rarity == 'legendary':
            return f"\n*** {self.name} (Legendary Item) ***{self.description}\n"
        return f"{self.name} ({self.rarity}) - {self.description}"

    def pick_up(self, player: str) -> str:
        self._ownership = player
        print(f"{self.name} is now owned by {player}")
    
    def throw_away(self) -> str:
        self._ownership = None
        print(f"{self.name} has been thrown away")
    
    def use(self) -> str:
        if self._ownership:
            print(f"{self.name} has been used by {self._ownership}")
        else:
            print(f"{self.name} cannot be used because it is not owned by anyone")


# Weapon Class handles what is common to all subclasses of weapons
class Weapon(Item):
    def __str__(self):
        if self.rarity == 'legendary':
            return f"⚔️ *** {self.name} (Legendary Weapon) ***  {self.description}: This weapon holds untold power!"
        return super().__str__()

    def __init__(self, name, damage, weapon_type, rarity='common'):
        super().__init__(name, rarity=rarity, item_type='weapon')
        self.damage = damage
        self.weapon_type = weapon_type
        self._equipped = False
        self.attack_modifier = 1.15 if rarity == 'legendary' else 1.0

    def equip(self) -> str:
        self._equipped = True
        print(f"{self.name} is equipped")

    def use(self) -> str:
        if self._equipped and self._ownership:
            attack_move = self.attack_move()
            damage_done = self.damage * self.attack_modifier
            print(f"{self._ownership} {attack_move}\n{self.name} deals {damage_done} damage")
        else:
            print(f"{self.name} is not equipped or has no owner and cannot be used")

    # Works as the def of the attack_move() interface in the subclasses. Will allow for argument
    # to be passed to use different attack moves if you would like to add them to each weapon type`s class
    def attack_move(self, move=None):
        if move:
            return move()
        return "Default attack move not implemented"
    
    
# Extened Weapon inheritance to these subclasses
class SingleHandedWeapon(Weapon):
    def __str__(self):
        if self.rarity == 'legendary':
            return f"🗡️🗡️🗡️ *** {self.name} (Legendary Single-Handed Weapon) The mightiest of all blades, capable of felling enemies with a single slash!*** 🗡️🗡️🗡️ "
        return super().__str__()    
    
    def attack_move(self, move=None):
        # If a specific move is passed, use that; otherwise, default to _slash()
        if move:
            return move()
        return self._slash()

    def _slash(self):
        return f"slashes the enemy!"

    def _stab(self):
        return f"stabs the enemy!"
    

class DoubleHandedWeapon(Weapon):
    def __str__(self):
        if self.rarity == 'legendary':
            return f"🪓🪓🪓 *** {self.name} (Legendary Double-Handed Weapon) A weapon of massive strength, spinning with devastating force!*** 🪓🪓🪓 "
        return super().__str__()
    
    def attack_move(self, move=None):
        if move:
            return move()
        return self._spin()

    def _spin(self):
        return f"spins through the enemy!"
    

class Pike(Weapon):
    def __str__(self):
        if self.rarity == 'legendary':
            return f"🔱🔱🔱 *** {self.name} (Legendary Pike): With the power to pierce, this pike never misses its mark! *** 🔱🔱🔱"
        return super().__str__()
    
    def attack_move(self, move=None):
        if move:
            return move()
        return self._thrust()

    def _thrust(self):
        return f"thrusts at the enemy!"


class RangedWeapon(Weapon):
    def __str__(self):
        if self.rarity == 'legendary':
            return f"🏹🏹🏹 *** {self.name} (Legendary Ranged Weapon): A weapon of precision, its arrows strike without fail! *** 🏹🏹🏹 "
        return super().__str__()
    
    def attack_move(self, move=None):
        if move:
            return move()
        return self._shoot()

    def _shoot(self):
        return f"shoots at the enemy!"


class Shield(Item):
    
    def __str__(self):
        if self.rarity == 'legendary':
            return f"🛡️🛡️🛡️ *** {self.name} (Legendary Shield) *** {self.description}: A high degree of protection! 🛡️🛡️🛡️"
        return super().__str__()

    def __init__(self, name, description, defense, rarity='common', broken=False):
        super().__init__(name, rarity=rarity, description=description, item_type='shield')
        self.defense = defense
        self.broken = broken
        self._equipped = False
        self.defense_modifier = 1.1 if rarity == 'legendary' else 1.0
        self.broken_modifier = 0.5 if broken else 1.0

    def equip(self) -> str:
        self._equipped = True
        print(f"{self.name} is equipped")

    def use(self) -> str:
        if self._equipped and self._ownership:
            defense_value = self.defense * self.defense_modifier * self.broken_modifier
            print(f"{self._ownership} uses {self.name}, blocking {defense_value} damage")
        else:
            print(f"{self.name} is not equipped or has no owner and cannot be used")



class Clothes(Item):
    def __str__(self):
        if self.rarity == 'legendary':
            return f"👕👕👖👖 *** {self.name} (Legendary Clothes) *** These clothes offer unmatched protection and durability!👕👕👖👖"
        return super().__str__()

    def __init__(self, name, durability, bonus, rarity='common'):
        super().__init__(name, rarity=rarity, item_type='clothes')
        self.durability = durability
        self.bonus = bonus
        self._equipped = False

    def equip(self) -> str:
        self._equipped = True
        print(f"{self.name} is equipped, providing {self.bonus}")

    def use(self) -> str:
        if self._equipped:
            print(f"{self.name} is used with bonus {self.bonus} and {self.durability} durability left")
        else:
            print(f"{self.name} is not equipped")


class Potion(Item):
    
    def __str__(self):
        if self.rarity == 'legendary':
            return f"🍶🍶🍶 *** {self.name} (Legendary Potion) *** {self.description}: This potion can heal even the gravest wounds!🍶🍶🍶"
        return super().__str__()

    def __init__(self, name, potion_type, owner, rarity='common', value=0, effective_time=0):
        super().__init__(name, rarity=rarity, item_type='potion')
        self.type = potion_type.lower()
        self.owner = owner
        self.empty = False
        self.value = value
        self.effective_time = effective_time

    def use(self) -> str:
        if not self.empty and self.owner:
            self.empty = True
            if self.type == 'attack':
                if self.value == 0:  
                    self.value = random.randint(30, 60)
                self.effective_time = 30 if self.effective_time == 0 else self.effective_time
                print(f"{self.owner} used {self.name}, and attack increased by {self.value} for {self.effective_time} seconds")
            elif self.type == 'defense':
                if self.value == 0:  
                    self.value = random.randint(30, 60)
                self.effective_time = 30 if self.effective_time == 0 else self.effective_time
                print(f"{self.owner} used {self.name}, and defense increased by {self.value} for {self.effective_time} seconds")
            elif self.type == 'hp':
                if self.value == 0:
                    self.value = random.randint(30, 60)
                print(f"{self.owner} used {self.name}, and HP increased by {self.value}")
        else:
            print(f"{self.name} is empty")

    @classmethod
    def from_ability(cls, name, owner, potion_type):
        return cls(name, potion_type, owner, rarity='common', value=50, effective_time=30)


# Using "Has A" relationship. Inventory Class "Has A" Item of different types.
class Inventory:
    
    def __init__(self, owner=None):
        self.owner = owner
        self.items = []

    def add_item(self, item: Item):
        item.pick_up(self.owner)
        self.items.append(item)
        print(f"{item.name} has been added to {self.owner}'s backpack.")

    def drop_item(self, item: Item):
        if item in self.items:
            item.throw_away()
            self.items.remove(item)
            print(f"{item.name} has been removed from {self.owner}'s backpack.")
        else:
            print(f"{item.name} is not in the backpack.")

    def view(self, item=None, item_type=None):
        if item:
        # If a specific item object is passed print that item if it exists in the inventory
            if item in self.items:
                print(item)
            else:
                print(f"{item.name} is not in the backpack.")
        elif item_type:
        # If an item_type is passed filter and print all items of that type
            filtered_items = [item for item in self.items if item.item_type == item_type]
            for item in filtered_items:
                print(item)
        else:
        # If neither is passed print all items
            for item in self.items:
                print(item)


    def __iter__(self):
        return iter(self.items)
    

    def __contains__(self, item):
        return item in self.items
    
    

# Examples
beleg_backpack = Inventory(owner='Beleg')

master_sword = SingleHandedWeapon(name='Master Sword', damage=300, weapon_type='sword', rarity='legendary')
muramasa = DoubleHandedWeapon(name='Muramasa', damage=580, weapon_type='katana', rarity='legendary')
gungnir = Pike(name='Gungnir', damage=290, weapon_type='spear', rarity='legendary')
belthronding = RangedWeapon(name='Belthronding', damage=500, weapon_type='bow', rarity='legendary')
hp_potion = Potion(name='Health Potion', potion_type='hp', owner='Beleg', rarity='legendary')
broken_pot_lid = Shield(name='Broken Pot Lid', description='A broken lid from a pot', defense=5, broken=True)
round_shield = Shield(name='Round Shield', description='A strong round shield', defense=100, rarity='legendary')

beleg_backpack = Inventory(owner = 'Beleg')
beleg_backpack.add_item(belthronding)
beleg_backpack.add_item(hp_potion)
beleg_backpack.add_item(master_sword)
beleg_backpack.add_item(broken_pot_lid)
beleg_backpack.add_item(muramasa)
beleg_backpack.add_item(gungnir)
beleg_backpack.add_item(round_shield)
beleg_backpack.view(item_type= 'shield') # ***PLEASE READ***I have an "item_type" (like "shield" or "weapon") in my view method and an item (like "master_sword") to view specific Items this is important for this test code.
beleg_backpack.view()
beleg_backpack.drop_item(broken_pot_lid)
if master_sword in beleg_backpack:
    master_sword.equip()
    print(master_sword)
# message to show off your legendary item
master_sword.use()
# Beleg slash using master sword
# master sword is used dealing 345 damage
for item in beleg_backpack:
    if isinstance(item, Weapon):
        beleg_backpack.view(item = item)


# beleg_backpack.view(item_type='shield')
# print("\n")

# beleg_backpack.view()
# print("\n")

# muramasa.pick_up("Nick")
# muramasa.equip()
# muramasa.use()

# beleg_backpack.drop_item(broken_pot_lid)

# for item in beleg_backpack:
#     if isinstance(item, Shield):
#         print(item)
# print("\n")


# if master_sword in beleg_backpack:
#     master_sword.equip()
#     print(master_sword)
#     master_sword.use()  # Output: "Beleg slashes the enemy!
# print("\n")


# if hp_potion in beleg_backpack:
#     hp_potion.use()
# print("\n")


# for item in beleg_backpack:
#     if isinstance(item, Weapon):
#         print(item)
# print("\n")
    
    
# for item in beleg_backpack:
#     if  isinstance(item, Potion):
#         print(item)
# print("\n")

    
# for item in beleg_backpack:
#     if isinstance(item, Shield):
#         print(item)


# long_bow = Weapon(name='Belthronding', damage=5000, weapon_type='bow', rarity='legendary')
# long_bow.pick_up('Beleg')  # Belthronding is now owned by Beleg
# long_bow.equip()  # Belthronding is equipped by Beleg
# long_bow.use()  # Belthronding is used, dealing 5750 damage

# broken_pot_lid = Shield(name='Wooden Lid', description='A lid made of wood, useful in cooking. No one will choose it willingly for a shield', defense=5, broken=True)
# broken_pot_lid.pick_up('Beleg')  # Wooden Lid is now owned by Beleg
# broken_pot_lid.equip()  # Wooden Lid is equipped by Beleg
# broken_pot_lid.use()  # Wooden Lid is used, blocking 2.5 damage
# broken_pot_lid.throw_away()  # Wooden Lid is thrown away
# broken_pot_lid.use()  # NO OUTPUT

# attack_potion = Potion.from_ability(name='Atk Potion Temp', owner='Beleg', potion_type='attack')
# attack_potion.use()  # Beleg used Atk Potion Temp, and attack increased by 50 for 30s
# attack_potion.use()  # NO OUTPUT

# # My Own testing

# sword1 = Weapon(name='Iron Sword', damage=50, weapon_type='sword')
# sword1.pick_up('Nick')
# sword1.use()
# sword1.equip()
# sword1.use()

# sheild1 = Shield(name = "metal shield", description='A shield made of metal', defense=20)
# sheild1.pick_up('Nick')
# sheild1.use()
# sheild1.equip()
# sheild1.use()

# clothes1 = Clothes(name='Leather Armor', durability=100, bonus='+10 defense')
# clothes1.pick_up('Nick')
# clothes1.use()
# clothes1.equip()
# clothes1.use()

# potion1 = Potion(name='HP Potion', potion_type='HP', owner='Nick')
# potion1.pick_up('Nick')
# potion1.use()  
# potion1.use()

# potion2 = Potion(name='Attack Potion', potion_type='Attack', owner='Nick')
# potion2.use()

# potion3 = Potion(name='Defense Potion', potion_type='Defense', owner='Nick')
# potion3.use()

# potion4 = Potion(name= 'Strange Potion', potion_type='Strange', owner='Nick')


# print(bool(sheild1._ownership))  
# sheild1.throw_away()
# print(bool(sheild1._ownership))


# print(bool(sword1._ownership))  
# sword1.throw_away()
# print(bool(sword1._ownership))
