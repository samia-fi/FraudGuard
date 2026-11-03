from app.services.fraud_engine import (
    MerchantRules,
    check_business_rules,
)


def test_amount_below_maximum_is_not_rejected():
    rules = MerchantRules(max_amount=10000)

    result = check_business_rules(
        amount=250.50,
        currency="MAD",
        rules=rules,
    )

    assert result is None


def test_amount_above_maximum_is_rejected():
    rules = MerchantRules(max_amount=10000)

    result = check_business_rules(
        amount=15000,
        currency="MAD",
        rules=rules,
    )

    assert result == "REJECT"


def test_blocked_currency_is_rejected():
    rules = MerchantRules(
        max_amount=10000,
        blocked_currencies=["EUR"],
    )

    result = check_business_rules(
        amount=250,
        currency="EUR",
        rules=rules,
    )

    assert result == "REJECT"