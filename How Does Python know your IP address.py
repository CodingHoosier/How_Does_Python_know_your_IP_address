# https://youtube.com/shorts/bH5njoc2iS0
# How Does Python Know Your IP Address?
import urllib.request, json
# This site will give us our public IP
# It's in JSON format.
url = "https://api.ipify.org?format=json"
response = urllib.request.urlopen(url)
# Extract it from the data stream
data = json.loads(response.read().decode())
print("Public IP Address:", data["ip"])
