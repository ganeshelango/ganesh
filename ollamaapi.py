import requests
OLLAMA_API_URL = "http://localhost:11434/api/generate"
suggesttag = {
    "incoming": [
        "Salary", "Bonus", "Freelance Income", "Business Income", "Interest Income",
        "Dividends", "Tax Refund", "Cash Deposit", "Gift Received", "Loan Received", "Reimbursement"
    ],
    "outgoing": {
        "Food": ["Groceries", "Restaurants", "Food", "Snacks & Beverages", "Food Delivery"],
        "Transportation": ["Fuel", "Toll Charges", "Car Maintenance", "Rideshare (Ola, Uber)", "Public Transport"],
        "Shopping": ["Clothing", "Footwear", "Accessories", "Electronics", "Online Shopping"],
        "Housing & Utilities": ["Rent", "Electricity", "Water Bill", "Internet", "Gas Bill"],
        "Health & Medical": ["Doctor Visits", "Medicines", "Health Insurance", "Lab Tests"],
        "Insurance": ["Life Insurance", "Vehicle Insurance", "Health Insurance"],
        "Personal Care": ["Salon / Spa", "Cosmetics", "Haircuts", "Wellness / Grooming"],
        "Entertainment": ["Subscriptions", "Movies", "Events", "Mobile Recharge / DTH"],
        "Education": ["Tuition Fees", "School Supplies", "Online Learning"],
        "Family & Kids": ["Childcare", "Toys & Games", "Baby Products"],
        "Gifts & Donations": ["Gifts", "Charity", "Religious Offerings"],
        "Debt & Loan Payments": ["Credit Card Payment", "Personal Loan EMI", "Vehicle Loan"],
        "Investment": ["Mutual Funds", "Stocks", "SIP Payments"]
    }
}

import json

payload = {
    "model": "mistral",
    "prompt": f"""
Given the below data:

Suggested_Tags:
{json.dumps(suggesttag, indent=2)}

Personalized_Tags: ["Food", "Transportation", "Shopping", "Housing & Utilities", "Healthcare", "Insurance", "Personal Care", "Entertainment", "Education","investment"]

Transaction_Description: "Etmoney"

Return JSON in this format:
{{ "personal_tag_sugg": "", "suggest_tag_sugg": "" }}

Rules:
- Choose ONE best match from Personalized_Tags(only on Personalized_Tags and it should be in Personalized_Tags).
- Choose ONE best match from Suggested_Tags (including subcategories).
- No extra text. Only valid JSON.
""",
    "stream": False
}

response = requests.post(OLLAMA_API_URL, json=payload)
if response.status_code == 200:
    data = response.json()
    print("Response from model:")
    print(data.get("response"))
else:
    print("Error:", response.status_code)
    print(response.text)
