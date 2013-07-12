__author__ = 'christopherfricke'

import subprocess
import os
import imdb


class dvd(object):
    """
        Class for ripping a DVD with MakeMKV
    """
    def __init__(self):
        self._disc_index = None
        self._output_path = None
        self._title = None
        self._output_workspace = None


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
    def title(self):
        """
        Returns a cleaned up version of the disc's title

        :return: Disc Title
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Cleans up the disc's file name and attempts to query IMDB for the its correct title.

        :param title: Disc's filename
        :type title: basestring
        :return:
        """
        ia = imdb.IMDb()
        title = title.strip()
        title = title.replace('"', '')
        title = title.replace("_", " ")
        title = title.title()

        request_title = ia.search_movie(title, results=1)

        if len(request_title) > 0:
            self._title = request_title[0]
        elif len(title) == 0:
            self._title = request_title

        print self._title

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
            self.output_path,
            #'--cache=%d' % cache,
            '--noscan',
            '--directio=false',
            '--debug',
            '--minlength=%d' % minimum_length * 60
        ]
        subprocess.call(command)

        disc_eject_command = [
            'drutil',
            '-drive',
            '1',
            'tray',
            'eject'
        ]
        subprocess.call(disc_eject_command)