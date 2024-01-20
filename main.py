from sys import exit
from filehandler import FileHandler
from utils import get_choice_prompt, no_contacts_msg, display_contacts_msg


class ContactBook:
    def __init__(self, title: str) -> None:
        self.title = title
        
        
    def display_contacts(self) -> None:
        """Function that displays contacts in the terminal or a message if the contact book is empty"""
        
        contacts = FileHandler.load_contacts()
        
        if not len(contacts):
            empty_contacts_msg = no_contacts_msg(contacts)
            response = input(empty_contacts_msg).lower()
            
            return self.create_contact() if (response == 'y') else main()
        
        contacts = sorted(contacts, key=lambda contact: contact['name'])

        display_contacts_msg(contacts)
            

    def create_contact(self) -> None:
        """Function that creates a new contact(s)"""
        
        contacts = FileHandler.load_contacts()

        while True:
            name = input('Name: ')
            mobile_no = input('Mobile Number: ')

            if not name or not mobile_no: 
                break

            contacts.append({'name': name, 'mobile_no': mobile_no})
            
            FileHandler.dump(contacts)

            answer = input('Do you want to add another contact?[Y/N]: ').lower()

            if answer != 'y': 
                break

    
    def search_contact(self) -> str | None:
        name = input('Contact name: ')

        contacts = self.find_contact(name, recurse=True)        

        if not contacts:
            print(f'\nSorry, {name.title()} does not exist in the contact book\n')
            return
        
        display_contacts_msg(contacts)
        
    
    def update_contact(self) -> None:
        name = input('Contact name: ')
        contact = self.find_contact(name)

        if not contact:
            print(f'\nSorry, {name.title()} does not exist in the contact book\n')
            return

        new_name = input('Name (leave blank to keep the old name): ')        
        new_mobile_no = input('Mobile Number (leave blank to keep the old number): ')

        if not new_name and not new_mobile_no:
            return
        
        new_contacts = []

        for contact in FileHandler.load_contacts():
            if contact['name'] == name:
                contact = {
                    'name': new_name or contact['name'], 
                    'mobile_no': new_mobile_no or contact['mobile_no']
                }
                new_contacts.append(contact)
            else:
                new_contacts.append(contact)

        FileHandler.dump(new_contacts)
    
    
    def remove_contact(self) -> None:
        pass
    
    
    def find_contact(self, name: str, recurse=False) -> dict | list | None:
        contacts = FileHandler.load_contacts()

        if not len(contacts): 
            return None

        contacts_list = []

        for contact in contacts:
            if contact['name'] == name and recurse:
                contacts_list.append(contact)
                continue

            if contact["name"] == name:
                return contact

        return contacts_list if len(contacts_list) > 0 else None
    
    
    def get_choice(self) -> str | None:
        """Function that gets a choice from the user"""

        while True:
            choice = input(get_choice_prompt())

            if not choice:
                break

            if choice not in ['1', '2', '3', '4', '5']:
                continue

            return choice
    
    
    def run(self) -> None:
        """Function that runs the program"""
       
        while True:
            try:
                choice = self.get_choice()
            except KeyboardInterrupt:
                break
            
            match choice:
                case '1': self.display_contacts()
                case '2': self.search_contact()
                case '3': self.create_contact() 
                case '4': self.update_contact()
                case '5': self.remove_contact()
                case _: exit() 


def main() -> None:
    phone_book = ContactBook('hello test')
    phone_book.run()    
    

if __name__ == '__main__':
    main()