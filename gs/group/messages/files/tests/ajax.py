# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2016 OnlineGroups.net and Contributors.
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
from mock import MagicMock, patch, PropertyMock
from unittest import TestCase
from gs.group.messages.files.ajax import (FilesAjax, )


class TestFilesAjax(TestCase):
    'Test the files AJAX endpoint'

    @patch.object(FilesAjax, 'groupInfo', new_callable=PropertyMock)
    def test_marshall_image(self, m_gI):
        'Test the marshalling of an image'
        fa = FilesAjax(MagicMock(), MagicMock())
        gi = fa.groupInfo
        gi.relativeURL = '/groups/example_group'
        f = {
            'mime_type': 'image/png',
            'file_id': 'example_file',
            'post_id': 'example_post',
        }

        r = fa.marshall_file(f)
        self.assertIn('isImage', r)
        self.assertTrue(r['isImage'])
        self.assertIn('url', r)
        self.assertIn('example_file', r['url'])
        self.assertIn('/groups/example_group', r['url'])
        self.assertIn('image', r['url'])

    @patch.object(FilesAjax, 'groupInfo', new_callable=PropertyMock)
    def test_marshall_file(self, m_gI):
        'Test the marshalling of a non-image'
        fa = FilesAjax(MagicMock(), MagicMock())
        gi = fa.groupInfo
        gi.relativeURL = '/groups/example_group'
        f = {
            'mime_type': 'application/x-gs-test',
            'file_id': 'example_file',
            'post_id': 'example_post',
        }

        r = fa.marshall_file(f)
        self.assertIn('isImage', r)
        self.assertFalse(r['isImage'])
        self.assertIn('url', r)
        self.assertIn('example_file', r['url'])
        self.assertIn('/groups/example_group', r['url'])
        self.assertIn('file', r['url'])
