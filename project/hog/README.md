[toc]

## Hog

### Rules

- **Pig Out**: If any of the dice outcomes is a 1, the current player's score for this turn is 1.

    投到 1 的一方本轮得分为 1

- **Free Bacon**: A player who chooses to roll zero dice scores `k+3` points, where `k` is the `n`th digit of `pi` after the decimal point, and `n` is the total score of their opponent. As a special case, if the opponent's score is `n = 0`, then `k = 3` (the digit of pi before the decimal point).

    选择不投的一方本轮得分为 pi 的小数点后第 n 位数字 k + 3，**n 为对方所得总分**

- **Swine Align**. After points for the turn are added to the current player's score, if both players have a positive score and the Greatest Common Divisor (GCD) of the current player's score and the opponent's score is at least 10, take another turn.

    如果本轮得分加给当前一方后，**每一方的总分都为正数且两方得分的最大公约数大于等于 10**，则当前一方再加一轮

- **Pig Pass**. After points for the turn are added to the current player's score, if the current player's score is lower than the opponent's score and the difference between them is less than 3, the current player takes another turn.

    如果本轮得分加给当前一方后，如果当前一方的分数低于对方且分差小于 3，则当前一方再加一轮

### Files

- `hog.py`: A starter implementation of Hog
- `dice.py`: Functions for rolling dice
- `hog_gui.py`: A graphical user interface (GUI) for Hog
- `ucb.py`: Utility functions for CS 61A
- `ok`: CS 61A autograder
- `tests`: A directory of tests used by `ok`
- `gui_files`: A directory of various things used by the web GUI
- ``test.py``: A test file for hog project

### Phase 1: Simulator

- Remember to call `dice()` exactly `num_rolls` times even if \*Pig Out\* happens in the middle of rolling. In this way, you correctly simulate rolling all the dice together.
- Only call a strategy function **once** per turn (or risk breaking the GUI). 

### Phase 2: Commentary

- A commentary function always **returns another commentary function** to be called on the next turn. The only side effect of a commentary function should be to print.

### Phase 3: Strategies

- To implement this function, you need a new piece of Python syntax `*args`

```python
>>> def printed(f):
...     def print_and_return(*args):
...         result = f(*args)
...         print('Result:', result)
...         return result
...     return print_and_return
>>> printed_pow = printed(pow)
>>> printed_pow(2, 8)
Result: 256
256
>>> printed_abs = printed(abs)
>>> printed_abs(-10)
Result: 10
10
```

