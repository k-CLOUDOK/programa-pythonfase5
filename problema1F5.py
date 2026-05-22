# Matrix with customer data
clients = [
    ["C001", 250, 10],
    ["C002", 45, 2],
    ["C003", 120, 5],
    ["C004", 200, 9],
    ["C005", 50, 6]
]

# Function to classify commitment
def classify_engagement(duration, clicks):

    if duration > 180 and clicks > 8:
        return "High"

    elif duration < 60 or clicks < 3:
        return "Low"

    else:
        return "Medium"


# Show report
print("CLASSIFICATION REPORT")
print("----------------------------")

for client in clients:

    client_id = client[0]
    duration = client[1]
    clicks = client[2]

    classification = classify_engagement(
        duration,
        clicks
    )

    print("Customer:", client_id)
    print("Classification:", classification)
    print("----------------------------")
