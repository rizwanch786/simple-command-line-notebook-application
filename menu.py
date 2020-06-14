import sys
from notebook import Notebook,Note

class Menu:
    '''Display the menu and respond to choices'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1" : self.show_notes,
            "2" : self.search_notes,
            "3" : self.add_note,
            "4" : self.modify_note,
            "5" : self.quit
        }

    def display_menu(self):
        print("""
        Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)
    
    def run(self):
        '''Display the menu and response to choices'''
        while True:
            self.display_menu()
            choice = int(input("Enter an Opinion: "))
            if choice <= 0 and choice > 5:
                print(f"{choice} is Invalid choice")
            elif choice == 1:
                self.show_notes()
            elif choice == 2:
                self.search_notes()
            elif choice == 3:
                self.add_note()
            elif choice == 4:
                self.modify_note()
            elif choice == 5:
                self.quit()

    def show_notes(self, notes = None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f"{note.id} : {note.tags} \n {note.memo}")
    
    def search_notes(self):
        filter = input("Search for:")
        notes = self.notebook.search(filter)
        self.show_notes(notes)
    
    def add_note(self):
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added")

    def modify_note(self):
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id,memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("Thank you for using your notebook today")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
