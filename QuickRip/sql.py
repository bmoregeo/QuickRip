__author__ = 'christopherfricke'

import sqlite3
from models import dvd

class table():
    def __init__(self, location):
        self.location = location
        self.connection = sqlite3.connect(location)
        self.cursor = self.connection.cursor()
        self.tablename = 'status'
        self.fields = [
            ('modified_date', 'varchar(30)'),
            ('disc_index', 'int'),
            ('filename', 'varchar(50)'),
            ('status', 'varchar(100)')
        ]

    def create(self):
        print 'Creating %s' % self.location
        # Create table
        fields = ', '.join([' '.join(field) for field in self.fields])
        self.cursor.execute('CREATE TABLE %s (%s)' % (self.tablename, fields))

    def add(self, disc):
        try:
            print 'Adding %s' % disc.filename
            self.cursor.execute("INSERT INTO %s VALUES ('%s', %s, '%s', '%s')" % (
                self.tablename,
                disc.modified_date,
                disc.disc_index,
                disc.filename,
                disc.status
            ))
            self.connection.commit()
        except sqlite3.OperationalError, e:
            if 'no such table: status' in e:
                self.create()
                self.add(disc)
            else:
                raise sqlite3.OperationalError(e)

    def update(self, disc):

        self.cursor.execute("UPDATE %s SET status='%s', modified_date='%s' WHERE filename='%s'" % (
            self.tablename,
            disc.status,
            disc.modified_date,
            disc.filename
        ))
        self.connection.commit()

    def select(self, query):

        discs = []
        for row in self.connection.execute(query):
            disc = dvd.dvd()
            disc.modified_date, disc.disc_index, disc.filename, disc.status = row
            discs.append(disc)
        return discs

    def delete(self, disc):
        self.cursor.execute("DELETE FROM %s WHERE filename=%s" % (
            self.tablename,
            disc.filename
        ))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
