letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Created Dictionary using letters and points lists
letter_to_points = {key: value for key, value in zip(letters, points)}

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

