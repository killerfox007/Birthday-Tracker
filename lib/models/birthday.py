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
            raise ValueError("Date Must be in this format, 00/00/0000")
1
    @property
    def person_id(self):
        return self._person_id
    @person_id.setter
    def person_id(self, person_id):
        from models.people import People
        if isinstance(person_id,int) and person_id > 0:
            person=People.find_by_id(person_id)
            if person:
                self._person_id = person_id
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
            person_id INTEGER
            );
            """
        CURSOR.execute(sql)
        CONN.commit()