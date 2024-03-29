from typing import List
from resources import Entry
import os
import json

class EntryManager:
    def __init__(self, data_path:str):
        self.data_path = data_path
        self.entries = []

    def save(self):
        for entry in self.entries:
            entry.save_entry(self.data_path)

    def load(self):
        if not os.path.isdir(self.data_path):
            os.makedirs(self.data_path)
        else:
            for filename in os.listdir(self.data_path):
                if filename.endswith('.json'):
                    entry = Entry.load_entry(os.path.join(self.data_path, filename))
                    self.entries.append(entry)
        return self

    def add_entry(self, title: str):
        self.entries.append(Entry(title))
