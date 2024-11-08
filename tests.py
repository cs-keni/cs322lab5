from bank import Account

def test_deposit():
  # Arrange
  acct = Account('owner', balance=0)
  assert acct.balance == 0

  # Act
  acct.deposit(10)

  # Assert
  assert acct.balance == 10


def test_withdraw():
  # Arrange
  acct = Account('owner', balance=10)
  assert acct.balance == 10

  # Act
  acct.withdraw(5)

  # Assert
  assert acct.balance == 5


def test_get_balance():
  # Arrange
  acct = Account('owner', balance=10)
  assert acct.balance == 10

  # Assert
  assert acct.get_balance() == 10


def test_transfer():
  # Arrange
  acct1 = Account('owner', balance=0)
  assert acct1.balance == 0

  acct2 = Account('owner', balance=10)
  assert acct2.balance == 10

  # Act
  acct2.transfer(10, acct1)

  # Assert
  assert acct1.balance == 10
  assert acct2.balance == 0
