from datetime import date


def build_text_proposal(
    owner_name: str,
    scope_summary: str,
    service_lines: list[str],
    estimated_annual_revenue: float,
) -> str:
    services = "\n".join(f"- {line}" for line in service_lines)

    return f"""MCD Consulting LLC
Stormwater Maintenance Opportunity Summary

Date: {date.today().isoformat()}
Prospect: {owner_name}

Executive Summary
{scope_summary}

Recommended Services
{services}

Estimated Annual Maintenance Opportunity
${estimated_annual_revenue:,.0f}

Recommended Next Step
Verify ownership, confirm stormwater BMP locations, review any recorded O&M agreement, and schedule an initial site review.

Prepared by:
MCD Consulting LLC
"""
