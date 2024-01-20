"""File that contains messages and prompts to be displayed in the terminal"""

from tabulate import tabulate


def get_choice_prompt():
    return """
============ Contact Management System ============

1. View all contacts
2. Search contact
3. Create contact
4. Update contact
5. Remove contact

============ Press 'enter' to quit ============
> """


def no_contacts_msg(contacts: list[dict]) -> str:
    """Function that displays a message when you have no contacts"""
    
    return f"""
Total Contacts: {len(contacts)}

============ You have no contacts ============

Do you want to add new contacts?[Y/N] 
> """
    

def display_contacts_msg(contacts: list[dict]) -> str:
    """Function for displaying contacts in the terminal"""
    
    headers = contacts[0].keys()
    rows = [contact.values() for contact in contacts]
    
    contacts_str = tabulate(rows, headers=headers, tablefmt='outline')
    
    print(f"""
==============================================

{contacts_str}

Total Contacts: {len(contacts)}

==============================================
""".strip())