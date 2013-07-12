import dvd

__author__ = 'christopherfricke'
import subprocess


def rip_discs(output_workspace):

    get_discs_command = ['makemkvcon', '-r', 'info']
    proc = subprocess.Popen(get_discs_command,
                            stderr=subprocess.PIPE,
                            stdout=subprocess.PIPE)

    info = proc.stdout.read()

    print info

    for line in info.split('\n'):
        if line[:3] == 'DRV':
            fields = line.split(',')

            if len(fields[5].replace('"', '')) > 0:
                d = dvd.dvd()
                d.disc_index = fields[0][4:]
                d.title = fields[5]
                d.output_workspace = output_workspace
                d.rip()


if __name__ == '__main__':

    minimum_length = 22

    output_path = '/Users/christopherfricke/Source/quickrip/out'
    #print output_path
    discs = rip_discs(output_path)
