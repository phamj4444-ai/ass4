import re
def hide_phone_numbers(text):
  pattern = r"\+84\d{9}|\b\d{10}\b"
  return re.sub(pattern, "[REDACTED]", text)
document = "Contact 0912345678 or +84987654321 for more details."
print(hide_phone_numbers(document))