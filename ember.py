from django import template

register = template.Library()


@register.tag(name='linkto')
def do_linkto(parser, token):
    nodelist = parser.parse(('endlinkto',))
    args = token.split_contents()[1:]
    if not args:
        raise template.TemplateSyntaxError("{0} tag requires at least one argument".format(token.contents.split()[0]))
    parser.delete_first_token()
    return LinkToNode(nodelist, *args)


class LinkToNode(template.Node):
    def __init__(self, nodelist, *args):
        self.args = args
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return "{{#linkTo " + " ".join(self.args) + '}}' + output + "{{/linkTo}}"


@register.tag(name='ember')
def do_ember(parser, token):
    tokens = token.split_contents()
    args = " ".join(tokens[1:])
    #parser.delete_first_token()
    return EmberTagNode(args)


class EmberTagNode(template.Node):
    def __init__(self, args):
        self.args = args

    def render(self, context):
        return "{{" + self.args + "}}"
