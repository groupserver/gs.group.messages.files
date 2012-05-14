# coding=utf-8
from zope.cachedescriptors.property import Lazy
from gs.group.home.simpletab import UserInfoTab

class FilesTab(UserInfoTab):
    def __init__(self, group, request, view, manager):
        UserInfoTab.__init__(self, group, request, view, manager)

