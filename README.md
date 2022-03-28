# python-wordle-cli

Command line game based on wordle classic.

Installation
============

```
git clone https://github.com/vhidrogo/python-wordle-cli.git
cd python-wordle-cli
python wordle.py <letter_count>
```

Demo with 4 letters
===================

```
victorhidrogo@Victors-MacBook-Pro desktop % python wordle.py 4

5 Tries left. Enter a valid 4 letter word: hope

----Game Board----
Hope
****
****
****
****

----Key Board-----
q w * r t y u i * *
a s d f g H j k l
z x c v b n m

4 Tries left. Enter a valid 4 letter word: high

----Game Board----
Hope
HigH
****
****
****

----Key Board-----
q w * r t y u * * *
a s d f * H j k l
z x c v b n m

3 Tries left. Enter a valid 4 letter word: hash

----Game Board----
Hope
HigH
HASH
****
****

----Key Board-----
q w * r t y u * * *
A S d f * H j k l
z x c v b n m

YOU FOUND THE WORD WITH 2 TRIES LEFT!!
```

Dependencies
============

- english-words >= 1.1.0