# Chess Engine and AI

<img src="https://user-images.githubusercontent.com/103080532/219822474-5df94728-6324-4347-9189-1bd1fc8b93d8.gif" height=30% width=100%/>

This Chess AI and Engine is my first AI project. I decided to focus on chess as the premise for this project since the game is relatively fun, in my opinion. I use the PyGame library to help with implementing the graphics in ```main.py```. Most of the logic and representation of the board, engine, and AI are in the ```util.py``` file. I search for valid moves using a piece-centric approach and do a quiescence check to validate the moves in regards to pins, etc. The AI is implemented with the minimax algorithm and includes alpha-beta pruning. Board evaluation is done with piece scores and position scores. I originally decided to undertake my project by discovering Eddie Sharick on YouTube, which most of my code's structuring is loosely based on.

# Improvements

Of course, changing the depth on the minimax algorithm correlates to its performance and ability to 'look ahead.' A depth of 3 and greater significantly impact the duration of time it takes for the AI to conclude on a move. One improvement that will lead to an efficiency boost would be NumPy arrays whose implementation would be more tedious than anything.

### Thanks for checking my project out!
