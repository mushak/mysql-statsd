from interface import Preprocessor


class ColumnsPreprocessor(Preprocessor):
    """Preprocessor for data returned in single row/multiple columns format (f.e.: SHOW SLAVE STATUS)"""
    def __init__(self, *args, **kwargs):
        super(ColumnsPreprocessor, self).__init__(*args, **kwargs)

    def process(self, rows, column_names):
        if not rows:
            return []
        return [a for b in [zip(column_names, row) for row in rows] for a in b]
