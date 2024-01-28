# The Lost Island
![Mockup](docs/mockup.webp)
[Live site](https://git.heroku.com/lost-island.git)
## Introduction
This is a text-based adventure game.

The game invites the user to an exciting interactive story, where the user's different choices controls the direction of the story.

Since this is a text-based game, I have made an active choice not to validate the inputs where the user is prompted to press enter to be interactive. These inputs are part of the design and their purpose is to keep the user interested in the game.

## Project goals

* Write code that is clean and readable.

* Write code where the user is interactive in the story.

* Hold the user's interest with an exciting story.

* Create a design that lightens up the text and makes the game user-friendly.

## Features
### Existing Features
### Future Features


## Data Model
### Flowchart
I used a flowchart from [Lucidchart](https://www.lucidchart.com/pages/ER-diagram-symbols-and-meaning)
to map out how I envisioned the logic of the game. This flowchart is a basis for the most important functions and directions of the game. therefore, the number of scenes may differ from the final result.

![Flowchart](docs/blank_diagram.webp)

### Imports
I've used the following Python packages and/or external imported packages.

* `sys`: used for the restart() and print_slow() functions.
* `os`: used for the clear() function.
* `time`: used for time.sleep()function.
* `pyfiglet`: used for including the ASCII art.
* `colorama`: used for including colors.

## Testing
* Throughout this project I have been testing the game by running it in the gitpod terminal.
* Tested in Heroku terminal aswell
* The code has been run through the Code Institutes Linter with no errors.

![Python Linter](docs/linter_1.webp)

![Python Linter](docs/linter_2.webp)
## Deployment
### Adding, committing and pushing code
* All code has been pushed to the repository [adventure-game](https://github.com/Linnea87/adventure-game)
* All code has been regurlary added, committed and pushed throughout the project.
* The commands being used are `git add <file>`,
  `git commit -m “commit message”` and
  `git push`
* Due to being completely brand new into this tech world, the `git commit -m “commit message”` have gradually improved throughout this project. 
### Deploying to Heroku
I deployed my project directly to Heroku by doing the following:

* Created an account at Heroku.com.
* Installed my own packages in the requirements.txt terminal by typing `pip3 freeze --local > requirements.txt`
* Clicked on "Create new app" and named it adventure-game.
* Clicked on Settings and added Backpacks - Python and Node.js.
* Made sure the backpacks were in the right order.
* From the new app Settings, I clicked Reveal Config Vars, and sets the value of KEY to PORT, and the value to 8000 then selected add.
* Connected my GitHub profile and found the right Repository.
* Manually deployed the page and clicked "Eanble automatic deploys" at the same time.
## Credits

**Source**|**Location**|**Notes**
:-----:|:-----:|:-----:
[Colorama](https://pypi.org/project/colorama/)|Adventure-game terminal|Page to help add colors in the terminal
[Pypi](https://pypi.org/project/pyfiglet/)|Adventure-game terminal|ASCII art came from this page
[Figlet](https://www.figlet.org)|Adventure-game terminal|ASCII font style came from this page
[Stack overflow](https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing)|Adventure-game terminal|Type slow function inspired from this page
[Geeks for geeks](https://www.geeksforgeeks.org/clear-screen-python/)|Adventure-game terminal|Clear function are inspired from this page
[Python long-string](https://note.nkmk.me/en/python-long-string/)|Adventure-game terminal|Inspired from this page to split code when one line exceeds 80 characters
[Stack overflow](https://stackoverflow.com/questions/10506973/can-not-increment-global-variable-from-function-in-python)|Adventure-game terminal|Inspired how to use the global key  to transfer variables from one function to another
[Github](https://gist.github.com/jrosco/d01b28c2f37100bb5278)|Adventure-game terminal|Code that are modify for restart the game

## Acknowledgments

* Thanks to my mentor [Graeme Taylor](https://github.com/G-Taylor) who always gives me good tips, advice and feedback on how to plan and implement my projects. And for this project advised me how to best use the flowchart and gif recording.