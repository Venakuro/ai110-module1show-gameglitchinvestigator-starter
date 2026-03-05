# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
ans: The game looked normal when i first run it. It is a number guessing game which gives you clues in order for you to guess the number. It has limited attempts and a place to set the difficulty.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  ans: one bug i noticed was that, regardless of the guess i put in, it kept telling me go lower. Another bug i noticed was that when i change the difficulty and the range is supposed to change, the secret number could still be out of range. I also noticed that the newgame feature does not work

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
ans: The AI suggested that the Hard range should be larger than Normal. I checked this by inspecting the website myself and agreed that it is logically for Hard to have a higher range to make the guessing more difficult.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
ans: The AI did not give me any wrong suggeston.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
