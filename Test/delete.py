class Account():
    def __init__(self,name,value):
        self.name=name
        self.value=value

    def close(self):
        self.name=0

    def actived(self):
        if self.value!=0:
            return True


def newaccount():
    return Account("mr.Bond",10)

def close_account(account):
    account.close
    del account



account = newaccount()
print(not account.actived())



