jQuery.noConflict();function gs_group_messages_files_init_home(){var c=null,a=null,d=null;
a=jQuery("base").attr("href");if(a[a.length-1]!="/"){a=a+"/"}d=a+"gs-group-messages-files-ajax.html";
c=GSSearch("#gs-group-messages-files-search",d,0,5,{},null);c.load()}jQuery(window).load(function(){gsJsLoader.with_module("/++resource++gs-search-base-js-min-20131121.js",gs_group_messages_files_init_home)
});