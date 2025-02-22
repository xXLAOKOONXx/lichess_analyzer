import math

class MoveTree:
  pass

class MoveTree:
  step: int
  '''
  The step in the move list that this tree represents, e.g. the first move of a game is step 0.
  This mighht be -1 if the tree is the root.  
  '''
  counts: int
  '''The number of games that have reached this step.'''
  count_places: int
  '''The number of digits in the counts, used for formatting.'''
  move: str | None
  '''The move that this tree represents. None if the tree is the root.'''
  children: list[MoveTree]
  '''The children of this tree, representing the next moves.'''
  good_move: bool | None
  '''Whether this move is good, bad, or neutral. None if not yet determined.'''
  recommended_move: str | None
  '''The move that is recommended for this position. None if not yet determined.'''
  def __init__(self, games_list, step, counts_places: int | None = None):
    self.counts = len(games_list)
    if not counts_places:
      self.count_places = math.ceil(math.log10(self.counts))
    else:
      self.count_places = counts_places
    self.step = step
    self.move = games_list[0]["move_list"][step] if step != -1 else None
    self.children:list[MoveTree] = []
    self.good_move: bool | None = None
    self.recommended_move: str | None = None
    if self.counts == 1:
      return
    next_moves = list(set([g["move_list"][step + 1] for g in games_list if len(g["move_list"]) > step + 1]))
    for move in next_moves:
      next_games = [g for g in games_list if len(g["move_list"]) > step + 1 and g["move_list"][step + 1] == move]
      self.children.append(MoveTree(next_games, step + 1, counts_places=self.count_places))

  def __str__(self):
    good_move_string = '+' if self.good_move is True else '-' if self.good_move is False else ' '
    return f'''{str(self.move):>5} ({str(self.counts):>{self.count_places}}) [{good_move_string}]'''

  def complex_str(self) -> str:
    '''
    Generates a string representation of the current object and its children.
    This representation uses one row per move, so it might be challenging for larger trees.
    '''
    spacing = '  ' * self.step
    head = f'{spacing}{self.move} ({self.counts})'
    if not self.children:
      return head
    children = '\n'.join([str(c) for c in self.children])
    return f'{head}\n{children}'
  
  def gridified(self) -> list[list[str]]:
    '''
    Generates a grid representation of the current object and its children.
    Returns:
      list[list[str]]: A 2D list where each sublist represents a line in the grid.
                Each element in the sublist is a string representation of the object or its children.
    '''
    lines:list[list[str]] = [[str(self)]]
    for _ in range(1, self.counts):
      lines.append([''])
    if not self.move:
      lines = [[] for _ in range(self.counts)]
    current_line = 0
    for child in self.children:
      child_lines = child.gridified()
      for child_line in child_lines:
        lines[current_line].extend(child_line)
        current_line += 1
    return lines

  def gridprint_file(self, filepath='opening_tree.txt'):
    '''
    Prints the gridified representation of the tree to a file.
    Args:
      filepath (str): The path to the file where the gridified tree should be printed.
    '''
    lines = self.gridified()
    with open(filepath, 'w') as f:
      for line in lines:
        f.write(' '.join([f'{col:>{12 + self.count_places}}' for col in line]) + '\n')

  def gridprint(self):
    '''
    Prints the gridified representation of the tree to the console.
    '''
    lines = self.gridified()
    for line in lines:
      print(' '.join([f'{col:>10}' for col in line]))