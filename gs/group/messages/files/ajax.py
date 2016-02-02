# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2013, 2014, 2016 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals, print_function
from zope.cachedescriptors.property import Lazy
from AccessControl import getSecurityManager
from gs.core import to_ascii
from gs.group.base.page import GroupPage
from gs.group.messages.base import get_icon
from .queries import FileQuery


class FilesAjax(GroupPage):
    @Lazy
    def imgBase(self):
        retval = '{0}/messages/image'.format(self.groupInfo.relativeURL)
        return retval

    @Lazy
    def fileBase(self):
        retval = '{0}/files/f'.format(self.groupInfo.relativeURL)
        return retval

    @Lazy
    def viewTopics(self):
        # TODO: Figure out I could do this better.
        msgs = self.context.messages
        user = getSecurityManager().getUser()
        retval = bool(user.has_permission('View', msgs))
        return retval

    def files(self):
        fs = FileQuery()
        files = fs.recent_files(self.siteInfo.id, self.groupInfo.id, 5)
        retval = [self.marshall_file(f) for f in files]
        assert type(retval) == list
        return retval

    def marshall_file(self, f):
        '''Marshall the file information'''
        retval = f
        retval['isImage'] = retval['mime_type'][:5] == 'image'
        base = self.imgBase if retval['isImage'] else self.fileBase
        imageUrl = '{0}/{1}'.format(base, retval['file_id'])
        retval['url'] = to_ascii(imageUrl)
        postUrl = '{0}/messages/post/{1}'.format(self.groupInfo.relativeURL, retval['post_id'])
        retval['postUrl'] = postUrl
        imgUrl = '{0}/{1}'.format(self.fileBase, retval['file_id']) if retval['isImage'] else ''
        retval['imgUrl'] = imgUrl
        retval['icon'] = get_icon(f['mime_type'])
        return retval
