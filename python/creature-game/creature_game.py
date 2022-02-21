"""
Challenge. Show me a mythical creature!
- Create a menu with a list of creatures
- Prompt the menu and allow the user select an option:
    * Creature type
    * Creature name
- Show to the user a creature picture and its name based on the user's selection.
- Show to the user the creature sound based on menu selection.

Play it on https://replit.com/@martinezga/creature-game
"""
import os
import creatures


menu = {
    '1': 'Dragon 🐉',
    '2': 'Mermaid 🧜',
    '3': 'Unicorn 🦄',
    '0': 'Exit 🔚',
}

sounds = {
    'dragon': 'grrrr',
    'mermaid': 'la la laaa',
    'unicorn': 'hiiii',
}

class Creature():
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.show_creature()
        self.show_name_and_sound()

    def show_creature(self):
        creature = getattr(creatures, self.type)
        print(creature)
        return creature

    def show_name_and_sound(self):
        text = f'{sounds.get(self.type).title()} 🎵... My name is {self.name}'
        print(text)
        return text


if __name__ == '__main__':
    os.system('clear')
    print(f'{os.linesep}Welcome to the Creature Game! 🌈')
    while True:
        print(f'{os.linesep}Please select a creature:')
        for option in menu:
            print(f'{option}. {menu.get(option)}')

        animal_input = input(f'{os.linesep}Enter an option: ')

        if animal_input == '0':
            print(f'{os.linesep}Goodbye! 😁 Thank you for playing!')
            break
        elif animal_input not in menu:
            print(f'{os.linesep}Invalid option, please try again.')
        else:
            animal_name = input(f'{os.linesep}Please enter a creature name: ')
            animal_type_raw = menu.get(animal_input)
            animal_type = animal_type_raw.split(' ')[0]
            creature = Creature(animal_type.lower(), animal_name)


# Realizado con 💖 por Gabriella Martínez 😊