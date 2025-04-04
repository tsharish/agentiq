<div align="center">

![Agentiq Logo](assets/agentiq_logo.png)

</div>

Agentiq is an easy-to-use AI agent framework developed using Python and uses Cohere's [Command R+ model](https://docs.cohere.com/v2/docs/command-r-plus) and [API](https://docs.cohere.com/v2/reference/about). It has minimal dependencies and does not rely on LangChain or other agent frameworks. This repo consists of 2 parts - the Core agent framework and a Web App for demonstrating the functionality.

## Core
Agents interact with their environment and perform actions using *Tools*. In Agentiq, tools are nothing but Python functions. Consider the below function that creates an event in a user's calendar.

```
def create_event(
    name: Annotated[str, "Name of the event"],
    date: Annotated[str, "Date of the event, formatted as YYYY-MM-DD"],
    start_time: Annotated[str, "Start time of the event, formatted as HH:MM"],
    end_time: Annotated[str, "End time of the event, formatted as HH:MM"],
):
    """Creates a new event based on event name, date, start and end time"""
    new_event = {"name": name, "date": date, "start_time": start_time, "end_time": end_time}
    events.append(new_event)
    return f"Event '{name}' created successfully for {date} from {start_time} to {end_time}"
```

This can be converted into a tool with the following code:
```
create_event_tool = Tool(create_event)
```

An *Agent* can then be created by providing a list of tools available to it.
```
event_agent = Agent([create_event_tool])
```

A *system message* can also be provided to the agent to give it more context. The system message can either be a string or a function including a lambda.
```
tools = [create_event_tool]
system_message = lambda: f"Today is {date.today()}"
event_agent = Agent(tools=tools, system_message=system_message)
```

The agent can be invoked using its *run* method.
```
generator = event_agent.run(message="Create an hour-long appointment for the first available free slot after 9am titled Client Meeting")
for response in generator:
    print(response)
```

## Web App
The Web App is a basic CRM system that demonstrates the Agentiq framework. The following outlines the various functionalities of the web app and the tools in each.

### Customers
The Customers section displays all customer records. Here are the tools available for managing customer information:

| Tool	| Example Prompts |
| ------- | ----------------- |
| get_customer_by_name: Returns customer details including address based on the name | "Where is TechNova located?" |
| create_customer: Creates a customer record by providing the customer's name, city, state and country | "Create a customer for Presalesly AI located in Atlanta, Georgia, United States" |
| edit_customer: Edits a customer record given the customer ID and new details | "Update the city for GreenEdge Innovations to Palo Alto" |

### Opportunities
In the Opportunities section, you can view all the opportunities in CRM. Available tools include:

| Tool	| Example Prompts |
| ------- | ----------------- |
| get_opportunity_by_name: Returns opportunity details based on the opportunity name | "What is the value and stage of the Cloud Migration Project opportunity?" |
| create_opportunity: Creates an opportunity record by specifying the opportunity name, customer ID and amount | "Create an opportunity called HCM Implementation for Skyline Dynamics for 120000" |
| close_opportunity: Closes an opportunity given the opportunity name and stage | "Close the Cybersecurity Upgrade opportunity" |
| edit_opportunity: Edits an opportunity record given the opportunity ID and new details | "Update the CRM Expansion opportunity to 85K" |
| delete_opportunity: Deletes an opportunity record given the opportunity ID | "Delete the Network Security Audit opportunity" |

### Events
The Events section displays all events for a selected date (default is today). Here are the tools available for managing events:

| Tool	| Example Prompts |
| ------- | ----------------- |
| get_events_by_date: Returns all events for a specific date | "What meetings do I have today?" |
| create_event: Creates a new event based on event name, date, start and end time | "Create an hour-long appointment for the first available free slot after 9am today titled RFP response review" |

## Tech Stack
The Core is developed using Python and uses Cohere's models and API. The Web App is developed using Python and FastAPI as the backend and Vue (written in TypeScript) as the frontend. It is hosted on [Render](https://render.com/) at [agentiq.onrender.com](https://agentiq.onrender.com/) where each commit to github triggers a deploy.