import json
import http
# import requests

# url = "https://files.pushshift.io/reddit/comments/RC_2008-01.zst"
# response = requests.get(url)
# json_response = json.loads(response.text)

your_filename = "./data/RC_2008-01.txt"
with open(your_filename, "rb") as f:
    data = f.read()

# print(data)

my_json = data.decode('utf8')
my_json = my_json.split('\n')
posts = []

for i in range(0,len(my_json)):
    # print(i)
    try:
        post = json.loads(my_json[i])
        posts.append(post)
    except:
        print("Post " + str(i) + " failed to be added")

# print(posts)
sales = ["Agreement",
"Deal",
"Sale",
"Package",
"Dollars",
"Euro",
"Aid",
"security support",
"military support",
"Guarantee",
"Loan",
"Delivery",
"Transfer",
"Detterent",
"consignment",]
weapon = [
"Missile",
"rocket",  
"System",
"Arms",
"Munition",
"Weapon",
"Bomb",
"Warhead",
"Defense",
]
result = []
for p in posts:
    first = False
    second = False
    for s in sales:
        if s in p['body']:
            first = True
            break
    if not first:
        continue
    for w in weapon:
        if w in p['body']:
            second = True
            break
    if first and second:
        result.append(p)

for r in result:
    print(r['body'])
    print("----------------------------")

print(len(result))
