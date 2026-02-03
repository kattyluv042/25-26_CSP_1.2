import NoteUtilities


def main():
    # Display the menu and ask for the user's input.
    print("Welcome to KiedesNote - For All Your Temporary Note Needs.")
    print("Please don't confuse us with other (lesser known) products like Evernote....")
    print("The best temporary notes system on the market - just ask us.")
    print("In order to get started, select from one of the options below:")
    print("1. Add a note.")
    print("2. Display all notes.")
    print("3. Display a random note.")
    print("4. Add and display all notes.")
    print("5. Display a random note.")
    print("6. Delete a note.")
    print("7. Quit program.")

    run = True

    while run:
        # Take the user's choice and process it accordingly
        print("What would you like to do?")

        try:
            choice = int(input())
        except ValueError:
            print("Sorry - I couldn't understand that. Please try again.")
            continue

        if choice == 1:
            NoteUtilities.add_note()
        elif choice == 2:
            NoteUtilities.display_notes()
        elif choice == 3:
            NoteUtilities.display_random_note()
        elif choice == 4:
            NoteUtilities.add_and_display()
        elif choice == 5:
            NoteUtilities.display_random_note()
        elif choice == 6:
            print("Which note would you like to delete?")
            try:
                index = int(input())
                NoteUtilities.delete_note(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == 7:
            run = False
        else:
            print("Sorry - I couldn't understand that. Please try again.")


# Python equivalent of Java's main method
if __name__ == "__main__":
    main()