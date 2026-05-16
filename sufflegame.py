import random
import os
import time

# Step 1: Take names from user
students = []

for i in range(4):
    name = input(f"Enter name of student {i+1}: ")
    students.append(name)

# Step 2: Shuffling animation
print("\nShuffling", end="")
for _ in range(5):
    print(".", end="", flush=True)
    time.sleep(0.5)

# Clear screen (optional)
os.system("cls" if os.name == "nt" else "clear")

# Step 3: Shuffle (hidden from user)
random.shuffle(students)

# Step 4: Pick a random winner
winner = random.choice(students)

# Step 5: Show only winner
print("🎯 Picking a student...")
time.sleep(2)
print(f"\n🎉 Selected Student: {winner}")