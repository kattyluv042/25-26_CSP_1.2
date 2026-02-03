import random

"""
The NoteUtilities module keeps track of the list holding the notes and the index
of the last note added.

Since Java static arrays cannot change size, the original program used a large
array (10,000 items). We keep the same idea here for instructional consistency.
"""

# Setup note_list, last_note, and random number generator
note_list = [""] * 10000
last_note = 0

# Add a note to note_list
def add_note():
    global last_note
    print("Please type in the note you would like to add below:")
    new_note = input()
    note_list[last_note] = new_note
    last_note += 1


# Display all the notes in note_list
# We add 1 to current_note for purposes of display only
def display_notes():
    for current_note in range(last_note):
        print(f"{current_note + 1}. {note_list[current_note]}")
    print()


# Select a random note from note_list to display
def display_random_note():
    if last_note == 0:
        print("No notes to display.")
        return

    random_note = random.randint(0, last_note - 1)
    print(f"Your random note was number {random_note + 1}!")
    print(note_list[random_note])


# Add and display all notes in one option
def add_and_display():
    add_note()
    display_notes()


def delete_note(num_note):
    global last_note

    # Adjust for human-friendly numbering
    num_note -= 1

    # Validate selection
    if num_note < 0 or num_note >= last_note:
        print("I'm sorry, but you have made an invalid selection.")
        print("Please try again.")
    else:
        # Shift notes left to overwrite deleted note
        for current_note in range(num_note, last_note - 1):
            note_list[current_note] = note_list[current_note + 1]

        note_list[last_note - 1] = ""
        last_note -= 1
        print("Note deleted.")