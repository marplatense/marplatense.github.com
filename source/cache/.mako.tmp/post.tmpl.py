# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1343313330.103953
_enable_loop = True
_template_filename = '/home/mariano/Code/blog/env/local/lib/python2.7/site-packages/nikola/data/themes/site/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'sourcelink']


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
        title = context.get('title', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context.locals_(__M_locals))
        len = context.get('len', UNDEFINED)
        def content():
            return render_content(context.locals_(__M_locals))
        link = context.get('link', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        disqus_forum = context.get('disqus_forum', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 55
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        # SOURCE LINE 61
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        title = context.get('title', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def content():
            return render_content(context)
        link = context.get('link', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        disqus_forum = context.get('disqus_forum', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    <h1>')
        # SOURCE LINE 4
        __M_writer(unicode(title))
        __M_writer(u'</h1>\n')
        # SOURCE LINE 5
        if link:
            # SOURCE LINE 6
            __M_writer(u"            <p><a href='")
            __M_writer(unicode(link))
            __M_writer(u"'>")
            __M_writer(unicode(messages[lang]["Original site"]))
            __M_writer(u'</a></p>\n')
        # SOURCE LINE 8
        __M_writer(u'    <hr>\n    <small>\n        ')
        # SOURCE LINE 10
        __M_writer(unicode(messages[lang]["Posted:"]))
        __M_writer(u' ')
        __M_writer(unicode(post.date))
        __M_writer(u'\n\n')
        # SOURCE LINE 12
        if len(translations) > 1:
            # SOURCE LINE 13
            for langname in translations.keys():
                # SOURCE LINE 14
                if langname != lang:
                    # SOURCE LINE 15
                    __M_writer(u'                    &nbsp;&nbsp;|&nbsp;&nbsp;\n                    <a href="')
                    # SOURCE LINE 16
                    __M_writer(unicode(post.permalink(langname)))
                    __M_writer(u'">')
                    __M_writer(unicode(messages[langname][u"Read in English"]))
                    __M_writer(u'</a>\n')
        # SOURCE LINE 20
        if post.tags:
            # SOURCE LINE 21
            __M_writer(u'            &nbsp;&nbsp;|&nbsp;&nbsp;')
            __M_writer(unicode(messages[lang]["More posts about"]))
            __M_writer(u'\n')
            # SOURCE LINE 22
            for tag in post.tags:
                # SOURCE LINE 23
                __M_writer(u'                <a href="')
                __M_writer(unicode(_link("tag", tag, lang)))
                __M_writer(u'"><span class="badge badge-info">')
                __M_writer(unicode(tag))
                __M_writer(u'</span></a>\n')
        # SOURCE LINE 26
        __M_writer(u'    </small>\n    <hr>\n    ')
        # SOURCE LINE 28
        __M_writer(unicode(post.text(lang)))
        __M_writer(u'\n    <ul class="pager">\n')
        # SOURCE LINE 30
        if post.prev_post:
            # SOURCE LINE 31
            __M_writer(u'        <li class="previous">\n            <a href="')
            # SOURCE LINE 32
            __M_writer(unicode(post.prev_post.permalink(lang)))
            __M_writer(u'">')
            __M_writer(unicode(messages[lang]["&larr; Previous post"]))
            __M_writer(u'</a>\n        </li>\n')
        # SOURCE LINE 35
        if post.next_post:
            # SOURCE LINE 36
            __M_writer(u'        <li class="next">\n            <a href="')
            # SOURCE LINE 37
            __M_writer(unicode(post.next_post.permalink(lang)))
            __M_writer(u'">')
            __M_writer(unicode(messages[lang]["Next post &rarr;"]))
            __M_writer(u'</a>\n        </li>\n')
        # SOURCE LINE 40
        __M_writer(u'    </ul>\n')
        # SOURCE LINE 41
        if disqus_forum:
            # SOURCE LINE 42
            __M_writer(u'        <div id="disqus_thread"></div>\n        <script type="text/javascript">\n            var disqus_shortname = \'')
            # SOURCE LINE 44
            __M_writer(unicode(disqus_forum))
            __M_writer(u"';\n            var disqus_url = '")
            # SOURCE LINE 45
            __M_writer(unicode(post.permalink(absolute=True)))
            __M_writer(u'\';\n            (function() {\n                var dsq = document.createElement(\'script\'); dsq.type = \'text/javascript\'; dsq.async = true;\n                dsq.src = \'http://\' + disqus_shortname + \'.disqus.com/embed.js\';\n                (document.getElementsByTagName(\'head\')[0] || document.getElementsByTagName(\'body\')[0]).appendChild(dsq);\n            })();\n        </script>\n        <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>\n        <a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 57
        __M_writer(u'\n    <li>\n    <a href="')
        # SOURCE LINE 59
        __M_writer(unicode(post.pagenames[lang]+post.source_ext()))
        __M_writer(u'">reSt</a>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


