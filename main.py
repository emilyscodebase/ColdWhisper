# ColdWhisper prototype

user_input = input("How are you feeling while coding? ")

if "frustrated" in user_input.lower():
    print("Take a short break. You're doing well. Try again in a few minutes 💪")
elif "stuck" in user_input.lower():
    print("Try breaking the problem into smaller parts or use an AI tool to guide you.")
else:
    print("Keep going! You're making progress 🚀")
