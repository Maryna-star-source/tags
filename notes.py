from collections import UserDict
from constants import RED, GRAY, CYAN, MAGENTA, RESET, LEN_OF_NAME_FIELD
from datetime import datetime
import os.path
import pickle



class Note():
    def __init__(self, title, content, tags=None, keywords=None):
        self.title = title
        self.content = content
        self.tags = tags or []
        
        
    def add_note(self, title, content):
        self.notes[title] = content 

    def edit_note(self, title, new_content):
        if title in self.notes:
            self.notes[title] = new_content
            return f"Note '{title}' edited."
        else:
            return f"Note '{title}' not found." 

    def delete_note(self, title):
        if title in self.notes:
            del self.notes[title]
            return f"Note '{title}' deleted."
        else:
            return f"Note '{title}' not found."
                
    
class NotesBook(UserDict):
    def __init__(self):
        self.notes = {} 
        
    

    def search_notes_by_tag(self, tag, sort_by_keywords=False):
matching_notes = [
    f"Title: {title}\nContent: {note['content']}\nTags: {', '.join(note['tags'])}"
    for title, note in self.notes.items() if tag.lower() in map(str.lower, note['tags'])
]


    def add_tags(self, title, tags): # метод для додавання тегів
        if title in self.notes:
            self.notes[title].tags.extend(tags)
            return f"Tags {', '.join(tags)} added to the note with title '{title}'."
        else:
            raise NoteError(f"Note with title '{title}' not found.")


    def search_notes_by_tag(self, tag, sort_by_keywords=False):
        matching_notes = [note for note in self.notes.values() if tag.lower() in map(str.lower, note.tags)]

        if sort_by_keywords:
            matching_notes.sort(key=lambda note: note.keywords)

        if matching_notes:
            return "\n".join(map(str, matching_notes))
        else:
            return "No notes found with the specified tag."

