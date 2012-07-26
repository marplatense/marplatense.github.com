# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1343313330.123024
_enable_loop = True
_template_filename = u'/home/mariano/Code/blog/env/local/lib/python2.7/site-packages/nikola/data/themes/site/templates/base.tmpl'
_template_uri = u'base.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'sourcelink', u'belowtitle']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        lang = context.get('lang', UNDEFINED)
        def extra_head():
            return render_extra_head(context.locals_(__M_locals))
        permalink = context.get('permalink', UNDEFINED)
        exists = context.get('exists', UNDEFINED)
        title = context.get('title', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context.locals_(__M_locals))
        search_form = context.get('search_form', UNDEFINED)
        sidebar_links = context.get('sidebar_links', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        content_footer = context.get('content_footer', UNDEFINED)
        len = context.get('len', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        analytics = context.get('analytics', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def belowtitle():
            return render_belowtitle(context.locals_(__M_locals))
        rel_link = context.get('rel_link', UNDEFINED)
        def content():
            return render_content(context.locals_(__M_locals))
        blog_title = context.get('blog_title', UNDEFINED)
        add_this_buttons = context.get('add_this_buttons', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<!DOCTYPE html>\n<html lang="')
        # SOURCE LINE 3
        __M_writer(unicode(lang))
        __M_writer(u'">\n<head>\n    <meta charset="utf-8">\n    <title>')
        # SOURCE LINE 6
        __M_writer(unicode(title))
        __M_writer(u'</title>\n    <!-- Le styles -->\n    <link href="/assets/css/bootstrap.css" rel="stylesheet" type="text/css">\n    <link href="/assets/css/bootstrap-responsive.css" rel="stylesheet" type="text/css">\n    <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n    <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n')
        # SOURCE LINE 12
        if exists("files/assets/css/custom.css", not_empty=True):
            # SOURCE LINE 13
            __M_writer(u'    <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        # SOURCE LINE 15
        __M_writer(u'    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->\n    <!--[if lt IE 9]>\n      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>\n    <![endif]-->\n')
        # SOURCE LINE 19
        if rss_link:
            # SOURCE LINE 20
            __M_writer(u'        ')
            __M_writer(unicode(rss_link))
            __M_writer(u'\n')
            # SOURCE LINE 21
        else:
            # SOURCE LINE 22
            for language in translations:
                # SOURCE LINE 23
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" title="RSS (')
                __M_writer(unicode(language))
                __M_writer(u')" href="')
                __M_writer(unicode(_link("rss", None, lang)))
                __M_writer(u'">\n')
        # SOURCE LINE 26
        __M_writer(u'    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 27
        __M_writer(u'\n</head>\n<body>\n<!-- Menubar -->\n<div class="navbar navbar-fixed-top">\n    <div class="navbar-inner">\n        <div class="container">\n            <a class="brand" href="')
        # SOURCE LINE 34
        __M_writer(unicode(abs_link('/')))
        __M_writer(u'">\n            ')
        # SOURCE LINE 35
        __M_writer(unicode(blog_title))
        __M_writer(u'\n            </a>\n            <ul class="nav">\n')
        # SOURCE LINE 38
        for url, text in sidebar_links[lang]:
            # SOURCE LINE 39
            if rel_link(permalink, url) == "#":
                # SOURCE LINE 40
                __M_writer(u'                        <li class="active"><a href="')
                __M_writer(unicode(url))
                __M_writer(u'">')
                __M_writer(unicode(text))
                __M_writer(u'</a>\n')
                # SOURCE LINE 41
            else:
                # SOURCE LINE 42
                __M_writer(u'                        <li><a href="')
                __M_writer(unicode(url))
                __M_writer(u'">')
                __M_writer(unicode(text))
                __M_writer(u'</a>\n')
        # SOURCE LINE 45
        __M_writer(u'            </ul>\n')
        # SOURCE LINE 46
        if search_form:
            # SOURCE LINE 47
            __M_writer(u'                ')
            __M_writer(unicode(search_form))
            __M_writer(u'\n')
        # SOURCE LINE 49
        __M_writer(u'            <ul class="nav pull-right">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        # SOURCE LINE 60
        __M_writer(u'\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        # SOURCE LINE 61
        __M_writer(u'\n            </ul>\n        </div>\n    </div>\n</div>\n<!-- End of Menubar -->\n\n<div class="container" id="container" style="margin-top: 50px;">\n    <!--Body content-->\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 70
        __M_writer(u'\n    <!--End of body content-->\n</div>\n    <div class="span12" style="text-align: center;">\n    <hr>\n    <small>')
        # SOURCE LINE 75
        __M_writer(unicode(content_footer))
        __M_writer(u'</small>\n    </div>\n')
        # SOURCE LINE 77
        if add_this_buttons:
            # SOURCE LINE 78
            __M_writer(u'    <!-- addthis -->\n    <div class="addthis_bar addthis_bar_vertical addthis_bar_small" style="top:50px;left:10px;">\n        <div class="addthis_toolbox addthis_default_style">\n            <span><a class="addthis_button_preferred_1"></a></span>\n            <span><a class="addthis_button_preferred_2"></a></span>\n            <span><a class="addthis_button_preferred_3"></a></span>\n            <span><a class="addthis_button_preferred_4"></a></span>\n            <span><a class="addthis_button_compact"></a></span>\n        </div>\n    </div>\n    <script type="text/javascript" src="http://s7.addthis.com/js/300/addthis_widget.js#pubid=ra-4f7088a56bb93798"></script>\n    <!-- End of addthis -->\n')
        # SOURCE LINE 91
        __M_writer(unicode(analytics))
        __M_writer(u'\n</body>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        # SOURCE LINE 26
        __M_writer(u'\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        # SOURCE LINE 61
        __M_writer(u' ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        def belowtitle():
            return render_belowtitle(context)
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 50
        __M_writer(u'\n')
        # SOURCE LINE 51
        if len(translations) > 1:
            # SOURCE LINE 52
            __M_writer(u'                    <li>\n')
            # SOURCE LINE 53
            for langname in translations.keys():
                # SOURCE LINE 54
                if langname != lang:
                    # SOURCE LINE 55
                    __M_writer(u'                            <a href="')
                    __M_writer(unicode(_link("index", None, langname)))
                    __M_writer(u'">')
                    __M_writer(unicode(messages[langname]["LANGUAGE"]))
                    __M_writer(u'</a>\n')
            # SOURCE LINE 58
            __M_writer(u'                    </li>\n')
        # SOURCE LINE 60
        __M_writer(u'            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


