import re

registration = input("Enter vehicle registration (example MH12AB1234): ").strip().upper()
pattern = r"[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}"

if re.fullmatch(pattern, registration):
    print("Registration format is valid")
else:
    print("Registration format is invalid")
