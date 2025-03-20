from typing import Annotated

from .data import customers


def get_customer_by_name(name: Annotated[str, "Customer Name"]):
    """Returns customer details including address based on the name"""
    name_lower = name.lower()

    # Try exact match first
    exact_match = next(
        (customer for customer in customers if customer["name"].lower() == name_lower), None
    )
    if exact_match:
        return exact_match

    # If no exact match, return the first partial match
    return next(
        (customer for customer in customers if name_lower in customer["name"].lower()), None
    )


def create_customer(
    name: Annotated[str, "Customer Name"],
    city: Annotated[str, "City"],
    state: Annotated[str, "State"],
    country: Annotated[str, "Country"],
):
    """Creates a customer record given the customer name, city, state and country"""
    if any(customer["name"].lower() == name.lower() for customer in customers):
        return f"Customer {name} already exists."

    customers.append(
        {
            "id": max((customer["id"] for customer in customers), default=0) + 1,
            "name": name,
            "city": city,
            "state": state,
            "country": country,
        }
    )
    return f"Customer {name} successfully created"
