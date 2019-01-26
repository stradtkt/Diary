from peewee import *
import datetime
db = SqliteDatabase("diary.db")

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

def initialize():
    """Create the db and table if they do not exist"""
    db.connect()
    db.create_tables([Entry], safe=True)

def menu_loop():
    """Show the menu"""


def add_entry():
    """Add an entry"""


def view_entries():
    """View previous entries"""


def delete_entry():
    """Delete an entry"""


if __name__ == "__main__":
    initialize()
    menu_loop()