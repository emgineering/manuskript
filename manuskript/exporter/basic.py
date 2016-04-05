#!/usr/bin/env python
# --!-- coding: utf8 --!--

import shutil
import subprocess

from PyQt5.QtWidgets import QWidget

from manuskript.models.outlineModel import outlineItem


class basicExporter:

    name = ""
    description = ""
    exportTo = []
    cmd = ""

    def __init__(self):
        pass

    @classmethod
    def getFormatByName(cls, name):
        for f in cls.exportTo:
            if f.name == name:
                return f

        return None

    @classmethod
    def isValid(cls):
        return cls.path() != None

    @classmethod
    def version(cls):
        return ""

    @classmethod
    def path(cls):
        return shutil.which(cls.cmd)

    @classmethod
    def run(cls, args):
        r = subprocess.check_output([cls.cmd] + args)  # timeout=.2
        return r.decode("utf-8")

        # Example of how to run a command
        #
        # cmdl = ['txt2tags', '-t', target, '--enc=utf-8', '--no-headers', '-o', '-', '-']
        #
        # cmd = subprocess.Popen(('echo', text), stdout=subprocess.PIPE)
        # try:
        #     output = subprocess.check_output(cmdl, stdin=cmd.stdout, stderr=subprocess.STDOUT)  # , cwd="/tmp"
        # except subprocess.CalledProcessError as e:
        #     print("Error!")
        #     return text
        # cmd.wait()
        #
        # return output.decode("utf-8")


class basicFormat:

    implemented = False
    requires = {
        "Settings": False,
        "Preview": False,
    }

    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    @classmethod
    def settingsWidget(cls):
        return QWidget()

    @classmethod
    def previewWidget(cls):
        return QWidget()

    @classmethod
    def preview(cls, settingsWidget, previewWidget):
        pass