from threading import RLock


class Bank2:
    def __init__(self, balance: List[int]):
        self.accounts: List[Account] = [Account(amount) for amount in balance]

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        acc1: Account = self.get_account(account1)
        acc2: Account = self.get_account(account2)

        if not acc1 or not acc2 or acc1.balance < money or money < 0:
            return False

        with acc1.lock and acc2.lock:
            if acc1.withdraw(money):
                acc2.deposit(money)
            else:
                return False

        return True

    def deposit(self, account: int, money: int) -> bool:
        acc: Account = self.get_account(account)

        if not acc or money < 0:
            return False

        acc.deposit(money)

        return True

    def withdraw(self, account: int, money: int) -> bool:
        acc: Account = self.get_account(account)

        if not acc or acc.balance < money:
            return False

        acc.withdraw(money)

        return True

    def get_account(self, account: int):
        return self.accounts[account - 1] if account <= len(self.accounts) else None


class Account:
    def __init__(self, balance: int):
        self.balance = balance
        self.lock = RLock()

    def deposit(self, amount: int) -> bool:
        with self.lock:
            self.balance += amount

        return True

    def withdraw(self, amount: int) -> bool:
        with self.lock:
            self.balance -= amount

        return True


class Bank1:
    """
    Note:
        - "Valid" transactions:
            - 1 < account number < n
            - amount <= balance[account_number]
                - When "withdrawing" and "tranferring"
    Steps:
        1. object intializes object with
    """

    def __init__(self, balance: List[int]):
        # TC: O(n) / SC: O(n)
        self.accounts = {i + 1: [amount] for i, amount in enumerate(balance)}

    def _get_account(self, account: int) -> List[int] | None:
        # TC: O(1)
        return self.accounts.get(account, None)

    def deposit(self, account: int, money: int) -> bool:
        """
        Conditions:
            1. if transaction successful:
                - return True
            2. else:
                - return False
        Successful:
            - account exists
            - money is valid:
                - no negative deposit
                - money must be int
        Unsuccessful:
            - account number doesn't exist
            - money isn't valid:
                - negative deposit
                - money in type other than int
        """
        # TC: O(1)
        account = self._get_account(account)

        if money < 0 or not isinstance(money, int) or not account:
            return False

        account.append(account[-1] + money)

        return True

    def withdraw(self, account: int, money: int) -> bool:
        """
        Successful:
            - account exists
            - money <= balance
        Unsuccessful:
            - account doesn't exist
            - money > balance
        """
        # TC: O(1)
        account = self._get_account(account)

        if not account or money > account[-1] or not isinstance(money, int):
            return False

        account.append(account[-1] - money)

        return True

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        """
        Successful:
            - account1 AND account2 exists
            - account1's balance <= balance
        """
        # TC: O(1)
        acc1 = self._get_account(account1)
        acc2 = self._get_account(account2)

        if not acc1 or not acc2 or money > acc1[-1] or not isinstance(money, int):
            return False

        self.withdraw(account1, money)
        self.deposit(account2, money)

        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
