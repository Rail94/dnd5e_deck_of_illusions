import csv
import random

folder = "files"
txt = f"{folder}/deck_list.txt"
backup = f"{folder}/backup_list.txt"

def show_deck():
    """
     Show number of cards
    """
    try:
        deck = get_cards()
        total_cards = len(deck)
        return total_cards

    except Exception as e:
        print("\nSomething went wrong while showing deck!\n")

def show_figures():
    """
    Show remaining figures
    """
    try:
        with open(txt, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            remaining_cards = []
            for row in reader:
                remaining_cards.append(row)
            return remaining_cards

    except FileNotFoundError:
        print("\nFile txt not found!\n")

    except Exception as e:
        print("\nSomething went wrong while getting a card number!\n")

def reset_deck():
    """
    Reset cards
    """
    try:
        #Get data from backup file
        with open(backup, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            backup_cards = []
            for row in reader:
                backup_cards.append(row)

            # Overwrite txt file with backup
        with open(txt, "w", encoding="utf-8") as file:
            # Write headers
            file.write("id,card\n")

            for row in backup_cards:
                file.write(f"{row['id']},{row['card']}\n")

        print("\nGenerated new deck!\n")

    except FileNotFoundError:
        print("\nFile txt not found!\n")

    except Exception as e:
        print("\nSomething went wrong!\n")

def pick_card():
    """
     Pick one random card from deck
    """
    try:
        remaining_cards = get_cards()

        random_card = get_random_card(remaining_cards)

        if random_card:
            print(f"\nPicked {random_card['card']}!\n")

        update_cards(remaining_cards, random_card)
    except Exception as e:
        print("\nSomething went wrong while picking a card!\n")
def get_cards():
    """
    Get remaining cards ids
    """
    try:
        with open(txt, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            remaining_cards = []
            for row in reader:
                remaining_cards.append(row)
            return remaining_cards

    except FileNotFoundError:
        print("\nFile txt not found!\n")

    except Exception as e:
        print("\nSomething went wrong while getting a card number!\n")

def get_random_card(remaining_cards):
    """
    Pick one random remaining card id
    """
    if remaining_cards != []:
        try:
            random_card = random.choice(remaining_cards)
            return random_card

        except Exception as e:
            print("\nSomething went wrong while getting a random card!\n")
    else:
        print("\nNo cards remaining!\n")

def update_cards(remaining_cards, random_card):
    """
    Delete picked card from txt file and rewrites it
    """
    try:
        updated_cards = []
        for card in remaining_cards:
            if random_card == card:
                continue
            updated_cards.append(card)

        #Overwrite updated new file
        with open(txt, "w", encoding="utf-8") as file:
            # Write headers
            file.write("id,card\n")

            for row in updated_cards:
                file.write(f"{row['id']},{row['card']}\n")

    except FileNotFoundError:
        print("\nFile txt not found!\n")

    except Exception as e:
        print("\nSomething went wrong!\n")