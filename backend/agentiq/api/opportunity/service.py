from typing import Annotated

from .models import Stage
from .data import opportunities


def get_opportunity_by_name(name: Annotated[str, "Opportunity Name"]):
    """Returns opportunity details based on the name"""
    name_lower = name.lower()

    # Try exact match first
    exact_match = next(
        (opportunity for opportunity in opportunities if opportunity["name"].lower() == name_lower),
        None,
    )
    if exact_match:
        return exact_match

    # If no exact match, return the first partial match
    return next(
        (opportunity for opportunity in opportunities if name_lower in opportunity["name"].lower()),
        None,
    )


def create_opportunity(
    name: Annotated[str, "Opportunity Name"],
    customer_id: Annotated[int, "Customer ID"],
    amount: Annotated[float, "Amount"],
):
    """Creates an opportunity record given the opportunity name, customer id and amount"""
    opportunities.append(
        {
            "id": max((opportunity["id"] for opportunity in opportunities), default=0) + 1,
            "name": name,
            "customer_id": customer_id,
            "amount": amount,
            "stage": Stage.open,
        }
    )
    return f"Opportunity {name} successfully created"


def close_opportunity(
    name: Annotated[str, "Opportunity Name"], stage: Annotated[str, "Opportunity Stage"] = None
):
    """Closes an opportunity given the opportunity name and stage"""
    if stage is None:
        return "Please ask the user to specify the stage as either 'Closed Won' or 'Closed Lost'."

    if stage not in [Stage.closed_won, Stage.closed_lost]:
        return "Invalid stage. Please specify the stage as either 'Closed Won' or 'Closed Lost'."

    opportunity = get_opportunity_by_name(name)
    if not opportunity:
        return f"Opportunity {name} not found."

    if opportunity["stage"] != Stage.open:
        return f"Opportunity {name} is already closed."

    opportunity["stage"] = stage
    return f"Opportunity {name} successfully closed with stage {stage}"
