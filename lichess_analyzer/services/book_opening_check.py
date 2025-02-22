from lichess_analyzer.services.opening_variation import OpeningVariation
from lichess_analyzer.services.move_tree import MoveTree

def check_follows_book_opening(book_openings: OpeningVariation, actual_opening: MoveTree):
  """
  Checks if the actual opening move follows the book opening variations.
  This manipulates the actual_opening object by setting the good_move and recommended_move attributes.
  This manipulates the book_openings object by increasing the occurences attribute.
  Args:
    book_openings (OpeningVariation): The current situation in the book opening.
    actual_opening (MoveTree): The next move made by the enemy.
  Returns:
    None
  Also prints the missplay if the actual opening move does not follow the book opening variations.
  Also prints if an enemy move was not available in the book.
  """
  book_openings.occurences += actual_opening.counts
  if not book_openings or not book_openings.followed_by:
    print('bad opening book')
    return
  if not actual_opening.move:
    print('no move')
    if not actual_opening.children:
      return
    for child in actual_opening.children:
      if child.move != book_openings.response:
        child.good_move = False
        child.recommended_move = book_openings.response
        print(f'Wrong response: {child.move} instead of {book_openings.response}')
        continue
      for enemy_response in child.children:
        check_follows_book_opening(book_openings, enemy_response)
    return
  prepared_response = book_openings.get_follow_up(actual_opening.move)
  if prepared_response is None:
    print(f'Not prepared for move: {actual_opening.move}')
    print(f'Only prepared for: {[v.enemy_move for v in book_openings.followed_by]}')
    return
  actual_player_responses = actual_opening.children
  if len(actual_player_responses) > 1:
    print('More than one responses')
  correct_response_move = None
  for response in actual_player_responses:
    if response.move.replace('+', '') != prepared_response.response.replace('+', ''):
      response.good_move = False
      response.recommended_move = prepared_response.response
      print(f'Wrong response: {response.move} instead of {prepared_response.response}')
      continue
    correct_response_move = response
  if correct_response_move is None:
    print(f'No correct response found for {actual_opening.move}')
    return
  correct_response_move.good_move = True
  for child in correct_response_move.children:
    check_follows_book_opening(prepared_response, child)