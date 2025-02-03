import re


def clean_emails(email_str):
    # Регулярное выражение для поиска электронных адресов
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    matches = re.findall(pattern, email_str)
    return ", ".join(matches)