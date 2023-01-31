import urllib.request, urllib.parse, urllib.error
import ssl
import json

# not needed for HTTP, but must be included for all HTTPS sites
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter URL: ")
    if len(address) < 1:
        break

    # website into string
    print("Retrieving", address)
    website = urllib.request.urlopen(address, context=ctx)
    data = website.read().decode()
    print("Retrieved", len(data), "characters")

    # string into dictionary
    try:
        js = json.loads(data)
    except:
        js = None

    print("Count:", len(js["comments"]))

    # views json structure
    #   print(json.dumps(js, indent=4))  #

    # TEST  http://py4e-data.dr-chuck.net/comments_42.json
    sum = 0

    for item in js["comments"]:
        x = int(item["count"])
        sum = sum + x

    print(sum)
