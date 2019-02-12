class Market:
    articles = []
    valid_from = None
    valid_until = None
    name = None

    def __init__(self, name):
        self.name = name