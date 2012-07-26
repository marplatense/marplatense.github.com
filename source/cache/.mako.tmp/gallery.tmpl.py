# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1343313330.165914
_enable_loop = True
_template_filename = '/home/mariano/Code/blog/env/local/lib/python2.7/site-packages/nikola/data/themes/default/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context.locals_(__M_locals))
        def extra_head():
            return render_extra_head(context.locals_(__M_locals))
        images = context.get('images', UNDEFINED)
        text = context.get('text', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 8
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        # SOURCE LINE 9
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 31
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        text = context.get('text', UNDEFINED)
        images = context.get('images', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'\n')
        # SOURCE LINE 12
        if text:
            # SOURCE LINE 13
            __M_writer(u'    <p>\n        ')
            # SOURCE LINE 14
            __M_writer(unicode(text))
            __M_writer(u'\n    </p>\n')
        # SOURCE LINE 17
        __M_writer(u'    <ul class="thumbnails">\n')
        # SOURCE LINE 18
        for image in images:
            # SOURCE LINE 19
            __M_writer(u'            <li><a href="')
            __M_writer(unicode(image[0]))
            __M_writer(u'" class="thumbnail" ')
            __M_writer(unicode(image[2]))
            __M_writer(u'>\n                <img src="')
            # SOURCE LINE 20
            __M_writer(unicode(image[1]))
            __M_writer(u'" /></a></li>\n')
        # SOURCE LINE 22
        __M_writer(u'    </ul>\n    <script type="text/javascript">\n        jQuery(\'a.thumbnail\').colorbox({\n            rel:\'gal\',\n            maxWidth:\'80%\',\n            maxHeight:\'80%\',\n            scalePhotos: true\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n    <link rel="stylesheet" href="/assets/css/colorbox.css" type="text/css"/>\n    <script src="/assets/js/jquery-1.7.2.min.js" type="text/javascript"></script>\n    <script src="/assets/js/jquery.colorbox-min.js" type="text/javascript"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


