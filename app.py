import json

with open('boilerplate2.json') as f:
    data = json.load(f)

for i in range(888):
    # Modifique a chave "name" para incluir o número da iteração atual
    data["name"] = f"name example #{i+1}"

    with open(str(i), 'w') as f:
        json.dump(data, f, indent=2)

    print("New json file is created from boilerplate2.json file - number:"+str(i))