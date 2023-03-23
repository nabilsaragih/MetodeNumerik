import re

def parse(persamaan):
# Replace ^ with **
    persamaan = re.sub(r'\^', r'**', persamaan)

    # Add * between number and variable
    persamaan = re.sub(r'(\d+)([a-zA-Z])', r'\1*\2', persamaan)

    return str(persamaan)
