import re

def check_query(query: str):
    
    pattern = r'^[a-zA-Z]+(?: [a-zA-Z]+)*$'

    if re.match(pattern, query):
        return True
    else:
        return False