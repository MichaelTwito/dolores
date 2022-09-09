

class RepositoryBase(object):
    def __init__(self, db):
        self.db = db
        print(db)

    def session(self):
        return self.db.session

    def create(self, item):
        self.session().add(item)
        self.session().commit()
        self.session().refresh(item)
        return item


            