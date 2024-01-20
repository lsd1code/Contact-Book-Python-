import json

class FileHandler:
    filename = 'contact.json'
    
    @classmethod
    def load_contacts(cls) -> list[dict[str, str]] | list:
        try:
            with open(cls.filename) as f:
                contacts = json.load(f)
        except FileNotFoundError:
            return []
        else:
            return contacts

        
    @classmethod
    def dump(cls, data: list[dict[str, str]]) -> None:
        with open(cls.filename, 'w') as f: 
            json.dump(data, f)
    

def main() -> None:
    pass


if __name__ == '__main__':
    main()