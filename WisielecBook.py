import random
def hangman():
    words=["car","house","city","bridge","football","player","president"]
    word=words[random.randint(0,6)]
    wrong=0
    stages=["",
            "_____    ",
            "|        ",
            "|    |   ",
            "|    0   ",
            "|   /|\  ",
            "|   / \  ",
            "|_       "]
    rletters= list(word)
    board="_"*len(word)
    win = False
    print("Gra w wisielca")
    while wrong<=len(stages)-1:
        print("\n")
        msg="Odgadnij litere: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board=board[:cind]+char+board[cind+1:]
            rletters[cind] = "$"
        else:
            wrong+=1
        print((" ".join(board)))
        e = wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("Wygrales!")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("Przegrales! Miales odgadnac: {}.".format(word))
hangman()

        
