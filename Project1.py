# you_may_know.py

users = {
    "Rupak": ["Amit", "Soham", "Riya"],
    "Amit": ["Rupak", "Soham"],
    "Soham": ["Rupak", "Amit", "Riya"],
    "Riya": ["Rupak", "Soham"],
    "Tablu":["Amit"],
    "Shreya":["Rupak"]
}

def recommend(user):
    friends = users[user]
    suggestions = []

    for friend in friends:
        for mutual in users[friend]:
            if mutual != user and mutual not in friends:
                suggestions.append(mutual)

    return list(set(suggestions))

name = input("Enter your name: ")
print("People you may know:", recommend(name))