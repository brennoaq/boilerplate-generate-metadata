import json

with open('boilerplate.json') as f:
    data = json.load(f)

with open('boilerplate2.json') as f:
    data2 = json.load(f)
    
    
for i in range(20):
  
  if i <= 10: 
    with open(str(i)+'.json', 'w') as f:
        json.dump(data, f, indent=2)
        print("New json file is created from boilerplate.json file - number:"+str(i))
  elif i <= 20: 
    with open(str(i)+'.json', 'w') as f:
        json.dump(data2, f, indent=2)
        print("New json file is created from boilerplate2.json file - number:"+str(i))