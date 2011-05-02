from django.core.urlresolvers import NoReverseMatch, reverse
from django.template.base import Node
from django.template.base import TemplateSyntaxError
from django.conf import settings
from django.template.defaulttags import kwarg_re
from django.utils.encoding import smart_str
from django.template.base import Library
from django.core import urlresolvers

register = Library()

class URLNode(Node):
    def __init__(self, view_name, args, kwargs, asvar, legacy_view_name=True):
        self.view_name = view_name
        self.legacy_view_name = legacy_view_name
        self.args = args
        self.kwargs = kwargs
        self.asvar = asvar

    def render(self, context):
        args = [arg.resolve(context) for arg in self.args]
        kwargs = dict([(smart_str(k, 'ascii'), v.resolve(context))
                       for k, v in self.kwargs.items()])

        view_name = self.view_name
        if not self.legacy_view_name:
            view_name = view_name.resolve(context)

        url = ''
        try:
            url = reverse(str(self.view_name), args=args, kwargs=kwargs, current_app=context.current_app)
        except NoReverseMatch, e:
            if settings.SETTINGS_MODULE:
                project_name = settings.SETTINGS_MODULE.split('.')[0]
                try:
                    url = reverse(project_name + '.' + str(self.view_name),
                                  args=args, kwargs=kwargs,
                                  current_app=context.current_app)
                except NoReverseMatch:
                    if self.view_name:
                        try:
                            urlresolvers.set_urlconf('eliar.urls')
                            url = reverse(str(self.view_name), args=args, kwargs=kwargs,
                                          current_app=context.current_app)
                        except NoReverseMatch, e:
                            try:
                                url = reverse(project_name + '.' + str(self.view_name), args=args, kwargs=kwargs,
                                              current_app=context.current_app)
                            except NoReverseMatch, e:
                                if self.asvar is None:
                                    raise e
                    else:
                        raise e
            else:
                if self.asvar is None:
                    raise e

        if self.asvar:
            context[self.asvar] = url
            return ''
        else:
            return url


@register.tag
def url(parser, token):
    bits = token.split_contents()
    if len(bits) < 2:
        raise TemplateSyntaxError("'%s' takes at least one argument"
                                  " (path to a view)" % bits[0])
    viewname = parser.compile_filter(bits[1])
    if not viewname:
        raise Exception(token)
    args = []
    kwargs = {}
    asvar = None
    bits = bits[2:]
    if len(bits) >= 2 and bits[-2] == 'as':
        asvar = bits[-1]
        bits = bits[:-2]

    if len(bits):
        for bit in bits:
            match = kwarg_re.match(bit)
            if not match:
                raise TemplateSyntaxError("Malformed arguments to url tag")
            name, value = match.groups()
            if name:
                kwargs[name] = parser.compile_filter(value)
            else:
                args.append(parser.compile_filter(value))

    return URLNode(viewname, args, kwargs, asvar, legacy_view_name=False)
