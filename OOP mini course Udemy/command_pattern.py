from abc import ABCMeta, abstractmethod


class Transaction(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class SELECT(Transaction):
    def __init__(self, transaction):
        self.trans = transaction

    def execute(self):
        self.trans.SELECT()


class INSERT(Transaction):
    def __init__(self, transaction):
        self.trans = transaction

    def execute(self):
        self.trans.INSERT()


class UPDATE(Transaction):
    def __init__(self, transaction):
        self.trans = transaction

    def execute(self):
        self.trans.UPDATE()


class TransactionManager:
    def SELECT(self):
        print("Performing SELECT operation")

    def INSERT(self):
        print("Performing INSERT operation")

    def UPDATE(self):
        print("Performing UPDATE operation")

    def requestTransaction(self, tr_select):
        pass


class TransactionBroker:
    def __init__(self):
        self.__transactionQueue = []

    def request_transaction(self, transaction):
        self.__transactionQueue.append(transaction)
        transaction.execute()


if __name__ == '__main__':
    transaction = TransactionManager()
    tr_select = SELECT(transaction)
    tr_insert = INSERT(transaction)
    tr_update = UPDATE(transaction)

    brkr = TransactionManager()
    brkr.requestTransaction(tr_select)
    brkr.requestTransaction(tr_insert)
    brkr.requestTransaction(tr_update)
    brkr.requestTransaction(tr_select)
    brkr.requestTransaction(tr_insert)
    brkr.requestTransaction(tr_update)