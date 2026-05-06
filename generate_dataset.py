import pandas as pd
import random

phishing_templates = [
    "Verify your account immediately at {}",
    "Click here to reset your password {}",
    "Urgent: your bank account is locked {}",
    "Confirm your identity now {}",
    "You won a prize! Claim here {}",
    "Security alert: login attempt detected {}",
    "Update your billing info {}",
    "Your account will be suspended {}",
    "Act now to avoid account closure {}",
    "Unauthorized transaction detected {}"
]

safe_templates = [
    "Meeting scheduled at {}",
    "Lunch at {}?",
    "Project deadline is {}",
    "Please review the document",
    "Let's catch up {}",
    "Reminder: team meeting {}",
    "Invoice attached",
    "Happy birthday!",
    "Can we reschedule?",
    "Thanks for your help"
]

urls = [
    "http://secure-login.com",
    "http://verify-account.net",
    "http://update-info.org",
    "http://bank-alert.co",
    "http://login-security.com"
]

times = ["10 AM", "2 PM", "tomorrow", "next week", "Friday"]

data = []

# Generate 500 phishing
for _ in range(500):
    text = random.choice(phishing_templates).format(random.choice(urls))
    data.append([text, "phishing"])

# Generate 500 safe
for _ in range(500):
    template = random.choice(safe_templates)
    if "{}" in template:
        text = template.format(random.choice(times))
    else:
        text = template
    data.append([text, "safe"])

# Shuffle dataset
random.shuffle(data)

# Save to CSV
df = pd.DataFrame(data, columns=["text", "label"])
df.to_csv("emails.csv", index=False)

print("✅ 1000 email dataset generated as emails.csv")