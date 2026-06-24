from pathlib import Path

import pandas as pd

from mcd.proposals.proposal_templates import build_text_proposal
from mcd.proposals.scope_builder import build_scope_summary, build_service_lines


def build_proposals(
    target_accounts: pd.DataFrame,
    output_dir: Path,
    top_n: int = 10,
) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)

    accounts = target_accounts.copy().head(top_n)
    paths: list[Path] = []

    for _, account in accounts.iterrows():
        owner_name = str(account.get("Owner_Name", account.get("Owner", "Unknown Owner")))
        safe_owner = (
            owner_name.replace("/", "-")
            .replace("\\", "-")
            .replace(":", "")
            .replace("*", "")
            .replace("?", "")
            .replace('"', "")
            .replace("<", "")
            .replace(">", "")
            .replace("|", "")
        )[:80]

        scope = build_scope_summary(account)
        service_lines = build_service_lines(account)
        estimated_revenue = float(account.get("Estimated_Total_Annual_Revenue", 0) or 0)

        proposal = build_text_proposal(
            owner_name=owner_name,
            scope_summary=scope,
            service_lines=service_lines,
            estimated_annual_revenue=estimated_revenue,
        )

        path = output_dir / f"{safe_owner}_stormwater_opportunity_summary.txt"
        path.write_text(proposal, encoding="utf-8")
        paths.append(path)

    return paths
