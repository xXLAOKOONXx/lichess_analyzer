class OpeningVariation:
  pass

class OpeningVariation:
  '''
  Class to represent an opening variation in a chess opening book.
  Attributes:
    enemy_move (str): The move that the opponent plays in this variation. None if the player starts as white and therefor has nothing to respond to.
    response (str): The move that the player plays in response to the opponent's move.
    followed_by (list[OpeningVariation]): A list of opening variations that can follow this one.
    comment (str): A comment about this variation.
    occurences (int): The number of times this variation has been played.
  '''
  enemy_move: str | None
  '''The move that the opponent plays in this variation. None if the player starts as white and therefor has nothing to respond to.'''
  response: str
  '''The move that the player plays in response to the opponent's move.'''
  followed_by: list[OpeningVariation]
  '''A list of opening variations that can follow this one. Each enemy move should be included not more than 1 times.'''
  comment: str
  '''A comment about this variation.'''
  occurences: int
  '''The number of times this variation has been played.'''
  def __init__(self, enemy_move: str | None, response: str, followed_by: list[OpeningVariation] = [], comment: str = ''):
    self.enemy_move = enemy_move.strip() if enemy_move else None
    self.response = response
    self.followed_by = followed_by
    self.comment = comment
    self.occurences = 0

  def is_enemy_move(self, enemy_move: str):
    return enemy_move.strip().replace('+','') == self.enemy_move
  
  def get_follow_up(self, enemy_move: str) -> OpeningVariation | None:
    for variation in self.followed_by:
      if variation.is_enemy_move(enemy_move):
        return variation
    return None
  
  def child_lines_count(self) -> int:
    if not self.followed_by:
      return 1
    for v in self.followed_by:
      if not isinstance(v, OpeningVariation):
        print(f'Error with opening variation: {v} is a string not an OpeningVariation; {self}')
        return 1
    return sum([v.child_lines_count() for v in self.followed_by])
    
  def __str__(self):
    return f'{self.enemy_move} ({self.occurences}) {self.response}'
    
  def gridified(self) -> list[list[str]]:
    '''
    Generates a grid representation of the current object and its children.
    Returns:
      list[list[str]]: A 2D list where each sublist represents a line in the grid.
                Each element in the sublist is a string representation of the object or its children.
    '''
    lines:list[list[str]] = [[str(self)]]
    for _ in range(1, self.child_lines_count()):
      lines.append([''])
    if not self.enemy_move:
      lines = [[] for _ in range(self.child_lines_count())]
    current_line = 0
    for child in self.followed_by:
      child_lines = child.gridified()
      for child_line in child_lines:
        lines[current_line].extend(child_line)
        current_line += 1
    return lines
  
  def gridprint_file(self, filepath='opening_book_tree.txt'):
    '''
    Prints the gridified representation of the tree to a file.
    Args:
      filepath (str): The path to the file where the gridified tree should be printed.
    '''
    lines = self.gridified()
    with open(filepath, 'w') as f:
      for line in lines:
        f.write(' '.join([f'{col:>20}' for col in line]) + '\n')