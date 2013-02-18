jQuery.noConflict();
function gs_group_messages_files_init_home() {
    // HACK to get the group ID for the AJAX.
    var bodyId = null, gId = null, e = /_.*$/, filesSearch = null, d = null,
        show_files = null;

    bodyId = jQuery('body').attr('id');
    gId = String(e.exec(bodyId)).slice(1);
    d = {'g': gId, 't': '0', 'f': '1'};
    filesSearch = GSSearch('#gs-group-messages-files-search',
                           '/s/search.ajax', 0, 5, d, null);
    filesSearch.load();
}

jQuery(window).load(function () {
    gsJsLoader.with_module('/++resource++gs-search-base-js-min-20121217.js',
                           gs_group_messages_files_init_home);
});
