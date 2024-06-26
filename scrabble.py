letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Allows lowercase version of letters as well
letters_lowercase = [letter.lower() for letter in letters]

#Created Dictionary using letters and points lists

letter_to_points = {key: value for key, value in zip(letters or letters_lowercase, points)}

#Added new key to dictionary
letter_to_points[" "] = 0 

#Function that returns the value of any given word
def score_word(word):
  point_total = 0
  for letter in word:
    word_value = letter_to_points.get(letter, 0)
    point_total += word_value
  return point_total

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"],"Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

# Returned score for each player in player_to_words dictionary
player_to_points = {}
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

#Created a function that adds a player and word and will add a new word to the list of values for an already existing player
players_and_words= {}
def play_word(player, word):
  if player not in players_and_words.keys():
    players_and_words[player] = word
  elif type(players_and_words[player]) == list:
    players_and_words[player].append(word)
  else:
    players_and_words[player] = [players_and_words[player], word]