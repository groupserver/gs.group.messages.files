jQuery.noConflict();
function gs_group_messages_files_init_home() {
    var filesSearch = null, b = null, url = null;

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
    gsJsLoader.with_module('/++resource++gs-search-base-js-min-20121217.js',
                           gs_group_messages_files_init_home);
});
