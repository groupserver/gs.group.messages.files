===========================
``gs.group.messages.files``
===========================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The list of recently posted files in a group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2015-03-02
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
`Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

Introduction
============

In some groups the files that are posted are very important. To
support this, the *Files* list_ displays the files that have been
posted recently on the *Group* page. It also supplies a link to
the ATOM feed_ for the most-recent files.

List
====

The ``gs-group-messages-files-tab`` viewlet provides the space
for a list of recently posted files, in the Secondary part of the
Group page [#group]_.  An AJAX call is made by the JavaScript
resource_ for the list, which is loaded after the other resources
in the browser-window.

Each list item shows

* A square thumbnail, if the file is a photo,
* The file-name, and
* The topic name (linking to the topic).

Resource
--------

The JavaScript resource
``gs-group-messages-files-js-20120604.js`` [#min]_ loads the
files from the page ``gs-group-messages-files-ajax.html`` in the
Group context. It uses the ``GSSearch`` system to perform the
search [#search]_.

The resource is added to the Group page by the
``gs-group-messages-files-script`` viewlet.

Feed
====

A link to the ATOM of all files posted to the group is provided
by this product. It has the name ``gs-group-messages-files-link``
and relies on the viewlet manager providing the
``gs.group.home.interfaces.IGroupHomepageMetadata`` interface.

Resources
=========

- Code repository:
  https://github.com/groupserver/gs.group.messages.files
- Questions and comments to
  http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17

.. [#group] The files list uses the `viewlet manager`_
            ``gs.group.home.interfaces.IGroupHomepageSecondary``. See
            ``gs.group.home``
            <https://github.com/groupserver/gs.group.home>
.. _viewlet manager: http://docs.zope.org/zope.viewlet/
.. [#min] The minified version
          ``gs-group-messages-files-js-min-20120604.js`` is normally used.
.. [#search] See ``gs.search.base``
             <https://github.com/groupserver/gs.search.base>
