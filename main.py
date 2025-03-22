from functions import show_deck, pick_card, reset_deck, get_cards

def menu():
    menu = True

    while menu == True:
        print("---------------------------------------\nOptions:\n1) Pick Card\n2) Show remaining cards\n3) Show remaining figures\n4) Reset Deck\n0) Exit App\n")

        try:
            select = int(input("Insert option number: "))

            # 1 PICK A CARD
            if select == 1:
                pick_card()

            # 2 SHOW NUMBER OF CARDS
            elif select == 2:
                total_cards = show_deck()
                if total_cards > 1:
                    print(f"\nRemain {total_cards} cards!\n")
                elif total_cards == 1:
                    print(f"\nRemain {total_cards} card!\n")
                else:
                    print("\nNo cards remaining!\n")

            # 3 SHOW REMAINING FIGURES
            elif select == 3:
                remaining_cards = get_cards()
                counter = 0

                if remaining_cards != []:

                    for card in remaining_cards:
                        counter += 1
                        print(f"{counter}. {card['card']}")
                else:
                    print("\nNo cards remaining!\n")

            # 4 RESET DECK
            elif select == 4:
                reset_deck()

            # 5 RESTORE A CARD
            elif select == 5:
                print("Restore card function")

            # CLOSE APP
            elif select == 0:
                print("Exiting...")
                menu = False

            else:
                print("\nNot valid command!\n")

        except ValueError as e:
            print("\nInvalid input, please insert a number.\n")
        except Exception as e:
            print("\nUnexpected error!\n")

# Start App
menu()