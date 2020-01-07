from enum import Enum


class PaymentMethod(Enum):
    MANUAL = 'MN'
    AUTO = 'AU'
    SEMAUTO = 'SA'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class PaymentSystem(Enum):
    PRIVAT = 'PB'
    PAYPAL = 'PP'
    BANK_ACCOUNT = 'BA'
    PAYONEER = 'PO'
    CREDIT_CARD = 'CC'
    CASH = 'CH'
    BY_CHOICE = 'BC'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class Currency(Enum):
    UAH = 'UAH'
    USD = 'USD'
    EUR = 'EUR'
    GBP = 'GBP'
    RUB = 'RUB'
    CAD = 'CAD'
    PLN = 'PLN'
    CZK = 'CZK'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class Ceo(Enum):
    YES = 'YES'
    NO = 'NO'
    ON_HOLD = 'OH'
    CANCELLED = 'CNC'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
