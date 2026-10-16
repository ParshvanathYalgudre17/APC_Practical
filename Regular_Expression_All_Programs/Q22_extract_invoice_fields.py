import re

text = input("Enter invoice text: ")

invoice_numbers = re.findall(r"\bInvoice\s*(?:No\.?|Number|#)?\s*[:\-]?\s*([A-Z0-9/-]+)", text, flags=re.IGNORECASE)
dates = re.findall(r"\b(?:0[1-9]|[12]\d|3[01])[-/](?:0[1-9]|1[0-2])[-/]\d{4}\b", text)
amounts = re.findall(r"(?:₹|Rs\.?|INR)\s*\d+(?:,\d{3})*(?:\.\d{2})?", text, flags=re.IGNORECASE)

print("Invoice numbers:", invoice_numbers)
print("Dates:", dates)
print("Monetary amounts:", amounts)
