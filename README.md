# Chess Engine and AI

<img src="https://user-images.githubusercontent.com/103080532/219822474-5df94728-6324-4347-9189-1bd1fc8b93d8.gif" height=30% width=100%/>

This Chess AI and Engine is my first AI project. I used the PyGame library to help with implementing the graphics in ```main.py```. Most of the logic and representation of the board, engine, and AI are in the ```util.py``` file. I search for valid moves using a piece-centric approach and do a quiescence check to validate the moves in regards to pins, etc. The AI is implemented with the minimax algorithm and includes alpha-beta pruning. Board evaluation is done with piece scores and position scores. I originally decided to undertake my project by discovering Eddie Sharick on YouTube, which most of my code's structuring is loosely based on.

# Improvements

A depth of 3 and greater significantly impacts the duration of time it takes for the AI to conclude on a move. So, some improvements that could be made that could push the depth to 4 or 5 (albeit with an upper bound of 30 seconds), especially for this specific minimax implementation might be:

* using move ordering instead of visiting nodes in the minimax tree randomly -> increase prob. of an earlier beta cutoff
* use move caching (lru)
* give the model data on openings -> move lookup rather than generation in the early game
* an inherently faster, compiled programming language...

### Thanks for checking my project out!
