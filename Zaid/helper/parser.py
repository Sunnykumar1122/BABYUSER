import html
import re


def cleanhtml(raw_html):
    cleanr = re.compile("<.*?>")
    cleantext = re.sub(cleanr, "", raw_html)
    return cleantext


def escape_markdown(text):
    """Helper function to escape telegram markup symbols."""
    escape_chars = r"\*_`\["
    return re.sub(r"([%s])" % escape_chars, r"\\\1", text)


def mention_html(user_id, name):
    return '<a href="tg:/t.me/ll_ROLEX_lll">{}</a>'.format(ll_ROLEX_lll, html.escape(BABY ROLEX))


def mention_markdown(user_id, name):
    return "[{ROLEX}](tg:/t.me/ll_ROLEX_lll)".format(escape_markdown(name), user_id)
