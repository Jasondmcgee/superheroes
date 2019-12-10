import random


class Ability:
    def __init__(self, name, attack_strength):
        '''
       Initialize the values passed into this
       method as instance variables.
        '''

        # Assign the "name" and "max_damage"
        # for a specific instance of the Ability class
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''

        # Pick a random value between 0 and self.max_damage
        random_value = random.randint(0, self.max_damage)
        return random_value


class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use integer division to find half of the max_damage value
        # then return a random integer between half of max_damage and max_damage
        return random.randint(self.max_damage/2, self.max_damage)



class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        # TODO: Create instance variables for the values passed in.
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' Return a value between 0 and the value set by self.max_block.'''

        random_value = random.randint(0,self.max_block)
        return random_value


class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
        '''

        self.deaths = 0
        self.kills = 0
        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
        
    def add_kill(self):
        ''' Update self.kills by num_kills amount'''
        self.kills += 1

    def add_death(self):
        ''' Update deaths with num_deaths'''
        # TODO: This method should add the number of deaths to self.deaths
        self.deaths += 1

    def add_ability(self, ability):
        ''' Add ability to abilities list '''

        # We used the append method to add strings to a list
        # in the Rainbow Checklist tutorial. This time,
        # we're not adding strings, instead we'll add ability objects.
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        self.add_ability(weapon)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total_damage:Int
        '''
         # start our total out at 0
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
        Armor: Armor Object
        '''
        self.armors.append(armor)
        # TODO: Add armor object that is passed in to `self.armors`

    def defend(self, damage_amt):
        '''Calculate the total block amount from all armor blocks.
        return: total_block:Int
        '''
        total_blocks = 0
        for armor in self.armors:
            total_blocks += armor.block()
        return total_blocks
        # TODO: This method should run the block method on each armor in self.armors

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        # TODO: Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        defense = self.defend(damage)
        if (defense > damage):
            pass
        else:
            self.current_health =  self.current_health - damage + defense

    def is_alive(self):  
        '''Return True or False depending on whether the hero is alive or not.
        '''
        if (self.current_health <= 0):
            return False
        else:
            return True
        # TODO: Check the current_health of the hero.
        # if it is <= 0, then return False. Otherwise, they still have health
        # and are therefore alive, so return True
    
    def fight(self, opponent):  
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        if(len(self.abilities) > 0 or len(opponent.abilities) > 0):
            while (self.current_health > 0 or opponent.current_health > 0):
                my_attack = self.attack()
                opponent.take_damage(my_attack)
                their_attack = opponent.attack()
                self.take_damage(their_attack)
                print(self.current_health, opponent.current_health)
                if(self.is_alive() != True):
                    self.add_death()
                    opponent.add_kill()
                    print('THIS HERO WON: '+ opponent.name)
                if(opponent.is_alive() != True):
                    self.add_kill()
                    opponent.add_death()
                    print('THIS HERO WON: ' + self.name)
        else:
            print('draw')
            pass

        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
        # 1) else, start the fighting loop until a hero has won
        # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
        # 3) After each attack, check if either the hero (self) or the opponent is alive
        # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
    
class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        foundHero = False
        # loop through each hero in our list
        for hero in self.heroes:
            # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # set our indicator to True
                foundHero = True
        # if we looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not foundHero:
            return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # TODO: Loop over the list of heroes and print their names to the terminal one by one.
        for hero in self.heroes:
            print(hero)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        # TODO: Add the Hero object that is passed in to the list of heroes in
        # self.heroes
        self.heroes.append(hero)

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))

    def revive_heroes(self):
        ''' Reset all heroes health to starting_health'''
        # TODO: for each hero in self.heroes,
        # set the hero's current_health to their starting_health
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)
        counter = 0
        while (len(living_heroes) > 0 and len(living_opponents)> 0):
            index = random.randint(0, len(living_heroes))
            opp_index = index = random.randint(0, len(living_opponents)) - 1
            my_hero = living_heroes[index]
            opp_hero = living_opponents[opp_index]
            my_hero.fight(opp_hero)
            if (my_hero.is_alive() != True):
                living_heroes.remove(my_hero)
            if (opp_hero.is_alive() != True):
                living_opponents.remove(opp_hero)
            counter += 1
            if counter > 999:
                print('shield stepped in')
                break
            # TODO: Complete the following steps:
            # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
            # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
            # 3) update the list of living_heroes and living_opponents
            # to reflect the result of the fight

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = []
        self.team_two = []
        # TODO: create instance variables named team_one and team_two that
        # will hold our teams.

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        name = input("What is the ability name?  ")
        max_damage = input(
            "What is the max damage of the ability?  ")

        return Ability(name, max_damage)
    
    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        name = input("What is the wepons name?")
        max_damage = input(
            "What is the max damage of the ability?  ")
        # TODO: This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.
        weapon = Weapon(name, max_damage)
        return weapon

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''

        name = input("What is the armors name?")
        max_block = input(
            "What is the max block of the armor?  ")
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor object.
        #  return the new armor object with values set by user.
        armor = Armor(name, max_block)
        return armor

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               self.create_ability()
               #TODO add an ability to the hero
           elif add_item == "2":
               self.create_weapon()
               #TODO add a weapon to the hero
           elif add_item == "3":
               self.create_armor()
               #TODO add an armor to the hero
        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # TODO: This method should allow a user to create team one.
        name = input('name your team:')
        num_heros = int(input('how many heroes on your team?'))
        self.team_one = Team(name)
        for i in range(0, num_heros):
            self.team_one.add_hero(self.create_hero())
        # 1) Prompt the user for the name of the team
        # 2) Prompt the user for the number of Heroes on the team
        # 3) Instantiate a new Team object,
        # using the team name obtained from user input
        # 4) use a loop to call self.create_hero() for the number
        # of heroes the user specified the team should have,
        # and then add the heroes to the team.

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        name = input('name the other team:')
        num_heros = int(input('how many heroes on the other team?'))
        self.team_two = Team(name)
        for i in range(1, num_heros):
            self.team_two.add_hero(self.create_hero())
        # TODO: This method should allow a user to create team two.
        # 1) Prompt the user for the name of the team
        # 2) Prompt the user for the number of Heroes on the team
        # 3) Instantiate a new Team object,
        # using the team name obtained from user input
        # 4) use a loop to call self.create_hero() for the number
        # of heroes the user specified the team should have,
        # and then add the heroes to the team.

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Show surviving heroes.
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        # Some help on how to achieve these tasks:
        team_one_counter = 0
        team_two_counter = 0
        total_killed_one = 0
        total_died_one = 0
        total_killed_two = 0
        total_died_two = 0
        for hero in self.team_one:
            print('Team_one living:')
            total_killed_one += hero.kills
            total_died_one += hero.deaths
            if hero.is_alive():
                print(hero.name)
                team_one_counter += 1
        print('number survived:', team_one_counter)
        print('average kills per memeber:', total_killed_one/len(self.team_one))
        print('average deaths per memeber:', total_died_one/len(self.team_one))
        for hero in self.team_two:
            print('Team_two living:')
            total_killed_two += hero.kills
            total_died_two += hero.deaths
            if hero.is_alive():
                team_two_counter += 1
                print(hero.name)
        print('number survived:', team_two_counter)
        print('average kills per memeber:', total_killed_two/len(self.team_two))
        print('average deaths per memeber:', total_died_two/len(self.team_two))
        if(team_one_counter > team_two_counter):
            print('team one wins!')
        elif(team_one_counter < team_two_counter):
            print('team two wins!')
        else:
            print('draw')
        

        
        # TODO: for each team, loop through all of their heroes,
        # and use the is_alive() method to check for alive heroes,
        # printing their names and increasing the count if they're alive.
        #
        # TODO: based off of your count of alive heroes,
        # you can see which team has more alive heroes, and therefore,
        # declare which team is the winning team
        #
        # TODO for each team, calculate the total kills and deaths for each hero,
        # find the average kills and deaths by dividing the totals by the number of heroes.
        # finally, divide the average number of kills by the average number of deaths for each team
        pass



        
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()