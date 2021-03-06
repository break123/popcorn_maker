import bleach


# Initial list borrowed from webmaker

ALLOWED_TAGS = [
    "a", "abbr", "address", "area", "article",
    "aside", "audio", "b", "bdi", "bdo", "blockquote", "br",
    "button", "canvas", "caption", "cite", "code", "col", "colgroup",
    "command", "datalist", "dd", "del", "details", "dfn", "div", "dl", "dt",
    "em", "embed", "figcaption", "figure", "footer",
    "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hgroup", "hr",
    "i", "img", "ins", "keygen", "kbd", "label",
    "legend", "li", "map", "mark", "menu", "meter", "nav",
    "ol", "optgroup", "output", "p", "param",
    "pre", "progress", "q", "rp", "rt", "s", "samp", "section",
    "small", "source", "span", "strong", "sub", "summary", "sup",
    "table", "tbody", "td", "tfoot", "th", "thead", "time",
    "tr", "track", "u", "ul", "var", "video", "wbr"
    ]

ALLOWED_ATTRS = {
    "meta": ["charset", "name", "content"],
    "*": ["class", "id", "data-butter", "data-butter-default"],
    "img": ["src", "width", "height"],
    "a": ["href"],
    "video": ["src", "controls"],
    "source": ["src"],
}


def clean(stream):
    return bleach.clean(stream, strip=True, strip_comments=False,
                        tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRS)
