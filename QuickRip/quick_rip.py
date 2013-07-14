from QuickRip.models import dvd

__author__ = 'christopherfricke'
import sql
import datetime

def rip(output_workspace):
    status = sql.table('example.db')
    #discs = status.select("SELECT * FROM status where status = 'Added to Queue'")
    discs = status.select("SELECT * FROM status where status = 'Ripping'")

    for disc in discs:
        disc.status = 'Ripping'
        disc.modified_date = datetime.datetime.now()
        disc.output_workspace = output_workspace
        status.update(disc)



        print 'Ripping %s on Tray %s' % (disc.title, disc.disc_index)
        disc.rip()


if __name__ == '__main__':

    minimum_length = 22

    output_path = '/Users/christopherfricke/Source/quickrip/out'
    #print output_path
    discs = rip(output_path)
