#problem: p1 and p2 rock paper scissors, return who won


def rps(p1, p2):
    #your code here
    winner = {"scissors": "paper", "paper": "rock", "rock": "scissors"}
    if p1==p2:
        return 'Draw!'
    elif winner[p1]==p2:
        #the [] returns the term, not the key, so if p1 is rock, it gives paper, and if p2 equals paper when p1 is rock p2 loses
        return "Player 1 won!"
    elif winner[p2]==p1:
        return "Player 2 won!"