import random

def check_win(player, computer):
    if player == computer:
        return "Draw"
    elif player == 'rocks' and computer in ['papers', 'scissors']:
        return "player wins"
    elif player == 'papers' and computer in ['rocks', 'scissors']:
        return "player wins"
    elif player == 'scissors' and computer in ['rocks', 'papers']:
        return "player wins"
    else:
        return "computer wins"

options = ['rocks', 'papers', 'scissors']
scores = {'player': 0, 'computer': 0}

def play_game():
    global scores

    print("\nPlayer".ljust(10), ":", scores['player'])
    print("Computer".ljust(10), ":", scores['computer'])

    player = input("Player -----").lower()
    computer = random.choice(options)

    print("Computer ---" + computer)

    result = check_win(player, computer)
    print(result)

    if result == "player wins":
        scores['player'] += 1
    elif result == "computer wins":
        scores['computer'] += 1

    if scores['player'] == 3 or scores['computer'] == 3:
        print("\nFirst to three wins")
        scores = {'player': 0, 'computer': 0}

def main():
    while True:
        try:
            play_game()
        except (EOFError, KeyboardInterrupt):
            print("\nFinish")
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()