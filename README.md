# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Game's purpose:** A number guessing game where the player tries to guess a secret number in the minimum attempts possible. The difficulty setting controls the number range and attempt limit. Points are awarded for winning and deducted for each wrong guess.

- [x] **Bugs found:**
  1. Hints were backwards — "Go Higher" shown when guess was too high, and vice-versa
  2. Attempts initialized to 1 instead of 0, so the first guess was counted as attempt 2
  3. Max score on first correct guess was 70 instead of 80 due to the attempt bug above
  4. On every even-numbered attempt, the secret was cast to a string, making comparison fail
  5. Submit button required two clicks due to Streamlit form/input focus behavior
  6. New Game did not reset score, status, or history, and ignored the selected difficulty range
  7. Info bar always showed "1 to 100" regardless of selected difficulty
  8. Wrong guess on even attempts added +5 points instead of deducting 5

- [x] **Fixes applied:**
  1. Swapped hint messages in `check_guess` — Too High now says "Go LOWER", Too Low says "Go HIGHER"
  2. Changed `attempts` initialization from `1` to `0`
  3. Removed the even/odd type cast that converted secret to string on even attempts
  4. Wrapped input and submit in `st.form` so a single click submits correctly
  5. Fixed New Game to reset all session state and use `random.randint(low, high)`
  6. Updated info bar to use `{low}` and `{high}` from the difficulty range
  7. Fixed score deduction to always subtract 5 for wrong guesses regardless of attempt number
  8. Refactored all logic into `logic_utils.py` and added 24 pytest unit tests

## 📸 Demo

![Game Demo](screenshot/Screenshot%202026-03-19%20234128.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
