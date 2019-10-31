import requests

r = requests.get('http://checkip.amazonaws.com')
print("#" * 33 )
print("\n")
print("Your ip external is: {0}".format(r.text))
print("#" * 33)
