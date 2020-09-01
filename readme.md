Simple number guessing game :- 

Question:
Computer will choose a random number between a range (say 1 to 100) and the user initially has 100 points. Computer will give clues to the user to guess the number (such as the number is factors of that number, multiple of some numbers etc.) Each time the user guesses the wrong answer, his points will be reduced.
After each guess a different clue will be shown to the user until his points becomes zero. And after guessing the number correctly, final score will be shown.

Method
1. Computer will generate a random number [1-100].
2. Computer will randomly select a clue related to the number and display that clue to the user.
3. User will have to guess the number. If he guesses it wrong, then 2nd step is repeated again.
4. This continues untill the user's points are reduced to 0 or he guesses it correctly, after which the game ends.

@random library has been used to generate random numbers, select random clues and generate them randomly also.