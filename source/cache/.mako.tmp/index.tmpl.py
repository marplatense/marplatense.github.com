# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1343313330.143682
_enable_loop = True
_template_filename = '/home/mariano/Code/blog/env/local/lib/python2.7/site-packages/nikola/data/themes/default/templates/index.tmpl'
_template_uri = 'index.tmpl'
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
        lang = context.get('lang', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        def content():
            return render_content(context.locals_(__M_locals))
        disqus_forum = context.get('disqus_forum', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 45
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        def content():
            return render_content(context)
        disqus_forum = context.get('disqus_forum', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        for post in posts:
            # SOURCE LINE 5
            __M_writer(u'        <div style="border-bottom: 2px solid darkgrey; margin-bottom: 12px;">\n        <h1><a href="')
            # SOURCE LINE 6
            __M_writer(unicode(post.permalink(lang)))
            __M_writer(u'">')
            __M_writer(unicode(post.title(lang)))
            __M_writer(u'</a>\n        <small>&nbsp;&nbsp;\n             ')
            # SOURCE LINE 8
            __M_writer(unicode(messages[lang]["Posted:"]))
            __M_writer(u' ')
            __M_writer(unicode(post.date))
            __M_writer(u'\n        </small></h1>\n        <hr>\n        ')
            # SOURCE LINE 11
            __M_writer(unicode(post.text(lang, index_teasers)))
            __M_writer(u'\n        <p>\n')
            # SOURCE LINE 13
            if disqus_forum:
                # SOURCE LINE 14
                __M_writer(u'            <a href="')
                __M_writer(unicode(post.permalink()))
                __M_writer(u'#disqus_thread">Comments</a>\n')
            # SOURCE LINE 16
            __M_writer(u'        </div>\n')
        # SOURCE LINE 18
        __M_writer(u'    <div>\n<ul class="pager">\n')
        # SOURCE LINE 20
        if prevlink:
            # SOURCE LINE 21
            __M_writer(u'    <li class="previous">\n        <a href="')
            # SOURCE LINE 22
            __M_writer(unicode(prevlink))
            __M_writer(u'">')
            __M_writer(unicode(messages[lang]["&larr; Newer posts"]))
            __M_writer(u'</a>\n    </li>\n')
        # SOURCE LINE 25
        if nextlink:
            # SOURCE LINE 26
            __M_writer(u'    <li class="next">\n        <a href="')
            # SOURCE LINE 27
            __M_writer(unicode(nextlink))
            __M_writer(u'">')
            __M_writer(unicode(messages[lang]["Older posts &rarr;"]))
            __M_writer(u'</a>\n    </li>\n')
        # SOURCE LINE 30
        __M_writer(u'</ul>\n\n    </div>\n    <hr>\n')
        # SOURCE LINE 34
        if disqus_forum:
            # SOURCE LINE 35
            __M_writer(u'       <script type="text/javascript">\n        var disqus_shortname = \'')
            # SOURCE LINE 36
            __M_writer(unicode(disqus_forum))
            __M_writer(u"';\n        (function () {\n            var s = document.createElement('script'); s.async = true;\n            s.type = 'text/javascript';\n            s.src = 'http://' + disqus_shortname + '.disqus.com/count.js';\n            (document.getElementsByTagName('HEAD')[0] || document.getElementsByTagName('BODY')[0]).appendChild(s);\n        }());\n        </script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


