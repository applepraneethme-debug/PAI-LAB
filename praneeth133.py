import random

player_hp = 100
enemy_hp = 100

def player_turn():
    global enemy_hp
    print("\n1. Attack\n2. Strong Attack\n3. Heal")
    choice = input("Choose action: ")

    if choice == "1":
        damage = random.randint(10, 20)
        enemy_hp -= damage
        print(f"You dealt {damage} damage!")
    elif choice == "2":
        damage = random.randint(15, 30)
        enemy_hp -= damage
        print(f"🔥 Strong hit! {damage} damage!")
    elif choice == "3":
        heal = random.randint(10, 20)
        print(f"💚 You healed {heal} HP!")
        return heal
    return 0

def enemy_turn():
    global player_hp
    action = random.choice(["attack", "strong"])

    if action == "attack":
        damage = random.randint(8, 18)
    else:
        damage = random.randint(12, 25)

    player_hp -= damage
    print(f"💻 Enemy deals {damage} damage!")

print("⚔️ Battle Game: You vs AI")

while player_hp > 0 and enemy_hp > 0:
    print(f"\n❤️ Your HP: {player_hp} | 💀 Enemy HP: {enemy_hp}")

    player_hp += player_turn()
    enemy_turn()

if player_hp > 0:
    print("🎉 You Win!")
else:
    print("💀 You Lose!")
