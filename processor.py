from dataclasses import dataclass
from typing import Optional

VENDOR_LIMITS = {"VEND-001": 5000.0, "VEND-002": 10000.0}

@dataclass
class Invoice:
    invoice_id: str
    vendor_id: str
    amount: float
    tax_amount: Optional[float]
    scenario: str = "success"

@dataclass
class PerformerResult:
    status: str
    total: Optional[float] = None
    error_type: Optional[str] = None
    error_message: Optional[str] = None
    retryable: bool = False

def process_invoice(invoice: Invoice) -> PerformerResult:
    if invoice.scenario == "credential_failure":
        return PerformerResult("Failed", error_type="credentials",
            error_message="Connection authorization failed; secret details omitted.")
    if invoice.scenario == "system_timeout":
        return PerformerResult("Failed", error_type="timeout",
            error_message="Downstream dependency timed out.", retryable=True)
    if invoice.scenario == "application_null_tax" or invoice.tax_amount is None:
        return PerformerResult("Failed", error_type="system_error",
            error_message="Tax amount is missing; invoice total cannot be calculated.")
    limit = VENDOR_LIMITS.get(invoice.vendor_id)
    if invoice.scenario == "business_approval_limit" or limit is None or invoice.amount > limit:
        return PerformerResult("Failed", error_type="business_exception",
            error_message="Invoice exceeds or lacks a configured vendor approval limit.")
    return PerformerResult("Completed", total=round(invoice.amount + invoice.tax_amount, 2))
