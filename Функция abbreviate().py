import re
def abbreviate(phrase: str) -> str:
    abr = ''.join(re.findall(r'\b\w|\B[A-Z]', phrase))
    return abr.upper()


print(abbreviate('gaveOver GameStarted happyEnd happyend'))