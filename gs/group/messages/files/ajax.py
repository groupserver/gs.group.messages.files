# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2013, 2014 OnlineGroups.net and Contributors.
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
from __future__ import absolute_import, unicode_literals
from zope.cachedescriptors.property import Lazy
from AccessControl import getSecurityManager
from gs.core import to_ascii
from gs.group.base.page import GroupPage
from gs.group.messages.base import get_icon
from .queries import FileQuery


class FilesAjax(GroupPage):
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
        imgBase = '{0}/messages/image'.format(self.groupInfo.relativeURL)
        fileBase = '{0}/files/f'.format(self.groupInfo.relativeURL)
        for f in files:
            f['isImage'] = f['mime_type'][:5] == 'image'
            base = imgBase if f['isImage'] else fileBase
            imageUrl = '{0}/{1}'.format(base, f['file_id'])
            f['url'] = to_ascii(imageUrl)
            postUrl = '{0}/messages/post/{1}'.format(self.groupInfo.relativeURL,
                                                        f['post_id'])
            f['postUrl'] = postUrl
            f['imgUrl'] = \
                '{0}/{1}'.format(fileBase, f['file_id']) if f['isImage'] else ''
            f['icon'] = get_icon(f['mime_type'])
        return files
