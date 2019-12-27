class Parser:
    @staticmethod
    def clean_html_tags(soupFile, reParser, filters=['script', 'style', 'meta', 'noscript']):
        for line in soupFile(filters):
            line.decompose()
        return reParser.sub('', ''.join(soupFile.stripped_strings))
