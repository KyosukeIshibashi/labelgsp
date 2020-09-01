class img_iter(iter):

    def __init__(self, obj):
        assert type(obj) == list "Argument Error: type of obj must be list"
        self.obj = obj
        self.idx = 0

    def current(self):
        return self.obj[self.idx]

    def next(self):
        if self.idx >= obj(len) - 1:
            return None
        else:
            self.idx = self.idx + 1
            return self.obj[self.idx]

    def prev(self):
        if self.idx <= 0:
            return None
        else:
            self.idx = self.idx - 1
            return self.obj[self.idx]

    def show(self):
        return self.obj

    def __len__(self):
        return len(self.obj)

    def empty(self):
        return len(self.obj) == 0
