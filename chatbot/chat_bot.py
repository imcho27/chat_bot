print("Welcome to the UK Visit Visa Fee Calculator!")
print("How long do you plan to stay in the UK, or what is your visa purpose?")
print("Options: '6 months', '2 years', '5 years', '10 years', 'medical', 'academic', 'priority' (for faster processing), or 'super priority'.")
print("Type 'quit' to exit.")

while True:
    # Get user input
    user_input = input("\nEnter your choice: ").lower().strip()

    # Check if user wants to quit
    if user_input == "quit":
        print("Thank you for using the UK Visit Visa Fee Calculator. Goodbye!")
        break

    # Define visa fees
    fees = {
        "6 months": "Standard Visitor Visa (up to 6 months): £127",
        "2 years": "Standard Visitor Visa (2 years): £475",
        "5 years": "Standard Visitor Visa (5 years): £848",
        "10 years": "Standard Visitor Visa (10 years): £1,059",
        "medical": "Medical Visitor Visa (up to 11 months): £200",
        "academic": "Academic Visitor Visa (12 months): £200",
        "priority": "Priority Service (5 working days): £500 (additional fee)",
        "super priority": "Super Priority Service (next working day): £1,000 (additional fee)"
    }

    # Check user input and display fee
    if user_input in fees:
        print(f"\nYour visa fee: {fees[user_input]}")
        print("Note: Additional costs like biometric fees (£19.20) or ETA (£16 for some nationalities) may apply.")
        print("Visit www.gov.uk for full details and to apply.")
    else:
        print("\nSorry, that's not a valid option. Please try again with '6 months', '2 years', '5 years', '10 years', 'medical', 'academic', 'priority', 'super priority', or 'quit' to exit.")