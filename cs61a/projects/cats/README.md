[toc]

## Cats

### Files

Here are the files included in the archive:

- `cats.py`: The typing test logic.
- `utils.py`: Utility functions for interacting with files and strings.
- `ucb.py`: Utility functions for CS 61A projects.
- `data/sample_paragraphs.txt`: A file containing text samples to be typed. These are scraped Wikipedia articles about various topics.
- `data/common_words.txt`: A file containing common English words in order of frequency.
- `data/words.txt`: A file containing many more English words in order of frequency.
- `gui.py`: A web server for the web-based graphical user interface (GUI).
- `gui_files`: A directory of files needed for the graphical user interface (GUI).
- `images`: A directory of images.
- `ok, proj02.ok, tests`: Testing files.

### Phase 1: Typing

**Time to test your typing speed!** 

```shell
python3 cats.py -t cats kittens
```


You can try out the web-based graphical user interface (GUI) using the following command.

```shell
python3 gui.py
```

### Phase 2: Autocorrect

**Extensions:** You may optionally design your own diff function called `final_diff`. Here are some ideas for making even more accurate corrections:

- Take into account which additions and deletions are more likely than others. For example, it's much more likely that you'll accidentally leave out a letter if it appears twice in a row.
- Treat two adjacent letters that have swapped positions as one change, not two.
- Try to **incorporate (合并)** common misspellings

### Phase 3: Multiplayer

Be sure to use the `game` constructor when returning a `game`, rather than assuming a particular data format. Read the definitions for the `game` constructor and selectors in `cats.py` to learn more about how the data abstraction is implemented.