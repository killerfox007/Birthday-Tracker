from models.__init__ import CONN, CURSOR
class Birthday:
    
    def __init__(self,date, person_id, id=None):
        self.date = date
        self.person_id = person_id
        self.id = id
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self,date):
        if isinstance(date, str) and len(date) == 10:
            self._date = date
        else:
            print("Date Must be in this format, 00/00/0000")
    @property
    def person_id(self):
        return self._person_id
    @person_id.setter
    def person_id(self, person_id):
        from models.people import People
        change_to_int = int(person_id)
        if isinstance(change_to_int, int) and change_to_int > 0:
            person=People.find_by_id(change_to_int)
            if person:
                self._person_id = change_to_int
            else:
                raise ValueError("Person not found")
        else:
            raise ValueError("Person not in database yet")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS birthdays (
            id INTEGER PRIMARY KEY,
            date TEXT,
            person_id INTEGER, 
            FOREIGN KEY (person_id) REFERENCES peoples(id)
            );
            """
        CURSOR.execute(sql)
        CONN.commit()

    def insert_into_db(self):
        sql = """
        INSERT INTO birthdays (date, person_id) VALUES (?,?);
        """
        CURSOR.execute(sql, (self.date, self.person_id,))
        CONN.commit()
        self.id = CURSOR.lastrowid
    @classmethod
    def create(cls, date, person_id):
        birthday = Birthday(date=date, person_id=person_id)
        birthday.insert_into_db()
        return birthday
    @classmethod
    def list_all_birthdays(cls):
        sql = """
            SELECT *
            FROM birthdays
        """
        all_birthdays = CURSOR.execute(sql).fetchall()
        return [cls.from_db(row) for row in all_birthdays]
    @classmethod
    def from_db(cls,row):
        return Birthday(id=row[0], date=row[1], person_id=row[2])

    def delete(self):
        sql = """
        DELETE FROM birthdays
        WHERE person_id = ?
        """
        CURSOR.execute(sql, (self.person_id,))
        CONN.commit()
    
    @classmethod
    def find_by_id(cls, person_id):
        sql="""
        SELECT *
        FROM birthdays
        WHERE person_id = ?
        """
        
        row = CURSOR.execute(sql, (person_id,)).fetchone()
        return cls.from_db(row) if row else None
    
    @classmethod
    def drop_table(cls):
        sql = """
        DROP TABLE IF EXISTS birthdays
        """
        CURSOR.execute(sql)
        CONN.commit()

    

    # def __repr__(self):
    #     return f'<Birthday id={self.id} birthday={self.date} person={self.person_id}'