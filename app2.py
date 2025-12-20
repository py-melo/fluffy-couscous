servers = {
        "web01": 45,
        "db01": 82, 
        "cache01": 30
        }


print("Server Health Checker")

print("Server CPU Usage:")

for server, cpu in servers.items():
    print(f"{server}: {cpu}%")
