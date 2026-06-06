import requests

url = "https://vinid.vn/hehehehihi"

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkZha2UgVXNlciIsImlhdCI6MTcxNzU0NTYwMH0.fake_signature_1234567890",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print("Response:")
print(response.text)

TEST_GITHUB_INDEX_9F7A1C3D8E
