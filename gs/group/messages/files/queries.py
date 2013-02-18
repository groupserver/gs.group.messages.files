# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gs.database import getSession, getTable


class FileQuery(object):

    def __init__(self):
        self.postTable = getTable('post')
        self.fileTable = getTable('file')
        self.topicTable = getTable('topic')

    def recent_files(self, siteId, groupId, limit=5):
        pt = self.postTable
        ft = self.fileTable
        tt = self.topicTable
        cols = [pt.c.user_id, pt.c.post_id, ft.c.file_id, ft.c.mime_type,
                ft.c.file_name, ft.c.file_size, ft.c.date,
                tt.c.original_subject, pt.c.date.label('post_date')]
        s = sa.select(cols, order_by=(sa.desc('post_date')), limit=limit)
        s.append_whereclause(pt.c.group_id == groupId)
        s.append_whereclause(pt.c.site_id == siteId)
        s.append_whereclause(pt.c.hidden == None)  # lint:ok
        s.append_whereclause(pt.c.post_id == ft.c.post_id)
        s.append_whereclause(pt.c.topic_id == tt.c.topic_id)

        session = getSession()
        r = session.execute(s)
        if r.rowcount:
            retval = [{'user_id': row['user_id'],
                        'file_id': row['file_id'],
                        'mime_type': row['mime_type'],
                        'name': row['file_name'],
                        'size': row['file_size'],
                        'date': row['date'],
                        'post_date': row['post_date'],
                        'post_id': row['post_id'],
                        'subject': row['original_subject']} for row in r]
        return retval
