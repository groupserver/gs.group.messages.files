# -*- coding: utf-8 -*-
from zope.cachedescriptors.property import Lazy
from AccessControl import getSecurityManager
from gs.group.base.page import GroupPage
from gs.group.messages.topics.topicssearch import ICON_CHAR
from queries import FileQuery


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
            f['url'] = '{0}/{1}'.format(base, f['file_id'])
            f['postUrl'] = '{0}/messages/post/{1}'.format(
                                    self.groupInfo.relativeURL, f['post_id'])
            f['imgUrl'] = \
                '{0}/{1}'.format(fileBase, f['file_id']) if f['isImage'] else ''
            f['icon'] = ICON_CHAR.get(f['mime_type'][:5], ICON_CHAR['other'])
        return files
