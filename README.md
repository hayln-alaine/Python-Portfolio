# Python-Portfolio
Choose Your Own Adventure - Save the Baby Dragon!
1. My Choose Your Own Adventure game is a fantastical adventure as you try to reunite a baby dragon with its family. Not only are you following along in a story and choosing between two choices along the way to continue the story, but you are also gaining or losing health points and gold coins, depending on the scenario.
2. Most of the design is tied in created functions for different parts of the adventure. each function leads to the next, depending on what is chosen. within each function, the health and gold coins variables are carried through, allowing the player to watch their score increase or decrease.
I started with first writing out the outline, or path, that I wanted to follow for the story. Than I sectioned off different parts of the story as functions. while this meant a lot of writing for the functions, the code to run the game, other than defined variables in the beginning, was a total of two lines. I let the functions do the heavy lifting and connected the story together through the functions.
It took a minute to figure out how to pull the points through the different functions and how to set those up. They work, mostly. I will explain more later on this.
The Beginning Function:
<img width="1174" alt="Screenshot 2023-06-09 at 10 05 36 AM" src="https://github.com/hayln-alaine/Python-Portfolio/assets/116326505/aba79f7f-9290-4d3f-9eaf-6063269611d2">

 
 The Forest Function to Town Function:
 <img width="1186" alt="Screenshot 2023-06-09 at 10 07 59 AM" src="https://github.com/hayln-alaine/Python-Portfolio/assets/116326505/e808804d-643c-4c0a-a2b9-0b5b1c89e409">

 The Cave Function (which leads to the end of the game):
 <img width="1184" alt="Screenshot 2023-06-09 at 10 08 52 AM" src="https://github.com/hayln-alaine/Python-Portfolio/assets/116326505/bfed1616-f168-4280-a10d-e8665d7a8e31">

3. I learned that I am quite verbose and really love creating stories. One of the things that I really like about the game is that it moves along with some fun and exciting parts.
I also liked that I was able to create a points component, to give the game more punch and learned that starting a project like this is really challenging, to switch from idea to coding.

as far as shortcomings, I would love to learn the time feature, to pull out the text line by line, instead of all at once for each section of the functions. I also realized, late into testing, that if you choose an option that bumps you through the else part of the function, the points still change and you can get negative points. My goal was to not make a game where the player died every round of choices, but in that, I don’t really have something to catch when numbers are going negative (and you have to take a certain path to get close to negative and then go through the last else statement). That will need to be course corrected, when I learn how!
with a python only based game, I am sure there is more I can change and tweak. I was also thinking ahead in how I could make this more animated, with ways to modify the text, timing, etc. I was also thinking about what it would look like for different kinds of players to move through the story or even players taking turns and then comparing their scores.
