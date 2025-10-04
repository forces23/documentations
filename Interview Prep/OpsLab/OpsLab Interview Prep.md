# 📌 Interview Prep Plan for OpsLab

## 1. **Project Deep Dive (Behavioral + Technical Mix)**

They’ll want to see if you can clearly explain your past work and  **map it to their stack** . Expect to go deep on:

* **Missouri Medicaid Portal (React/TypeScript)**
  * How you led the frontend (ownership, leadership, scaling forms system).
  * Challenges (state management, validation, async API calls, testing).
  * Tradeoffs you made (performance vs reusability, error handling, accessibility).
  * Your testing approach (unit + integration with Vitest).
* **AWS AI/Cloud Chatbots**
  * How you integrated with Bedrock, Lex, Connect.
  * Scalability, cost optimization ($50k savings w/ Lambda script).
  * Handling edge cases or production issues.

👉 Practice telling each project like a story:

 **Situation → Task → Action → Result (STAR)** .

⚡ Example Q’s you might get:

* “Tell me about a technical challenge you solved on the Medicaid project.”
* “How did you ensure reliability in the reusable form system?”
* “What tradeoffs did you face when standardizing forms?”
* “How did you collaborate with backend teams across time zones?”

---

## 2. **React & Frontend Knowledge**

Since the role is front-end heavy (70%+ React/TS), expect these:

* **Core Concepts**
  * State vs props
  * Lifecycle (functional + hooks)
  * useEffect pitfalls (dependencies, cleanup functions)
  * Context API vs Redux (when to use each)
  * Controlled vs uncontrolled components
  * Keys in lists
* **Advanced Topics**
  * Performance optimization (React.memo, useCallback, code splitting, lazy loading).
  * Form handling (validation, reusability—perfect tie-in to your past project).
  * Testing (Vitest/Jest, RTL—unit vs integration differences).
  * Error boundaries & handling async errors.

⚡ Example Q’s:

* “Explain the difference between state and props, and when you’d use each.”
* “What happens if you forget the dependency array in useEffect?”
* “How do you prevent unnecessary re-renders in React?”
* “How would you structure and test a reusable form component?”

---

## 3. **CS Fundamentals**

They said “assess CS fundamentals.” Since it’s not a leetcode-heavy role (mid-senior full stack, but frontend-focused), expect  **applied fundamentals** :

* **Data Structures**
  * Arrays, objects, sets, maps → when to use which.
  * Hash maps (fast lookups, uniqueness).
  * Queues/stacks basics.
* **Algorithms**
  * Time/space complexity (Big O) of common ops.
  * Searching/sorting basics.
  * Iteration vs recursion (pros/cons).
* **Systems Design (Lightweight)**
  * How frontend and backend communicate (RESTful APIs).
  * Pagination (why and how).
  * Caching strategies (browser cache, memoization).
  * Authentication (JWT/session basics).

⚡ Example Q’s:

* “How would you check if a string has all unique characters?”
* “What’s the time complexity of searching in a hash map vs array?”
* “How would you design a scalable frontend that consumes a slow API?”
* “How do you handle large datasets in React (e.g., 10,000 rows)?”

---

## 4. **Back-End / Full-Stack Awareness**

Even though you’re frontend-leaning, they may check if you can collaborate with backend devs:

* Basics of **Kotlin/Spring Boot** (map it to your Java/Spring Boot experience).
* REST principles (GET vs POST, idempotency, status codes).
* How you debug API integration issues.
* SQL basics (joins, indexing, optimization).

⚡ Example Q’s:

* “When would you use a POST vs PUT?”
* “How would you debug a failing API call in your React app?”
* “What’s an index in a database and why is it useful?”

---

## 5. **Behavioral & Culture Fit**

OpsLab is small, defense-focused, and this role touches leadership. Expect culture-fit checks:

* Comfortable in ambiguity (“embraces uncertainty”).
* Self-starter attitude.
* Collaboration across time zones.
* Interest in defense/Navy domain (you don’t need deep knowledge, just show curiosity).

⚡ Example Q’s:

* “Tell me about a time you had to deliver without complete information.”
* “How do you stay motivated when learning a new technology quickly?”
* “Describe a time you led an initiative or mentored others.”

---

# 📅 Prep Timeline (Next Few Days)

**Day 1:**

* Rehearse project stories (Medicaid Portal + AWS AI).
* Review React fundamentals (hooks, state, props, rendering).

**Day 2:**

* Brush up on CS fundamentals (hash maps, time complexity, arrays/sets).
* Practice a few coding problems (arrays, strings, maps).
* Refresh RESTful API + DB basics.

**Day of Interview:**

* Quick review of React optimization & testing.
* Re-read your resume + answers so you’re consistent.
* Be ready with 2-3 thoughtful questions for them (e.g., “What challenges is OpsLab facing scaling the frontend?”).
