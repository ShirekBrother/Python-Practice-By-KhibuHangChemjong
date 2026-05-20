import random

user_choice=input("Enter your choice ('Scissor','Paper','Rock') : ")

computer_choice=['Scissor', 'Paper', 'Rock']

let_computer_choose=random.choice(computer_choice)

print(f"Computer has chossen {let_computer_choose}.")

if user_choice=="Scissor" and let_computer_choose=="Scissor":
    print("🤝 It's a Draw!")
elif user_choice=="Scissor" and let_computer_choose=="Paper":
    print("🎉 Congratulations! You Win! 🏆")    
elif user_choice=="Scissor" and let_computer_choose=="Rock":
    print("😢 Sorry, You Lose! 💔")
elif user_choice=="Paper" and let_computer_choose=="Scissor":
    print("😢 Sorry, You Lose! 💔")
elif user_choice=="Paper" and let_computer_choose=="Paper":
    print("🤝 It's a Draw!")
elif user_choice=="Paper" and let_computer_choose=="Rock":
    print("🎉 Congratulations! You Win! 🏆")    
elif user_choice=="Rock" and let_computer_choose=="Scissor":
    print("🎉 Congratulations! You Win! 🏆")    
elif user_choice=="Rock" and let_computer_choose=="Paper":
    print("😢 Sorry, You Lose! 💔")
elif user_choice=="Rock" and let_computer_choose=="Rock":
    print("🤝 It's a Draw!")


