import json
from test_json import entry
import os
def print_with_indent(value, indent=0):
    indentation = "\t" * indent
    print(f"{indentation}{str(value)}")
    #print(indentation + str(value))



class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def __str__(self):
        return self.title

    @classmethod
    def entry_from_json(cls, value: dict):
        # десериализация объекта
        new_entry = cls(value['title'])
        for item in value.get('entries', []):
            new_entry.add_entry(cls.entry_from_json(item))
        return new_entry

    def add_entry(self, entry):
        self.entries.append(entry)
        #print(f"Добавили {entry.title}")
        entry.parent = self

    def json(self):
        res = {
            'title': self.title,
            'entries': [entry.json() for entry in self.entries] #список, который содержит в себе: для каждой записи во вложенных записях название этой записи c рекурсией
        }
        #for entry in self.entries:
            #res['entries'].append(entry.title)
        return res

    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for entry in self.entries:
            entry.print_entries(indent + 1)

    def save_entry(self, path):
        data = self.json()
        with open(os.path.join(path, f'{self.title}.json'), 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)

    @classmethod
    def load_entry(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return cls.entry_from_json(data)


new_entry = Entry.entry_from_json(entry)
new_entry.print_entries()
print(new_entry.json())

new_entry1 = Entry.entry_from_json(new_entry.json())
new_entry1.print_entries()
new_entry.save_entry('D:\programmingPython\/todoBackend')

loaded_entry = Entry.load_entry('D:\programmingPython\/todoBackend\Продукты.json')
print(loaded_entry)


# new_entry = Entry("Продукты")
# meet = Entry("Мясное")
# molochka = Entry("Молочные")
#
# new_entry.add_entry(meet)
# new_entry.add_entry(molochka)
#
# kolbasa = Entry("колбаса")
# meet.add_entry(kolbasa)
#
# moloko = Entry("Молоко")
# molochka.add_entry(moloko)
#
# salami = Entry('Salami')
# kolbasa.add_entry(salami)
#
# chicken = Entry("Chicken")
# salami.add_entry(chicken)
#
# #new_entry.print_entries()
# res = new_entry.json()

#Сериализация объекта
# print(json.dumps(res, ensure_ascii=False, indent=2))