import random
import json


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
        
    
            
    def to_json (self):
        return {
            'name': self.name,
            'description': self.description,
            'rarity': self.rarity,
            'item_type': self.item_type,
            'ownership': self._ownership
        }
    
    @classmethod
    def from_json (cls, data):
        
        """
        Creates a new Item instance from a JSON string.

        Input:
            data: The JSON string representing an item by its attributes.

        Returns:
            Item: A new object from the Item class created from the JSON data.
        """
        
        item = cls(data['name'], data['description'], data['rarity'], data['item_type'])
        item._ownership = data['ownership']
        return item


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

    def attack_move(self, move=None):
        if move:
            return move()
        return "Default attack move not implemented"
    
    def to_json(self):
        data = super().to_json()
        data.update({
            'damage': self.damage,
            'weapon_type': self.weapon_type,
            '_equipped': self._equipped,
            'attack_modifier': self.attack_modifier
        })
        return data
        
    @classmethod
    def from_json(cls, data):
        
        """
        Creates a new Weapon instance from a JSON string.

        Input:
            data: The JSON string representing a weapon by its attributes.

        Returns:
            Weapon: A new object from the Weapon class created from the JSON data.
        """
        
        weapon = cls(name = data['name'], damage = data['damage'], weapon_type= data['weapon_type'], rarity = data['rarity'])
        weapon. _equipped = data['_equipped']
        weapon.attack_modifier = data['attack_modifier']
        return weapon
    
        
    
    
class SingleHandedWeapon(Weapon):
    def __str__(self):
        if self.rarity == 'legendary':
            return f"🗡️🗡️🗡️ *** {self.name} (Legendary Single-Handed Weapon) The mightiest of all blades, capable of felling enemies with a single slash!*** 🗡️🗡️🗡️ "
        return super().__str__()    
    
    def attack_move(self, move=None):
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
    
    def to_json(self):
        data =super().to_json()
        data.update({
            "defense": self.defense,
            "broken": self.broken,
            "equipped": self._equipped,
            "defense_modifier": self.defense_modifier,
            "broken_modifier": self.broken_modifier
            
        })
        return data
    
    @classmethod
    def from_json(cls, data):
        
        """ Creates a new Shield instance from a JSON string.

        Input:
            data: The JSON string representing a shield by its attributes.

        Returns:
            Shield: A new object from the shield class created from the JSON data.
        """
        
        sheild = cls(name = data['name'], description = data['description'], defense = data['defense'], rarity = data['rarity'], broken = data['broken'])
        sheild._equipped = data['equipped']
        sheild.defense_modifier = data['defense_modifier']
        sheild.broken_modifier = data['broken_modifier']
        return sheild
        
        



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


    def to_json(self):
        data = super().to_json()
        data.update({
            'type': self.type,
            'owner': self.owner,
            'empty': self.empty,
            'value': self.value,
            'effective_time': self.effective_time
        })
        return data
    
    @classmethod
    def from_json(cls, data):
        
        """
        Creates a new Potion instance from a JSON string.

        Input:
             data: The JSON string representing a potion by its attributes.

        Returns:
            Potion: A new object from the potion class created from the JSON data.
        """
        
        potion = cls(data['name'], data['type'], data['owner'], rarity = data['rarity'], value = data['value'], effective_time = data['effective_time']) 
        potion.empty = data.get('empty', False)
        return potion
           

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
            if item in self.items:
                print(item)
            else:
                print(f"{item.name} is not in the backpack.")
        elif item_type:
            filtered_items = [item for item in self.items if item.item_type == item_type]
            for item in filtered_items:
                print(item)
        else:
            for item in self.items:
                print(item)


    def __iter__(self):
        return iter(self.items)
    

    def __contains__(self, item):
        return item in self.items
    
    def to_json(self):
        return {
            'owner': self.owner,
            'items': [item.to_json() for item in self.items]
        }
        
        
    @classmethod
    def from_json(cls,data):
        
        """
        Creates a new Inventory instance from a JSON string.

        Input:
            data: The JSON string representing an item in inventory.

        Returns:
            Inventory: A new object from the inventory class created from the JSON data.
        """
        
        inventory = cls(data['owner'])
        for item_data in data['items']:
            item_type = item_data['item_type'] 
            if item_type == 'weapon':
                inventory.add_item(Weapon.from_json(item_data))
            elif item_type == 'potion':
                inventory.add_item(Potion.from_json(item_data))
            elif item_type == 'shield':
                inventory.add_item(Shield.from_json(item_data))
            else:
                inventory.add_item(Item.from_json(item_data))
        return inventory



#Testing

# inventory = Inventory(owner='Beleg')
# sword = Weapon(name='Master Sword', damage=300, weapon_type='sword', rarity='legendary')
# potion = Potion(name='Health Potion', potion_type='HP', owner='Beleg')
# shield = Shield(name='Big Shield', description='A shield of protection', defense=100, rarity='common', broken=False)

# inventory.add_item(sword)
# inventory.add_item(potion)
# inventory.add_item(shield)

# inventory_json_string = json.dumps(inventory.to_json(), indent=4)
# print("Serialized Inventory JSON:\n", inventory_json_string)

# inventory_data = json.loads(inventory_json_string)

# deserialized_inventory = Inventory.from_json(inventory_data)

# print("Deserialized Inventory Owner:", deserialized_inventory.owner)
# for item in deserialized_inventory.items:
#     print(f"Item Name: {item.name}, Item Type: {item.item_type}")



