from spectrewatch.processor import Invoice, process_invoice
from spectrewatch.routing import route_failure

def test_success_total():
    result = process_invoice(Invoice("I1", "VEND-001", 1000, 100))
    assert result.status == "Completed"
    assert result.total == 1100

def test_missing_tax_is_system_error():
    result = process_invoice(Invoice("I2", "VEND-001", 1000, None))
    assert result.error_type == "system_error"

def test_business_exception_never_calls_coding_agent():
    result = process_invoice(Invoice("I3", "VEND-001", 6000, 100))
    route = route_failure(result.error_type)
    assert route["route"] == "Finance"
    assert route["coding_agent"] is False

def test_timeout_requires_recovery_review():
    route = route_failure("timeout")
    assert route["route"] == "RecoveryReview"
    assert route["retry"] is False

def test_credentials_go_to_connection_owner():
    route = route_failure("credentials")
    assert route["route"] == "ConnectionOwner"
    assert route["coding_agent"] is False

def test_coding_proposal_requires_all_gates():
    assert route_failure("system_error", .9, True, True)["coding_agent"] is True
    assert route_failure("system_error", .9, False, True)["coding_agent"] is False
    assert route_failure("system_error", .7, True, True)["coding_agent"] is False
    assert route_failure("system_error", .9, True, False)["coding_agent"] is False
