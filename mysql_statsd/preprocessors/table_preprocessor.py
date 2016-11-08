from interface import Preprocessor


class TablePreprocessor(Preprocessor):
    """Preprocessor for data returned in single row/multiple columns format (f.e.: SHOW SLAVE STATUS)"""
    def __init__(self, *args, **kwargs):
        super(TablePreprocessor, self).__init__(*args, **kwargs)

    def process(self, rows, column_names):
        if not rows:
            return []
        return [a for b in [zip(map(lambda c: row[0] + '.' + c, column_names[1:]), row[1:]) for row in rows] for a in b]
