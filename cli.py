import argparse
import json
from dataclasses import asdict
from .processor import Invoice, process_invoice
from .routing import route_failure

def main():
    parser = argparse.ArgumentParser(description="Run a SpectreWatch invoice simulation")
    parser.add_argument("--scenario", choices=[
        "success", "application_null_tax", "business_approval_limit",
        "system_timeout", "credential_failure"
    ], default="success")
    scenario = parser.parse_args().scenario
    tax = None if scenario == "application_null_tax" else 125.0
    invoice = Invoice("INV-DEMO-1001", "VEND-001", 1250.0, tax, scenario)
    result = process_invoice(invoice)
    output = {"scenario": scenario, "performer_result": asdict(result)}
    if result.status == "Failed":
        output["policy_route"] = route_failure(result.error_type)
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
