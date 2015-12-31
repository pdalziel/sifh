from libextract.api import extract


def extract_visable_text(html_path):
    textnodes = list(extract(html_path))
    text_str = unicode(''.join((e.text_content().encode('utf-8')) for e in textnodes))
    print text_str
    return text_str
