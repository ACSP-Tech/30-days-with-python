# Project: Number Guessing Game

In your IDE, create a guessing game like the one seen in the previous example. However, the range to guess is from 1 to 10. Of course, it would be a tedious game if we had to guess a number from 1 to 10 without any hints.
In the while loop, include some conditional statements that will provide clues to the user.
If the guess number is less than the actual number, the program should print:
“Your guess is smaller than the actual number.”

If the guess number is greater than the actual number, the program should print:
“Your guess is greater than the actual number.”

Also notify the user how many chances he or she has left. We will also only give them 3 chances to guess it correctly. If they do guess it correctly, the program will print:
“You guessed it correctly!”

If not, kindly tell the user his or her chances have all been used up and what the actual number was.
Here is the code for you to start:
```python
import random

num = random.randint(1, 10)
guess = int(raw_input('Guess a number from 1 to 10'))
chances = 2     # Chances is 2 since the first guess was used in the input above

while guess != num and chances:
    # TODO: finish code here
```

_Good luck!_

Source: IBM
