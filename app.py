import json

with open('boilerplate.json') as f:
    data = json.load(f)
    
    
for i in range(10):
    with open(str(i)+'.json', 'w') as f:
        json.dump(data, f, indent=2)
        print("New json file is created from boilerplate2.json file - number:"+str(i))