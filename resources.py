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

    def add_entry(self, entry):
        self.entries.append(entry)
        #print(f"Добавили {entry.title}")
        entry.parent = self

    def json(self):
        res ={
            'title': self.title,
            'entries': [entry.title for entry in self.entries] #список, который содержит в себе: для каждой записи во вложенных записях название этой записи
        }
        #for entry in self.entries:
            #res['entries'].append(entry.title)
        return res



    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for entry in self.entries:
            entry.print_entries(indent + 1)

new_entry = Entry("Продукты")
meet = Entry("Мясное")
molochka = Entry("Молочные")

new_entry.add_entry(meet)
new_entry.add_entry(molochka)

kolbasa = Entry("колбаса")
meet.add_entry(kolbasa)

moloko = Entry("Молоко")
molochka.add_entry(moloko)

salami = Entry('Salami')
kolbasa.add_entry(salami)

chicken = Entry("Chicken")
salami.add_entry(chicken)

#new_entry.print_entries()
print(new_entry.json())