from dataclasses import dataclass


@dataclass
class MerchantRules:
    max_amount: float | None = None
    blocked_currencies: list[str] | None = None


def check_business_rules(
    amount: float,
    currency: str,
    rules: MerchantRules
) -> str | None:

    if rules.max_amount is not None and amount > rules.max_amount:
        return "REJECT"

    if (
        rules.blocked_currencies is not None
        and currency in rules.blocked_currencies
    ):
        return "REJECT"

    return None