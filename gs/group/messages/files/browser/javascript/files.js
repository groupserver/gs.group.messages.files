jQuery.noConflict();
var GSGroupFilesTab = function () {
    // Private variables
    // Widgets
    var toolbar = null;
    var prevButton = null;
    var nextButton = null;
    var latestFiles = null;
    var loadingMessage = null;
    // Search Info
    var ajaxPage = '/s/search.ajax';
    var groupId = null;
    var offset = null;
    var limit = null;
    var toolbarShown = true;
    // Constants
    var MAX_ITEMS = 6;
    var FADE_SPEED = 'slow';
    var FADE_METHOD = 'swing';
    
    // Next button
    var init_next_button = function() {
        nextButton = jQuery('#gs-group-messages-files-toolbar-next');
        nextButton.button({
            text: true,
            icons: { secondary: 'ui-icon-carat-1-e', },
            disabled: true,
        });
        nextButton.click(handle_next);
    };// init_next_button
    var handle_next = function(eventObject) {
        offset = offset + limit;
        latestFiles.fadeOut(FADE_SPEED, FADE_METHOD, do_files_load);
    };//handle_next
    
    // Previous Button
    var init_prev_button = function() {
        prevButton = jQuery('#gs-group-messages-files-toolbar-prev');
        prevButton.button({
            text: true,
            icons: { primary: 'ui-icon-carat-1-w', },
            disabled: true,
        });
        prevButton.click(handle_prev);
    };// init_prev_button
    var handle_prev = function(eventObject) {
        offset = offset - limit;
        if (offset < 0) {
            offset = 0
        }
        latestFiles.fadeOut(FADE_SPEED, FADE_METHOD, do_files_load);
    };//handle_prev

    // Code to load the files in a pleasing way.
    var do_files_load = function () {
        // Function used by the buttons.
        loadingMessage.fadeIn(FADE_SPEED, FADE_METHOD, load_files);
    };//do_files_load
    var load_files = function() {
        // Actually load the files, making am AJAX request
        var data = {
            'i': offset,
            'l': limit,
            'g': groupId,            
            't': '0',
            'p': '0',
            'f': '1'
        };
        jQuery.post(ajaxPage, data, load_complete);
    };// load_files
    var load_complete = function(responseText, textStatus, request) {
        // Set the contents of the Files list to the respose.
        latestFiles.html(responseText);
        // Hide the Loading message and show the files
        loadingMessage.fadeOut(FADE_SPEED, FADE_METHOD, show_files);
    };// load_complete
    var show_files = function () {
        // Show the files list, and enable the buttons as required.
        var nFiles = null;
        latestFiles.fadeIn(FADE_SPEED, FADE_METHOD);
        prevButton.button('option', 'disabled', offset <= 0);
        
        nFiles = latestFiles.find('.file').length;
        nextButton.button('option', 'disabled', nFiles < limit);
        
        if ((offset <= 0) && (nFiles < limit) && toolbarShown) {
            toolbar.fadeOut('fast', FADE_METHOD);
            toolbarShown = false;
        } else if (((offset > 0) || (nFiles >= limit)) && !toolbarShown) {
            toolbar.fadeIn('fast', FADE_METHOD);
            toolbarShown = true;
        }
    };//show_files
    
    // Public methods and properties.
    return {
        init: function (gid) {
            groupId = gid;
            limit = 6;
            offset = 0;
        
            init_prev_button();
            init_next_button();
            
            latestFiles = jQuery('#gs-group-messages-files-latest');
            loadingMessage = jQuery('#gs-group-messages-files-loading');
            toolbar = jQuery('#gs-group-messages-files-toolbar');
            
            load_files();
        },//init
    };
}(); // GSGroupFilesTab

