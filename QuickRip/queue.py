__author__ = 'christopherfricke'
import subprocess

from models import dvd
import sql
import settings

def add_to_queue(database):
    status = sql.table(database)

    get_discs_command = ['makemkvcon', '-r', 'info']
    proc = subprocess.Popen(get_discs_command,
                            stderr=subprocess.PIPE,
                            stdout=subprocess.PIPE)

    info = proc.stdout.read()

    for line in info.split('\n'):
        if line[:3] == 'DRV':
            fields = line.split(',')
            if len(fields[5].replace('"', '')) > 0:

                disc = dvd.dvd()
                disc.disc_index = fields[0][4:]
                disc.filename = fields[5]
                disc.status = 'Added to Queue'

                status.add(disc)

    del status


if __name__ == '__main__':
    add_to_queue(settings.database)