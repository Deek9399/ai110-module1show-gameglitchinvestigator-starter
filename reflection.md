# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  
  When I first ran it, it looked simple. The idea is to guess the number in minimum attempts possible but once I actually played it: it felt confusing.
As a user the experience is not great.
Hints are not correct.
There seems to be some logic issues and the new game is not working.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. Hints are not correct, its says to Go Higher when it should be Go Lower and vice-versa.
  2. Attempt 1 is already there even if user has not started the game so users first attempt is being counted as attempt 2.
  3. Even if, the user gets the answer correct on first try , the highest score is 70.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    
    I used Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  I was working on the highest score, checking the logic of the function, even on inserting the correct number the highest score was 70 instead of 80. I asked AI to explain me the logic.
  I told it how I felt the final score should be 100 but based on the correct logic it should be 80. While working on that problem AI suggested the number of attempts is also initialized as one instead of 0, which was an error I already figured out but was also confirmed by the AI.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  When we press submit, we need to submit twice and then the hint appears. AI suggested that it works on odd attempts and not on even attempts. I tried it, it didn't work.
  I fixed the submit issue but the issue persists in the history tab.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  Initially I tested it manually, but later I used AI to write test cases for me.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I tested the hints after fixing the bugs, it worked manually and also all the related test cases passed.

- Did AI help you design or understand any tests? How?
I used AI to design test cases. It helped me understand the functions and use cases that should be tested and understand the correct behaviour.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

  I did not notice the secret number was changing while playing, but after opening the Developer Debug Info panel I could see it. Looking at the code, every time the page reruns Streamlit executes the script from top to bottom, so random.randint() was called fresh on every button click, generating a new secret. Streamlit's session state works like a persistent notepad — values stored in st.session_state survive reruns. The fix was wrapping the secret generation in if "secret" not in st.session_state: so it only runs once on the first load.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  Streamlit reruns the entire script every time you click a button, like refreshing a page. All regular variables reset. Session state is a special dictionary that survives those refreshes, so values like the secret number stay the same across clicks.
- What change did you make that finally gave the game a stable secret number?

  I wrapped the secret generation with if "secret" not in st.session_state: so that random.randint() only runs once on the first load. Every rerun after that skips it and uses the same stored value.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

    Using particular files or inline code to chat with claude and understand specific concepts more clearly.
- What is one thing you would do differently next time you work with AI on a coding task?

  Focus more on understanding the whole code and making decisons after having thorugh conversations with ai, so that i am completely aware of the tradeoffs and understanding how ai is solving the bugs.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

  AI can generate a whole working project quickly, but errors and edge cases can still be overlooked — a human still needs to review and verify the output. Understanding what the feature should do and how it should behave remains the developer's responsibility; AI is a collaborator, not a replacement. For example, designing game difficulty levels — like deciding what range and attempt count makes "Hard" actually hard — is a judgment call I'd discuss with AI rather than just accept blindly.
