from random_word import RandomWords


def find_occurrence(character):
    for index, current_letter in enumerate(word):
        if current_letter == character:
            yield index


def fill_in(character):
    for occ in find_occurrence(character):
        guess[occ] = character


difficulty = input("Choose your difficulty level: easy/medium/hard: ")
if difficulty == "easy":
    no_of_guesses = 20
elif difficulty == "medium":
    no_of_guesses = 12
elif difficulty == "hard":
    no_of_guesses = 7

r = RandomWords()

# Return a single random word
word = r.get_random_word(hasDictionaryDef="true")

length = len(word)
print("Length: {}".format(length))

first_letter = word[0]
print("First letter: {}".format(first_letter))

last_letter = word[length - 1]
print("Last letter: {}".format(last_letter))

# Initialise guess with first and last letter
guess = [None] * length
guess[0] = first_letter
guess[len(guess) - 1] = last_letter

# Fill in the guess with other occurrences of the first and last letter
fill_in(first_letter)
fill_in(last_letter)

guesses = set()

# Guessing starts
while no_of_guesses:
    print("------------------------------------------------------------")
    print("Current guess: {}".format(guess))
    print("You have {} guesses left".format(no_of_guesses))

    letter = input("Your guess: ")
    if letter in guesses:
        print("You already tried this one!")
        print("The letters you already tried are: {}".format(sorted(guesses)))
    else:
        if letter in word:
            print("Hooray! {} was correct!".format(letter))
            fill_in(letter)
            print(guess)

            if guess == list(word):
                print("Congrats! The word was {}".format(word))
                exit()

        else:
            no_of_guesses -= 1
        guesses.add(letter)

print("Sad. The word was: {}".format(word))
