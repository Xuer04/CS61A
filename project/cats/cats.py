"""Typing test implementation"""

from os import times
from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########

# AC
def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    choose_list = [paragraph for paragraph in paragraphs if select(paragraph)]
    return choose_list[k] if len(choose_list) >= k + 1 else ''
    # END PROBLEM 1

# AC
def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def select(paragraph):
        paragraph = remove_punctuation(paragraph)
        paragraph_list = [lower(subsrting) for subsrting in split(paragraph)]
        for word in topic:
            if word in paragraph_list:
                return True
        return False

    return select
    # END PROBLEM 2

# AC
def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if typed == '':
        return 0.0
    else:
        count = 0
        for index in range(0, min(len(typed_words), len(reference_words))):
            if typed_words[index] == reference_words[index]:
                count += 1
        return count / len(typed_words) * 100
    # END PROBLEM 3

# AC
def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    typed_len = len(typed)
    typed_speed =  (typed_len / 5) / elapsed * 60
    return typed_speed
    # END PROBLEM 4

# AC
def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    else:
        # get the list of all diff between elemnt and user_word.
        diff_list = [diff_function(user_word, valid_word, limit) for valid_word in valid_words]
        if min(diff_list) > limit:
            return user_word
        else:
            return valid_words[diff_list.index(min(diff_list))]
    # END PROBLEM 5

# AC
def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    if start == "":
        return len(goal)
    elif goal == "" or limit < 0:
        return len(start)
    else:
        if start[0] != goal[0]:
            return 1 + shifty_shifts(start[1:], goal[1:], limit - 1)
        else:
            return shifty_shifts(start[1:], goal[1:], limit)
    # END PROBLEM 6

# AC
def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # BEGIN
    "*** YOUR CODE HERE ***"
    if start == goal:
        return 0
    elif start == "":
        return len(goal)

    elif goal == "" or limit < 0:
        return len(start)

    else:
        if start[0] != goal[0]:
            add_diff = 1 + pawssible_patches(start, goal[1:], limit - 1)
            remove_diff = 1 + pawssible_patches(start[1:], goal, limit - 1)
            substitute_diff = 1 + pawssible_patches(start[1:], goal[1:], limit - 1)
            return min(add_diff, remove_diff, substitute_diff)
        else:
            return pawssible_patches(start[1:], goal[1:], limit)
    # END

# TODO
def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########

# AC
def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    count = 0
    for index in range(len(typed)):
        if typed[index] != prompt[index]:
            break
        else:
            count += 1
    progress = count / len(prompt)  # calculate progress
    report = {'id':user_id, 'progress':progress}  # construct report
    send(report)  # send report with the given send function
    return progress
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report

# AC
def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including
        the time the player started typing, followed by the time the player finished typing each word.

        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    times_list = [[item[index + 1] - item[index] for index in range(0, len(item) - 1)] for item in times_per_player]
    return game(words, times_list)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    all_fastest_words_list = [[] for _ in player_indices]  # construct a empty list for each player
    all_times_list = all_times(game)  # get all times for each player
    for word_index in word_indices:
        each_word_times_list = [all_times_list[player_id][word_index] for player_id in player_indices]  # get all times for each word
        each_word_fastest_player_index = each_word_times_list.index(min(each_word_times_list))  # select the fastest player for each word
        all_fastest_words_list[each_word_fastest_player_index].append(word_at(game, word_index))  # find the fastest player and add this word to its list
    return all_fastest_words_list
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = True # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)

