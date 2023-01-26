import requests

def test(n):
    header = b"foo" + int.to_bytes(n, 1, "little")
    url = "http://localhost:5000"
    #url = "https://crates.io"
    try:
        headers = {"Authorization": header}
        r = requests.get(url, headers=headers)
        print("Header:", header, "Response:", r.status_code)
        return r.status_code == 200
    except ValueError as e:
        print("Header:", header, "Request error:", e)
        return False

invalid = []
for i in range(256):
    if not test(i):
        invalid.append(i)

print("invalid:", invalid)
