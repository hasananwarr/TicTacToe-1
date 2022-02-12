# TicTacToe-1
1) Use and understand Git!
Ans) Yes, i have used and understood git and my whole code is available in github, i have also used its functions like push,pull,merge, rebase etc.
2) UML at least 3 good diagrams. "good" means you can pump it up artificially as written in DDD. You have 10 million $ from me! Please export the pics. I can not install all tools to view them!
Ans) https://github.com/hasananwarr/TicTacToe-1/blob/main/UML/TicTacToe_UML.png
3) DDD If your domain is too small, invent other domains around and document these domains (as if you have 10 Mio € from Edlich-Investment!) Develop a clear strategic design with mappings/relationships with 5-0 Domains. It would be nice if these domains are derived from an Event-Storming (but not mandatory). 
Ans) https://github.com/hasananwarr/TicTacToe-1/tree/main/DDD
4) Metrics at least two. Sonarcube would be great. Other non-trivial metrics are also fine.
Ans) https://github.com/hasananwarr/TicTacToe-1/tree/main/Sonarqube_Screenshot
5) Clean Code Development: A) at least 5 points you can show me with an explanation of why is this is clean code in your code and/or what has improved & B) >>10 points on your personal CCD cheat sheet. E.g. a PDF.
Ans) https://github.com/hasananwarr/TicTacToe-1/tree/main/Clean%20Code%20Development
6) Build Management with any Build System as Ant, Maven, Gradle, etc. (only Travis is perhaps not enough) Do e.g. generate Docs, call tests, etc. (it could be also disconnected from the project just to learn a build tool!)
Ans) https://github.com/hasananwarr/TicTacToe-1/tree/main/Gradle
In gradle build, i have learned it from youtube and each step is documented in photos, In this i have build a simple hello world function using gradle, then i created a test to validate exception error, so when i build it , it validates the code and generates the test report , which is also documented, whatever i have learned i have documented using pictures you can see
7) Integrate some nice Unit-Tests in your Code to be integrated into the Build
Ans) https://github.com/hasananwarr/TicTacToe-1/blob/main/test_.py
I tried to used pytest for testing with CI-CD GITLAB ACTIONS, but due to dependencies and different enviroment problem, i was unable to solve this problem , so i wrote both test_.py for pytest and i have also added function in my code which is named unit test , in which i have done unit testing, if you can unit_test(), you can see it works and i have attached the screenshot and here's is the link: 
8) Continuous Delivery: show me your pipeline using e.g. Jenkins, Travis-CI, Circle-CI, GitHub Action, GitLab CI, etc. E.g. you can also use Jenkins Pipelining or BlueOcean, etc. But at least insert more than 2 script calls as done in the lecture! (e.g. also call Ant or Gradle or something else).
Ans) https://github.com/hasananwarr/TicTacToe-1/actions ,
https://github.com/hasananwarr/TicTacToe-1/blob/main/.github/workflows/python-TicTactoe-app.yml
In CI-CD pipeline, i have used gitlab actions because it was so convinient because my code was already available in github , so it is better integrated, also i have used the concept of linting using flake8 which checks the syntax error in the code, yml code link is attached also , whenever i push something it starts its pipeline jobs
9) Use a good IDE and get fluent with it: e.g. IntelliJ. What are your favorite Key-Shortcuts?!
Ans) https://github.com/hasananwarr/TicTacToe-1/tree/main/IDE_Fav_Shortcuts
10) DSL Create a small DSL Demo example snippet in your code even if it does not contribute to your project (hence it can also be in another language).
Ans) https://github.com/hasananwarr/TicTacToe-1/tree/main/DSL
In DSL, i have created my own dsl file which is src1.dsl which will have file name in  which functions are written in python , also it can contains function name which i want to call, also input arguments are also going from dsl file, this dsl file will call python function and give argument which python will read and gives it's output, demo is given in screenshot and for the references i have use this link to understand DSL and to implement this part of the code! link: https://dbader.org/blog/writing-a-dsl-with-python#:~:text=A%20Domain%20Specific%20Language%2C%20or,regular%20expressions%20are%20a%20DSL.
11) Functional Programming: prove that you have covered all functional aspects in your code as:
*only final data structures*
Ans) Final is not in python
a) (mostly) side effect free functions
Ans) As you can see most of the functions used in Tictactoe game are side effect free function which means function owns state is not changing
b) the use of higher-order functions
Ans) I could have added this in my game but it would not have made sense of forcing this into the code, but just for the concept i did it separately in python, which i learned from geeksforgeeks , https://github.com/hasananwarr/TicTacToe-1/tree/main/HigherOrderfunction i made a simple calculating functions using higher order function
c) functions as parameters and return values
Ans) It is same as higher order function i think!
d) use closures / anonymous functions
Ans) anonymous function used Line: 19
You can also do it outside of your project. Even in another language as F#, Clojure, Julia, etc. 
