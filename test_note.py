from notes import Note, NotesBook
from constants import GREEN, RESET


if __name__ == "__main__":
    note_book = NotesBook()

    print(GREEN + "     створюємо нову нотатку" + RESET)
    print(note_book.add_note("first", "If you don’t have big dreams and goals you’ll end up working really hard for someone who does."))
