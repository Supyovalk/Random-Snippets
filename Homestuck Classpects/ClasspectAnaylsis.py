import sqlite3
DATABASE_PATH='ClasspectRatings.db'
class SQLConn():
    def __init__(self, file=DATABASE_PATH):
        self.file=file
    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()
    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()
Roles=[
    ("Seer","Canon Class",None),
    ("Time","Canon Aspect",None),
    ("Space","Canon Aspect",None),
    ("Heart","Canon Aspect",None),
    ("Seer of Time","Canon Aspect",["Seer","Time"]),
    ("Seer of Heart","Canon Aspect",["Seer","Heart"]),
    ("Time-Space","Canon Crosspect",["Time","Seer"]),
    ("Seer of Time-Space","Canon CrossClasspect",["Seer","Time","Space"])
]
Fandoms=[
    ("Life Is Strange",1,1)
]
Characters=[
    ("Alex Chen","Life Is Strange","Seer of Heart","Cancer","?")
]
CharacterRoleRating = [
    ("Alex Chen","Seer of Heart","X","Has Heart-Seeing Abilites,Struggles With Knowing Which Emotions are hers")
]
def createTables():
    with SQLConn() as crsr:
        crsr.execute("""CREATE TABLE IF NOT EXISTS FANDOMS(
                     id integer,
                     totalcharacters not null,
                     classpectedcharacters intger not null,
                     name text,
                     PRIMARY KEY (id AUTOINCREMENT)
                     )
                     """)
def addFandom(fandomname):
    with SQLConn() as crsr:
        crsr.execute('INSERT INTO fandoms(totalcharacters,classpectedcharacters,name) values(0,0,\''+fandomname+"\')")
def incrementFandomClasspectCount(fandomname):
    with SQLConn() as crsr:
        crsr.execute('UPDATE fandoms SET classpectedcharacters = classpectedcharacters + 1 WHERE name = \''+fandomname+"\'")
def incrementFandomCharacterCount(fandomname):
    with SQLConn() as crsr:
        crsr.execute('UPDATE fandoms SET totalcharacters = totalcharacters + 1 WHERE name = \''+fandomname+"\'")
createTables()
#addFandom("Life Is Strange")
incrementFandomClasspectCount("Life Is Strange")