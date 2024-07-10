from models.__init__ import CONN, CURSOR
class People:
    def __init__(self, name,id=None):
        self.name = name
        self.id = id

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name, str) and len(name) >= 2 and name != "":
            self._name = name
        else:
            raise ValueError("Please put a name Longer then 2 characters")
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS peoples (
            id INTEGER PRIMARY KEY,
            name TEXT
            );
            """
        CURSOR.execute(sql)
        CONN.commit()
    
    def insert_into_db(self):
        sql = """
        INSERT INTO peoples (name) VALUES (?);
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid
    @classmethod
    def create(cls, name):
        person = People(name=name)
        person.insert_into_db()
        return person

    def delete(self):
        sql = """
            DELETE FROM peoples 
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def all_people(cls):
        sql = """
            SELECT *
            FROM peoples
        """
        all_peoples = CURSOR.execute(sql).fetchall()
        return [cls.from_db(row) for row in all_peoples]

    @classmethod
    def from_db(cls,row):
        return People(id=row[0], name=row[1])
    @classmethod
    def find_by_name(cls,name):
        sql="""
        SELECT *
        FROM peoples
        WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.from_db(row) if row else None
    
    @classmethod
    def find_by_id(cls,id):
        sql="""
        SELECT *
        FROM peoples
        WHERE id = ?
        """
        
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.from_db(row) if row else None
    
    def __repr__(self):
        return f'<Person name={self.name} id={self.id}'