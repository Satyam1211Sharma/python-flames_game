# python-flames_game
This is a fun little project based on the classic FLAMES game we used to play during school/college days. Just input two names and find out what kind of relationship they share based on a simple elimination algorithm.

 FLAMES Game - Relationship Predictor in Python

This is a fun little project based on the classic FLAMES game we used to play during school/college days. Just input two names and find out what kind of relationship they share based on a simple elimination algorithm.

🚀 Features

Accepts any two names as input

Removes common characters

Counts remaining characters

Predicts relationship using FLAMES logic

Simple and clean output

🎮 How to Play (Usage)

python flames_game.py

Then input two names when prompted:

Enter your name: Satyam
Enter your partner's name: Anjali

🔥 Relationship Status between satyam and anjali: Love

🔧 How It Works

Takes both names as input.

Converts them to lowercase and removes spaces.

Removes all common letters between both names.

Adds the remaining letters.

The total count of remaining letters is used to loop over the word FLAMES until one character remains.

Based on the last remaining character, relationship status is printed.


