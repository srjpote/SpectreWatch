def route_failure(error_type, confidence=0.0, has_evidence=False, repository_mapped=False):
    # Deterministic policy rules take precedence over model recommendations.
    if error_type == "business_exception":
        return {"route": "Finance", "coding_agent": False, "retry": False}
    if error_type == "credentials":
        return {"route": "ConnectionOwner", "coding_agent": False, "retry": False}
    if error_type == "timeout":
        return {"route": "RecoveryReview", "coding_agent": False, "retry": False}
    if error_type == "system_error":
        eligible = confidence >= 0.85 and has_evidence and repository_mapped
        return {"route": "CodingProposal" if eligible else "EngineeringReview",
                "coding_agent": eligible, "retry": False}
    return {"route": "HumanReview", "coding_agent": False, "retry": False}
