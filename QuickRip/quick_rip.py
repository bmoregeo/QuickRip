from QuickRip.models import dvd

__author__ = 'christopherfricke'
import sql
import datetime
import settings


def rip(database, output_workspace, minimum_length):
    status = sql.table(database)
    discs = status.select("SELECT * FROM status where status = 'Added to Queue'")

    for disc in discs:
        disc.status = 'Ripping'
        disc.modified_date = datetime.datetime.now()
        disc.output_workspace = output_workspace
        disc.minimum_length = minimum_length
        status.update(disc)

        print 'Ripping %s on Tray %s' % (disc.title, disc.disc_index)
        disc.rip()
        disc.status = 'Ripped'
        status.update(disc)


if __name__ == '__main__':
    discs = rip(settings.database, settings.output_path, settings.minimum_length)
