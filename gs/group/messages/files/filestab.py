# coding=utf-8
from gs.group.home.simpletab import PublicTab


class FilesTab(PublicTab):
    def __init__(self, group, request, view, manager):
        super(FilesTab, self).__init__(group, request, view, manager)
