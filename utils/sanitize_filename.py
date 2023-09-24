import re

# Function to sanitize a string for use as a filename
def sanitize_filename(filename):
    # Remove any characters that are not letters, digits, hyphens, or underscores
    sanitized = re.sub(r'[^\w\-_]', '_', filename)
    return sanitized