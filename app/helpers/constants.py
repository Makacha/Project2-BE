
class Compare:
    LIKE = 'LIKE'
    LIKE_BEGIN = 'LIKE_BEGIN'
    EQUAL = 'EQ'
    GREATER_EQUAL = 'GE'
    LESS_EQUAL = 'LE'
    GREATER = 'GT'
    LESS = 'LT'
    IN_LIST = 'LIST'
    SIMILAR_EQUAL = 'SEQ'
    NOT_EQUAL = 'NEQ'

    @staticmethod
    def get_list():
        return ['LIKE', 'LIKE_BEGIN', 'EQ', 'GE', 'LE', 'GT', 'LT', 'LIST', 'SEQ', 'NEQ']
