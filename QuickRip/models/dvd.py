__author__ = 'christopherfricke'

import subprocess
import os
import imdb
import datetime

class dvd(object):
    """
        Class for ripping a DVD with MakeMKV
    """
    def __init__(self):
        self._disc_index = None
        self._output_path = None
        self._filename = None
        self._title = None
        self._output_workspace = None
        self._modified_date = datetime.datetime.now()


    @property
    def disc_index(self):
        """
        Returns the tray index of the disc

        :return: Disc Index
        """
        return self._disc_index

    @disc_index.setter
    def disc_index(self, disc_index):
        """
        Sets the tray index of the disc

        :param disc_index: Tray index of the disc
        :type disc_index: int
        :return:
        """
        self._disc_index = disc_index

    @property
    def output_path(self):
        """
        Returns the output path for the ripped mkv file

        :return: Output path to save mkv file into
        """
        return os.path.join(self.output_workspace, self.title)

    @property
    def output_workspace(self):
        """
        Returns the output workspace for all rips

        :return: Output workspace
        """
        return self._output_workspace

    @output_workspace.setter
    def output_workspace(self, output_workspace):
        """
        Sets the workspace folder for all rip jobs

        :param output_workspace: Output workspace for all rip jobs
        :type output_workspace: basestring
        :return:
        """
        self._output_workspace = output_workspace

    @property
    def filename(self):
        """
        Returns the original filename of the disc image

        :return: Filename of disc
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """
        Sets the filename of the original disc and populates the title with a cleaned up version.

        :param filename: Filename of disc
        :type filename: basestring
        :return:
        """
        self._filename = filename
        self._set_title()

    @property
    def title(self):
        """
        Returns a cleaned up version of the disc's title

        :return: Disc Title
        """
        return self._title

    def _set_title(self):
        """
        Cleans up the disc's file name and attempts to query IMDB for the its correct title.

        :param title: Disc's filename
        :type title: basestring
        :return:
        """
        ia = imdb.IMDb()
        title = self.filename.strip()
        title = title.replace('"', '')
        title = title.replace("_", " ")
        title = title.title()

        request_title = ia.search_movie(title, results=1)

        if len(request_title) > 0:
            self._title = request_title[0]
        elif len(request_title) == 0:
            self._title = title

    def rip(self, minimum_length=22):
        """
        Passes a request to makemkv to create a MKV file out of the disc image

        :param minimum_length: Minimum length of video file to rip in minutes
        :type minimum_length: int
        :return:
        """
        try:
            os.mkdir(self.output_path)
        except OSError:
            pass

        command = [
            'makemkvcon',
            'mkv',
            'disc:%s' % self.disc_index,
            '0',
            '"%s"' % self.output_path,
            '-r',
            #'--cache=%d' % cache,
            '--noscan',
            '--debug',
            '--minlength=%s' % (minimum_length * 60)
        ]
        print ' '.join(command)

        subprocess.call(command)

        disc_eject_command = [
            'drutil',
            '-drive',
            '1',
            'tray',
            'eject'
        ]
        #subprocess.call(disc_eject_command)

    @property
    def status(self):
        """
        Returns status of disc ripping process
        :return: Disc Rip Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        :param status: Status of Disc Rip One of following values ("Added to Queue", "Ripping", or "Ripped")
        :type status: basestring
        :return:
        """
        self._status = status

    @property
    def modified_date(self):
        """
        Return the last modified date on a disc
        :return: Datestamp
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """
        Set the last modified date on a disc
        :param modified_date: Datestamp of last modified date
        :type modified_date: datetime
        :return:
        """
        self._modified_date = modified_date