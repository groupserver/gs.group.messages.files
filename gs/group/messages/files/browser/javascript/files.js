// GroupServer JavaScript module for providing the Search mechanism
//
// Copyright © 2013 OnlineGroups.net and Contributors.
// All Rights Reserved.
//
// This software is subject to the provisions of the Zope Public License,
// Version 2.1 (ZPL). http://groupserver.org/downloads/license/
//
jQuery.noConflict();
function gs_group_messages_files_init_home() {
    var filesSearch=null, b=null, url=null;

    b = jQuery('base').attr('href');
    if (b[b.length -1] != '/') {
        b = b + '/';
    }
    url = b + 'gs-group-messages-files-ajax.html';

    filesSearch = GSSearch('#gs-group-messages-files-search', url, 0, 5, {}, 
                           null);
    filesSearch.load();
}

jQuery(window).load(function () {
    gsJsLoader.with_module('/++resource++gs-search-base-js-min-20131121.js',
                           gs_group_messages_files_init_home);
});
