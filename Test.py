import requests

TOKEN = "7926754081:AAHjWlGMT0X7Rba2UMq0MxVktXILCPCpO2k"
CHAT_ID = "518385491"
TEXT = "سلام! این یک پیام تست از ربات رباعی‌من است."

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {"chat_id": CHAT_ID, "text": TEXT}

response = requests.post(url, data=payload)
print(response.text)
