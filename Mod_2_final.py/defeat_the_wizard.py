import random
# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5) #attack power can be 5 lower or higher
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        heal_amount = 50
        if self.health + heal_amount > self.max_health:
            self.health = self.max_health
            print (f"{self.name} has full health! Current health: {self.health}") #they can't heal more than what their health is
            
        else:
            self.health += heal_amount
            print (f"{self.name} pulls out a glowing blue vial and drinks it!  This turn was used to heal! Health: {self.health}") 


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power
        
    def attack(self, opponent): 
        super().attack(opponent)
        print (f"{self.name} yells as they lift their blade and slashes {opponent.name} with their sword")

    def special_ability(self,opponent): #shield
        print (f"{self.name} lifts their guilded sheild, to protect themselves from {opponent.name}'s attack!")

class Baird(Character): #added a fun character that isn't strong but has good health
    def __init__(self, name):
        super().__init__(name, health=150, attack_power= 22) 
    
    def attack(self, opponent): #the uke of death
        super().attack(opponent)
        print (f"{self.name} holds up his ukelele, twirling it with impossible speeds as he swings and hits {opponent.name}!")

    def special_ability (self, opponent): #hide
        print (f"{self.name} hides behind a rocky column so {opponent.name} can't find them!")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power
    
    def attack(self, opponent):
        super().attack(opponent)
        print (f"{self.name} cast a powerful sphere of shocking blue kinetic energy at {opponent.name}!")

    def special_ability (self, opponent): #cast spell
        print (f"{self.name} cast a powerful shield bubble around themselves, effectively bouncing {opponent.name} off of them!")

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=25)

    def attack(self, opponent): #quick shot
        super().attack(opponent)
        print (f"{self.name} uses Quick Shot! Rapidly docking two arrows at lightning speed shooting at {opponent.name}!")
    
    def special_ability (self, opponent):
        print(f"{self.name} jumps out of the way and evades {opponent.name} attack!") #Evade attack

class Paladin(Character):
    def __init__(self,name):
        super().__init__(name, health=90, attack_power=40)
    
    def attack(self, opponent): #holy strike
        super().attack(opponent)
        print (f"{self.name} grits their teeth as they raise their sword, glenting it slams into {opponent.name} with Holy Strike!")

    def special_ability (self, opponent): #holy shield
        print (f"{self.name} claps their hands together and starts a prayer, using Holy Shield to block {opponent.name}'s attack!")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):

    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        if self.health > self.max_health:
            self.health = self.max_health
        
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

    def attack (self,opponent):
        super().attack(opponent)
        print(f"{self.name} laughs evilly as he reads from a tome, a wave of dark miasma hits {opponent.name}")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin
    print("5. Baird")
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    elif class_choice == '5':
        return Baird(name)
    
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")
        special_ability_used = False

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            # Call the special ability here
            player.special_ability(wizard)
            special_ability_used = True
        elif choice == '3':
            player.heal()

        elif choice == '4': # fixed, wizards attack is skipped if player wants to see their stats. neither party is harmed.
            player.display_stats()
            continue
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()

            if not special_ability_used:
                wizard.attack(player)
            else:
                print(f"{wizard.name} attack was blocked by {player.name}!") #used so the wizard doesn't hit every time

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            print("OH NO! Don't let the Wizard destroy the world! We were counting on you!")
            break

        if wizard.health <= 0:
            print(f"Congratulations! {wizard.name} has been defeated by {player.name}!")
        
# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()
