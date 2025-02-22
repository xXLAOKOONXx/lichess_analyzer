import berserk

def get_games(api_token:str, user_name:str, game_count:int=100, rated_only:bool=True):
  '''
  Scrapes games from the lichess API based on the defined preferences.
  Args:
  - api_token: The API token for the lichess API.
  - user_name: The user name of the player whose games should be scraped.
  - game_count: The number of games to be scraped.
  - rated_only: Whether only rated games should be scraped.

  Returns a list containing all games retrieved from the API.

  Each Game is a dictionary based on the API. Check out '<project>/api_reference/openapi.json' for detailed information.

  Additionally the following fields are added:

  - "side": Either "black" or "white", indicating which side the selected user played.
  - "move_list": All moves within the game as list instead of a string (as in "moves").
  - "result": Either "win", "tie" or "loss" based on whether the selected user won or not.
  - "similarity_steps": The depth of moves until the game is becoming unique, compared to the other scraped games.
  '''
  session = berserk.TokenSession(api_token)
  client = berserk.Client(session=session)

  games_list = []
  for game in client.games.export_by_player(user_name, max=game_count, rated=rated_only):
      games_list.append(game)

  for game in games_list:
    # split moves into list
    moves = game["moves"].split(' ')
    game["move_list"] = moves
    # determine side of user_name
    try:
      if game["players"]["white"]["user"]["name"] == user_name:
        game["side"] = "white"
      else:
        game["side"] = "black"
    except:
      game["side"] = "black"
    # determine result
    if not game.get("winner"):
      game["result"] = "tie"
    elif game["winner"] == game["side"]:
      game["result"] = "win"
    else:
      game["result"] = "loss"

  for game in games_list:
    unique_opening = game["move_list"]
    uniqueness_level = 0
    for check_game in games_list:
      if game["id"] == check_game["id"]:
        continue
      check_opening = check_game["move_list"]
      for j in range(0, len(check_opening)):
        # check until which move the openings are the same
        if j > uniqueness_level:
          uniqueness_level = j
        if j >= len(check_opening) or j >= len(unique_opening) or unique_opening[j] != check_opening[j]:
          break
    game["similarity_steps"] = uniqueness_level