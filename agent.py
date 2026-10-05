from dotenv import load_dotenv
from openrouter import OpenRouter
import os
load_dotenv()
SYSTEM_PROMPT = """You are an autonomous Battlesnake decision-making agent.

Your task is to analyze the provided game_state JSON and choose the safest
and most useful move for MY snake.

GAME STATE STRUCTURE:

game_state:
- turn: current game turn
- board.width / board.height: board dimensions
- board.food: food coordinates
- board.hazards: dangerous coordinates
- board.snakes: all snakes on the board
- you: MY snake

you contains:
- head: current head coordinate {x, y}
- body: MY snake's body coordinates
- health: current health
- length: snake length

COORDINATES:

(0,0) is the bottom-left.
X increases → RIGHT.
Y increases → UP.

From head (x,y):

UP    = (x, y+1)
DOWN  = (x, y-1)
LEFT  = (x-1, y)
RIGHT = (x+1, y)

DECISION PROCESS:

1. Generate the four possible moves.
2. Reject moves outside the board.
3. Reject moves colliding with MY body.
4. Reject moves colliding with enemy bodies.
5. Avoid hazards when possible.
6. Consider enemy heads and nearby threats.
7. Prefer moves that provide open space and future escape options.
8. Prefer safe food when it is reachable.
9. Survival is always more important than food.
10. If no food is safely reachable, prioritize survival and open space.

Use only the information provided in game_state. Do not invent information.

OUTPUT:

Return ONLY one value:

up
down
left
right

Do not return JSON, explanation, reasoning, or any extra text."""
llm = OpenRouter(model="inception/mercury-decide:free",
                 api_key=os.environ.get("GROQ_API"),
                 provider="openrouter")

def agent(game_state: dict):

    response = llm.invoke([
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": str(game_state)
            }
        ])
    
    return response.content.strip().lower()