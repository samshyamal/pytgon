def game(first_user,second_user):
  print(f"\nfirst user chose {first_user}, second user chose {second_user}.\n")
  if first_user == second_user:
    print(f"Both players selected {first_user}. It's a tie!")

  elif first_user == "rock":
   if second_user == "scissors":
     print("Rock smashes scissors! first win!")
   else:
     print("Paper covers rock! second win.")

  elif first_user == "paper":
   if second_user == "rock":
     print("Paper covers rock! first win!")
   else:
     print("Scissors cuts paper! second win.")

  elif first_user == "scissors":
    if second_user == "paper":
        print("Scissors cuts paper! first win!")
    else:
        print("Rock smashes scissors! second win.")

first_user = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
second_user = input("Enter a choice (rock, paper, scissors): ")

game(first_user,second_user)
