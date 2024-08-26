import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        # Regular expression to match valid email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        
        # Debug: Print the original and cleaned strings
        print("Original string:", self.email_string)
        
        # Replace commas and multiple spaces with a single space
        cleaned_string = re.sub(r'[,\s]+', ' ', self.email_string).strip()
        
        # Debug: Print the cleaned string
        print("Cleaned string:", cleaned_string)
        
        # Find all email addresses in the cleaned string
        found_emails = re.findall(email_pattern, cleaned_string)
        
        # Debug: Print found emails before removing duplicates
        print("Found emails:", found_emails)
        
        # Remove duplicates and return the list of emails
        return list(set(found_emails))

# Example usage:
parser = EmailAddressParser("alexa@amazon.com,john.doe@example.com,talk@talk.com,test@school.com")
print(parser.parse())  # Output should include all valid emails, without duplicates
