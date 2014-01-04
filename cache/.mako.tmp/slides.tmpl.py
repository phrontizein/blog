# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1388337811.363029
_enable_loop = True
_template_filename = u'/usr/local/lib/python2.7/dist-packages/nikola/data/themes/bootstrap3/templates/slides.tmpl'
_template_uri = u'slides.tmpl'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        content = context.get('content', UNDEFINED)
        range = context.get('range', UNDEFINED)
        carousel_id = context.get('carousel_id', UNDEFINED)
        len = context.get('len', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<div id="')
        __M_writer(unicode(carousel_id))
        __M_writer(u'" class="carousel slide">\n    <ol class="carousel-indicators">\n')
        # SOURCE LINE 3
        for i in range(len(content)):
            # SOURCE LINE 4
            if i == 0:
                # SOURCE LINE 5
                __M_writer(u'            <li data-target="#')
                __M_writer(unicode(carousel_id))
                __M_writer(u'" data-slide-to="')
                __M_writer(unicode(i))
                __M_writer(u'" class="active"></li>\n')
                # SOURCE LINE 6
            else:
                # SOURCE LINE 7
                __M_writer(u'            <li data-target="#')
                __M_writer(unicode(carousel_id))
                __M_writer(u'" data-slide-to="')
                __M_writer(unicode(i))
                __M_writer(u'"></li>\n')
        # SOURCE LINE 10
        __M_writer(u'    </ol>\n    <div class="carousel-inner">\n')
        # SOURCE LINE 12
        for i, image in enumerate(content):
            # SOURCE LINE 13
            if i == 0:
                # SOURCE LINE 14
                __M_writer(u'                <div class="item active"><img src="')
                __M_writer(unicode(image))
                __M_writer(u'" alt="" style="margin: 0 auto 0 auto;"></div>\n')
                # SOURCE LINE 15
            else:
                # SOURCE LINE 16
                __M_writer(u'                <div class="item"><img src="')
                __M_writer(unicode(image))
                __M_writer(u'" alt="" style="margin: 0 auto 0 auto;"></div>\n')
        # SOURCE LINE 19
        __M_writer(u'    </div>\n    <a class="left carousel-control" href="#')
        # SOURCE LINE 20
        __M_writer(unicode(carousel_id))
        __M_writer(u'" data-slide="prev"><span class="icon-prev"></span></a>\n    <a class="right carousel-control" href="#')
        # SOURCE LINE 21
        __M_writer(unicode(carousel_id))
        __M_writer(u'" data-slide="next"><span class="icon-next"></span></a>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


