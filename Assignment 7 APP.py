import re

# Assignment 7: Find email patterns using regex

# Sample text containing emails
text = """
Contact amit@gmail.com
or rahul@yahoo.com
You can also reach sneha123@outlook.com
"""

# Define regex pattern for email addresses
pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

# Find all email addresses in the text
emails = re.findall(pattern, text)

# Display results
print("Extracted Email Addresses:")
for email in emails:
    print(email)
