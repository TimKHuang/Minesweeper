# Minesweeper

This is a platform providing the ability for people to build their
own script to play the game *Minesweeper*. 

## Pre-Request
All the required packages are listed in the `requirements.py`.

## Run
to run the projects, `PYTHONPATH=path/to/project/ python src/Minesweeper.py`.
`PYTHONPATH` provides the directory for python to search for modules when import.

### Script / AI
The Programme provides a way to using script as a player. 
To do this, modify the `src/AI.py` and add `-ai` at the command when run.

### Options
* `-h` or `--help` to see all the options in detail
* `-t` or `--terminal` to run in terminal
* `-p` or `--pygame` to run using pygame
* `-tk` or `--tkinter` ro run using tkinter
* `ai` or run with pre-written script