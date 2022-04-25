class Account():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def close(self):
        self.name = 0

    def actived(self):
        if self.value != 0:
            return True

