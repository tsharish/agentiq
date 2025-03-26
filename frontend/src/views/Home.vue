<script setup lang="ts">
</script>

<template>
    <div class="card">
        <Accordion :value="['0']" multiple>
            <AccordionPanel value="0">
                <AccordionHeader>Welcome to Agentiq CRM!</AccordionHeader>
                <AccordionContent>
                    <p>
                        Agentiq CRM demonstrates the powerful agentic AI capabilities of <strong>Agentiq</strong>.
                        Agentiq is an intelligent assistant that can be accessed using the chat button located at the
                        bottom right corner of the screen. <br><br>
                        Below, you'll find an overview of the core features and tools available within Agentiq CRM. Each
                        tool is available across the entire system, making it easy to interact with the data and
                        automate tasks.
                    </p>
                </AccordionContent>
            </AccordionPanel>
            <AccordionPanel value="1">
                <AccordionHeader>Customers</AccordionHeader>
                <AccordionContent>
                    <p class="mb-3">The <strong>Customers</strong> section displays all customer records. Here are the
                        tools available for managing customer information:</p>
                    <table>
                        <thead>
                            <tr>
                                <th>Tool</th>
                                <th>Example Prompts</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <i>get_customer_by_name:</i> Returns customer details including address
                                    based on the name
                                </td>
                                <td>
                                    <i>"Where is TechNova located?"</i>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <i>create_customer:</i> Creates a customer record by providing the customer's
                                    name, city, state and country
                                </td>
                                <td>
                                    <i>"Create a customer for Presalesly AI located in Atlanta, Georgia, United
                                        States"</i>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <i>edit_customer:</i> Edits a customer record given the customer ID and new
                                    details
                                </td>
                                <td>
                                    <i>"Update the city for GreenEdge Innovations to Palo Alto"</i>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </AccordionContent>
            </AccordionPanel>
            <AccordionPanel value="2">
                <AccordionHeader>Opportunities</AccordionHeader>
                <AccordionContent>
                    <p class="mb-3">In the <strong>Opportunities</strong> section, you can view all the opportunities in
                        CRM. Available tools include:</p>
                    <table>
                        <thead>
                            <tr>
                                <th>Tool</th>
                                <th>Example Prompts</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <i>get_opportunity_by_name:</i> Returns opportunity details based on the opportunity
                                    name
                                </td>
                                <td>
                                    <i>"What is the value and stage of the Cloud Migration Project opportunity?"</i>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <i>create_opportunity:</i> Creates an opportunity record by specifying the
                                    opportunity name, customer ID and amount
                                </td>
                                <td>
                                    <i>"Create an opportunity called HCM Implementation for Skyline Dynamics for
                                        120000"</i>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <i>close_opportunity:</i> Closes an opportunity given the opportunity name and stage
                                </td>
                                <td>
                                    <i>"Close the Cybersecurity Upgrade opportunity"</i>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <i>edit_opportunity:</i> Edits an opportunity record given the opportunity ID and
                                    new details
                                </td>
                                <td>
                                    <i>"Update the CRM Expansion opportunity to 85K"</i>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <i>delete_opportunity:</i> Deletes an opportunity record given the opportunity ID
                                </td>
                                <td>
                                    <i>"Delete the Network Security Audit opportunity"</i>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </AccordionContent>
            </AccordionPanel>
            <AccordionPanel value="3">
                <AccordionHeader>Events</AccordionHeader>
                <AccordionContent>
                    <p class="mb-3">The <strong>Events</strong> section displays all events for a selected date (default
                        is today). Here are the tools available for managing events:</p>
                    <table>
                        <thead>
                            <tr>
                                <th>Tool</th>
                                <th>Example Prompts</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <i>get_events_by_date:</i> Returns all events for a specific date
                                </td>
                                <td>
                                    <i>"What meetings do I have today?"</i>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <i>create_event:</i> Creates a new event based on event name, date, start and end
                                    time
                                </td>
                                <td>
                                    <i>"Create an hour-long appointment for the first available free slot after 9am
                                        today titled RFP response review"</i>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </AccordionContent>
            </AccordionPanel>
        </Accordion>
    </div>
</template>

<style scoped>
table {
    border-collapse: collapse;
    width: 100%;
}

td,
th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}
</style>
