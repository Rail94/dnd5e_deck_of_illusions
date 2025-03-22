import csv
import random

folder = "files"
deck_list = f"{folder}/deck_list.txt"
used_cards = f"{folder}/used_cards.txt"

def pick_card():
    """
     Pick one random card from deck
    """
    try:
        remaining_cards = get_cards()
        random_card = get_random_card(remaining_cards)

        if random_card is None:
            return "\nNo cards remaining!\n"

        update_cards(remaining_cards, random_card)

        return f"\nPicked {random_card['card']}!\n"

    except Exception as e:
        return "\nSomething went wrong while picking a card!\n"

def get_cards():
    """
    Get remaining cards ids
    """
    try:
        with open(deck_list, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            remaining_cards = []
            for row in reader:
                remaining_cards.append(row)
            return remaining_cards

    except FileNotFoundError:
        return "\nFile deck_list.txt not found!\n"
    except Exception as e:
        print("\nSomething went wrong while getting a card number!\n")

def get_random_card(remaining_cards):
    """
    Pick one random remaining card id and append to used cards file
    """
    if remaining_cards != []:
        try:
            random_card = random.choice(remaining_cards)

            with open(used_cards, "a", encoding="utf-8") as file:
                file.write(f"{random_card['id']},{random_card['card']}\n")
            return random_card

        except FileNotFoundError:
            return "\nFile deck_list.txt not found!\n"
        except Exception as e:
            print("\nSomething went wrong while getting a random card!\n")
    else:
        return

def update_cards(remaining_cards, random_card):
    """
    Excludes picked card from txt file and rewrites it without that card
    """
    try:
        updated_cards = []
        for card in remaining_cards:
            if random_card == card:
                continue
            updated_cards.append(card)

        #Overwrite updated new file
        with open(deck_list, "w", encoding="utf-8") as file:
            # Write headers
            file.write("id,card\n")

            for row in updated_cards:
                file.write(f"{row['id']},{row['card']}\n")

    except FileNotFoundError:
        print("\nFile txt not found!\n")

    except Exception as e:
        print("\nSomething went wrong!\n")