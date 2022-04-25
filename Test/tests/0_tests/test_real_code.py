from Account import Account

def test_account_create(newaccount):
    assert isinstance(newaccount, Account), "Account is not correct"


def test_account_not_active(newaccount):
    assert (not newaccount.actived()), "Account is actived"
