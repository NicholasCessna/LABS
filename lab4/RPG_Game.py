# Lab 4 RPG

# I feel like this Lab could use extra time for a full logical implmentation. The logic I have works but I would like to have
# the time to think through all senarios and make sure the code implements and adjusts fully for all instances.
# I found myself wanting to do more on this lab and the last but I run out of time.
# I feel like I implemented it as described in the LAB outline and improvised where I needed to.

import random

class Item:
    def __init__(self, name, description = "", rarity = 'common'):
        self.name = name
        self.description = description
        self.rarity = rarity
        self._ownership = None
        
    def pick_up(self, player: str) -> str:
        self._ownership = player
        print(f"{self.name} is now owned by {player}")
    
    def throw_away(self) -> str:
        self._ownership = None
        print(f"{self.name} has been thrown away")
    
    def use(self) -> str:
        if self._ownership:
            print(f"{self.name} has been used by {self._ownership}")
            
            
        
    
class Weapon(Item):
    def __init__(self, name, damage, weapon_type, rarity='common'):
        super().__init__(name, rarity=rarity)
        self.damage = damage
        self.weapon_type = weapon_type
        self._equipped = False
        self.attack_modifier = 1.15 if rarity == 'legendary' else 1.0

    def equip(self) -> str:
        self._equipped = True
        print(f"{self.name} is equipped")

    def use(self) -> str:
        if self._equipped:
            damage_done = self.damage * self.attack_modifier
            print(f"{self.name} is used, dealing {damage_done} damage")
        else:
            print(f"{self.name} is not equipped and cannot be used")
            
            
            
        
class Shield(Item):
    def __init__(self, name, description, defense, rarity='common', broken=False):
        super().__init__(name, rarity=rarity, description=description)
        self.defense = defense
        self.broken = broken
        self._equipped = False
        self.defense_modifier = 1.1 if rarity == 'legendary' else 1.0
        self.broken_modifier = 0.5 if broken else 1.0

    def equip(self) -> str:
        self._equipped = True
        print(f"{self.name} is equipped")

    def use(self) -> str:
        if self._equipped:
            defense_value = self.defense * self.defense_modifier * self.broken_modifier
            print(f"{self.name} is used, blocking {defense_value} damage")
        else:
            print(f"{self.name} is not equipped and cannot be used")
            
            
        
        
# There wasnt a lot of infomation about the clothes subclass in the instructions. I made it give bonus defense and a 
# characteristic called durability. Further logic would need implemented to add the defense to futrue attacks and decrease in durability.
class Clothes(Item):
    def __init__(self, name, durability, bonus, rarity='common'):
        super().__init__(name, rarity=rarity)
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
    def __init__(self, name, potion_type, owner, rarity='common', value=0, effective_time=0):
        super().__init__(name, rarity=rarity)
        self.type = potion_type.lower()
        self.owner = owner
        self.empty = False
        self.value = value
        self.effective_time = effective_time
        
        if self.type not in ['attack', 'defense', 'hp']: # If anything other than the listed(from outline) is enetered it prints and deletes the potion instance
            print("That's a strange potion. It must just be water. Throw it away")
            del self

    def use(self) -> str:
        if not self.empty:
            self.empty = True
            if self.type == 'attack':
                if self.value == 0:  # I used random values for created potions if value is not set from_ability() method
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
        # Allows for ability created potion instances, logic in use() method makes sure of set values
        return cls(name, potion_type, owner, rarity='common', value=50, effective_time=30)




# Given Examples
long_bow = Weapon(name='Belthronding', damage=5000, weapon_type='bow', rarity='legendary')
long_bow.pick_up('Beleg')  # Belthronding is now owned by Beleg
long_bow.equip()  # Belthronding is equipped by Beleg
long_bow.use()  # Belthronding is used, dealing 5750 damage

broken_pot_lid = Shield(name='Wooden Lid', description='A lid made of wood, useful in cooking. No one will choose it willingly for a shield', defense=5, broken=True)
broken_pot_lid.pick_up('Beleg')  # Wooden Lid is now owned by Beleg
broken_pot_lid.equip()  # Wooden Lid is equipped by Beleg
broken_pot_lid.use()  # Wooden Lid is used, blocking 2.5 damage
broken_pot_lid.throw_away()  # Wooden Lid is thrown away
broken_pot_lid.use()  # NO OUTPUT

attack_potion = Potion.from_ability(name='Atk Potion Temp', owner='Beleg', potion_type='attack')
attack_potion.use()  # Beleg used Atk Potion Temp, and attack increased by 50 for 30s
attack_potion.use()  # NO OUTPUT

# My Own testing

sword1 = Weapon(name='Iron Sword', damage=50, weapon_type='sword')
sword1.pick_up('Nick')
sword1.use()
sword1.equip()
sword1.use()

sheild1 = Shield(name = "metal shield", description='A shield made of metal', defense=20)
sheild1.pick_up('Nick')
sheild1.use()
sheild1.equip()
sheild1.use()

clothes1 = Clothes(name='Leather Armor', durability=100, bonus='+10 defense')
clothes1.pick_up('Nick')
clothes1.use()
clothes1.equip()
clothes1.use()

potion1 = Potion(name='HP Potion', potion_type='HP', owner='Nick')
potion1.pick_up('Nick')
potion1.use()  
potion1.use()

potion2 = Potion(name='Attack Potion', potion_type='Attack', owner='Nick')
potion2.use()

potion3 = Potion(name='Defense Potion', potion_type='Defense', owner='Nick')
potion3.use()

potion4 = Potion(name= 'Strange Potion', potion_type='Strange', owner='Nick')


print(bool(sheild1._ownership))  
sheild1.throw_away()
print(bool(sheild1._ownership))


print(bool(sword1._ownership))  
sword1.throw_away()
print(bool(sword1._ownership))

