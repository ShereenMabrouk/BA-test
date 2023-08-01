# Shereen Mabrouk 
'''
A text-based (non-GUI) technical support ticketing application,
where issue types are organized in categories and defined outside of the program in an external file
'''
import os

# Function to read issue categories and types from the external file

def read_issue_categories(filename):
    categories = {}
    with open(filename, "r") as file:
        current_category = None
        for line in file:
            line = line.strip()
            if line.startswith("# Category:"):
                current_category = line.split(":")[1].strip()
                categories[current_category] = []
            elif line and current_category:
                categories[current_category].append(line)
    return categories

# Function to create a new ticket
def create_ticket(categories):
    print("Available Categories:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    category_index = int(input("Enter the category number: ")) - 1
    selected_category = list(categories.keys())[category_index]

    print(f"Available Issue Types for {selected_category}:")
    issue_types = categories[selected_category]
    for index, issue_type in enumerate(issue_types, start=1):
        print(f"{index}. {issue_type}")

    issue_type_index = int(input("Enter the issue type number: ")) - 1
    selected_issue_type = issue_types[issue_type_index]

    issue_description = input("Enter the issue description: ")
    ticket = {
        "category": selected_category,
        "issue_type": selected_issue_type,
        "description": issue_description
    }
    return ticket

# Function to display all tickets
def display_tickets(tickets):
    if not tickets:
        print("No tickets created yet.")
    else:
        print("All Tickets:")
        for index, ticket in enumerate(tickets, start=1):
            print(f"{index}. Category: {ticket['category']}, Type: {ticket['issue_type']}, Description: {ticket['description']}")
        print()

def main():
    filename = "issue_categories.txt"

    # Check if the external file exists
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return

    # Read issue categories and types from the external file
    categories = read_issue_categories(filename)

    tickets = []

    while True:
        print("Options:")
        print("1. Create a new ticket")
        print("2. Display all tickets")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            ticket = create_ticket(categories)
            tickets.append(ticket)
            print("Ticket created successfully.")
        elif choice == 2:
            display_tickets(tickets)
        elif choice == 3:
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
