Hello and welcome to my final project!

My name is Surya Malik and I decided to make war in python! This program had many nuances however I had a great time
making it. I used no pip-installable modules in this program, and it properly runs in the shell. I used random selection
and other than that, had nothing else I needed to import. I separated the majority of my code into respective functions
which I will begin to go over shortly. Overall my code was just about 255 lines of code with about 190 of that being
functions. Now to break down my code step by step:

1. Start_loop: This function is a while loop that checks user input and reacts based on what was entered. The whole
function is in a while true loop and begins by asking the user if they are ready to play war with an input statement and
capitalizes the response. If the result is Y, the function returns false which stops the loop and allows the rest of the
code to be run. If the result is N, the function prints a specific statement asking the user to rethink their decision.
If the result is anything other than Y or N, regardless of capitalization, the function prints an invalid input
statement and continue to iterate until Y is entered.

2. Create_deck: This function creates the card deck by using nested for loops that iterate through each list. For each
term in the suits list, it will match with each term in the value list, which ultimately returns a deck of tuples.

3. Shuffle_deck_loop: This code uses the same input validation as start_loop however with different messages. In this
instance, if the user enters n or N, the loop will stop and the rest of the code is run, converse to start_loop which
runs the rest of the code if Y is entered. Instead, everytime the user enters Y, the deck is shuffled.

4. Start_game_loop: Uses the same exact input validation from start_loop, just with different print statements,
allowing the game to begin.

5. Face_card_conversion: In the function, face cards appear as their face card value (jack, queen, king, ace) and not their
numeric value (11, 12, 13, 14). This function uses variables defined in the outer scope and assigns the numeric value
of the face card to the card values. Jack corresponds to 11, queen to 12, king to 13 and ace to 14.

6. User_wins: This is the function that runs if the user wins a round. All it does is print a specific statement and
append the user card and the computer card played to the user deck.

7. Computer_wins: This is the function is the same as user_wins, just for the computer. So it appends to the computer deck
instead of the user.

8. Ready_loop: Uses the same exact input validation as start_loop, just with different print statements. This allows for
the user to decide if they are ready for the war to be played.

9. War: This function took me days to get working. I could go into significant detail about what everything does but
I'll save you the reading and sum things up. The code is in a while loop stating that iterates
as long as the user and the computer play the same card. This ensures that multiple wars can happen back to back. The
function then begins to check the bajillion conditions that must be checked for this to function properly. A normal war
is played with 3 cards face down and 1 card face up used for comparison. This function ensures that if a special case
happens where the user or the computer doesn't have enough for a full war, the code still runs and iterates for however
many cards can be played, with different messages for each condition. All of these conditions are checked depending on
the length of the user or computer deck. For war purposes, I made new variables representing the respective user and
computer's  face up war card and the list of cards that are played face down. This is done by iterating through a
certain range, dependent on the conditions I just talked about, popping the first value of the respective computer
and user decks. I unpack the cards to isolate the values (excluding suits) for comparison. As long as the decks are
under 52, comparison can occur. Before a war is played, the ready_loop function is called. The user and computer cards
are printed (the ones that will be used for comparison (FACE UP CARDS)) and then are compared using greater than and
less than statements. If the user wins, the user_wins function is called and every card in both the user war list and
the computer war list are appended to the user deck. Conversely, if the computer wins, the computer_wins function is
called and the war lists are appended to the computer deck. If another war occurs, the code will continue to iterate
because of the while loop. At the end of every round that results in a war, the war lists are cleared to prevent extra
cards being added to the deck. That was a mouthful.

10. Create_user_computer_deck: This creates the user and the computer deck, by appending even numbered indexes in the
main deck to the user, and odd numbered indexes to the computer using a for loop iterating through the whole deck.

That's all my functions, now to everything under if name equals main.

I begin by importing random, initializing my face card variables, and printing the rules of the game, which I will
attach at the bottom of this text file for reference. I create the deck using the create_deck function. I then randomly
shuffle the deck and print a message. I call the shuffle_deck_loop and then initialize the user_deck and computer_deck
variables. I then call the create_user_computer_deck function and call the start_game_loop. I create a user_deck_length
and computer_deck_length variable in the outer scope, taking the lengths of both decks. I then initialize the
user_war_list and the computer_war_list. I print the current amount of cards each player has and then enter my main game
loop. I have some conditionals in here so I set up a counter_loop variable equal to True and a counter variable equal to
1. This counter variable keeps track of how many rounds are played. The whole game is in a while loop that iterates
while the computer or user deck length is less than 52 , nested inside the while counter_loop. This while counter loop
allows for the game to terminate at anytime. I set up the user_card variable the computer_card variable and print both.
These are popped from the front of the respective decks and used for comparison. I then unpack the tuple to exclude the
suits for comparison and call the face_card_conversion function to convert necessary face cards. If the user value is
greater than the computer, the user_wins function is called, if the user value is less than the computer value, the
computer_wins function is called, and if the values are equal, the war function is called, accepting both values as
arguments. The game will then run in the functions and produce the desired result. After the fact the length is checked
to see if the game is playable, and then prints the lengths of the user and computer deck again. I then have input
validation asking if the user wants to continue the game which is where the while counter_loop comes in. This input
validation is in a while loop,stating that as long as a variable, invalid_input (which I assign to be 0 before the loop
starts) is less than 1, the loop iterates and asks the user the question. If they respond with Y, the game continues,
invalid_input is set to 2 which breaks that while loop and 1 is added to the counter. If the counter reaches 1000
rounds, the game terminates and counter_loop is set to false, stopping everything. If they respond with N, then the
invalid_input loop is broken, counter_loop is set to false and then broken, ending the code. If they respond with
anything other than Y or N, an invalid input statement is printed and the question is asked again. Once the user deck or
the computer deck hits 52, the main while loop stops and the lengths are checked again. If the computer has 52, they win
and if the user has 52, they win. If counter_loop was set to false, meaning the user chose to terminate the game, then a
special print statement is presented.

I tried to slim this down the best I could but there was a lot I needed to discuss. Hope you enjoy!

Rules: The rules of the game are as followed: The deck is divided evenly between each player. Each player receives
exactly 26 cards, dealt one at a time, face down. The game begins with each player drawing their top card and playing
it, face up. Whoever has the higher value takes both cards and puts them face down at the bottom of the stack. This
repeats until one player has all 52 cards that were dealt at the start. The game gets its name when each player draws a
card that is the same rank. This is called a war. If this happens, each player draws another 3 cards, one by one, and
places them face down. Finally, a fourth card is played, face up and whoever has the higher value takes all 10 cards
from the round. If a player does not have enough cards to do a full war, then the last card they have will be played
face up to be used in the war. Good luck and have fun!