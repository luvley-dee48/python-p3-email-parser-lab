# your code goes here!


import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses
    
    def parse(self):
        # Split email addresses based on comma or space
        tokens = re.split(r'[,\s]+', self.email_addresses)
        
        # Use a set to collect unique email addresses
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
        unique_addresses = set()
        
        for token in tokens:
            if email_regex.match(token.strip()):
                unique_addresses.add(token.strip())
        
        # Sort the unique addresses alphabetically
        sorted_addresses = sorted(unique_addresses)
        
        return sorted_addresses