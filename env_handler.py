# I know this is dirty work but this will be changed if something else found
import json
f = open('env.json')
data = json.load(f)
f.close()
a = open(".env", "w")
for i in data:
    a.write(f"{i.get('name')}={i.get('value')}\n")
a.close()
