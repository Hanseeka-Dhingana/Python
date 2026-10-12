import json 


with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)


clients = data["clients"]
print(f"Total Clients: , {len(clients)}\n")

for client in clients:
    print(client["name"])
    print(f"Industry :, {client["industry"]}\n")
    print(f"  Year end : {client['year_end']}")
    print(f"  Revenue  : PKR {client['revenue']:,}")
    print(f"  Team     : {', '.join(client['team'])}")
    print()



# Find clients with a 30 June year end
june_clients = [c["name"] for c in clients if "30 June" in c["year_end"]]
print("June year-end clients:", june_clients)
