# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1343313330.171948
_enable_loop = True
_template_filename = '/home/mariano/Code/blog/env/local/lib/python2.7/site-packages/nikola/data/themes/default/templates/listing.tmpl'
_template_uri = 'listing.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content']


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
        code = context.get('code', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 10
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        code = context.get('code', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n<ul class="breadcrumb">\n')
        # SOURCE LINE 5
        for link, crumb in crumbs:
            # SOURCE LINE 6
            __M_writer(u'        <li><a href="')
            __M_writer(unicode(link))
            __M_writer(u'">/ ')
            __M_writer(unicode(crumb))
            __M_writer(u'</a></li>\n')
        # SOURCE LINE 8
        __M_writer(u'</ul>\n')
        # SOURCE LINE 9
        __M_writer(unicode(code))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


