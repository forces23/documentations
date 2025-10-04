# 📝 Mock Interview Sheet – OpsLab Prep

---

## Section 1: Project Deep Dive

## **Q1.** Can you walk me through the Medicaid Provider Portal project? What was your role, and what challenges did you face?

**Your Answer: The medicaid Provider portal project was to revamp the existing Provider Portal Project. its portal that allows providers to come and fill out forms whether i be pharmacy forms , elgibility forms , etc. My role in this Project was to bring the UI designs to life. we had a team that was tasked to build the UI in figma and i was task to make the UI look and function they way they expected. but since i was in the portal all the time i would also suggest functionality changes. It started out with a team of 2 but i was the only one the was fully dedicated to the project. the other team member had to split his work up. My main task was the forms but i would also create anything they needed, especially for time sensitive task. the biggest challenges i was faced was 1 there was a demo for the state of Virginia and i was task to complete this specific functionality within a short timeline and the biggest challenge was figuring out the structure that was going to be the layout for the entire way the forms were going to be created by any team memeber assisting on the project. it had to be simple and straight forward enough that anyone could just come in and hit the ground running. it took some time but i was able to get it to where it was easy and quick for anyone to jump in and start build forms.**

## **Q2.** Tell me about the reusable form system you built. How did you design it, and what impact did it have?

**Your Answer: again for the provider portal forms i had to create the forms that were able to be reused for different types of forms. the way i did that was actually creating reusable and configurable input components for the different form inputs. so all you had to do was call the correct component and pass it a config for the input and it would build the layout and style the forms input. this way everything was uniformed across the whole site and other developers didnt need to worry about the styles also.**

## **Q3.** How did you handle collaborating with backend developers across time zones when APIs weren’t working as expected?

**Your Answer: That was the most difficult part of being in my company since it was an indai based company a lot of the remote backend developers were in India and i would have to either get up early or stay up late to try to catch a team member to collaborate with if need for issues or just to update what i have done so they can proceed with what they are doing and vise versa**

## **Q4.** Can you describe a bug or issue that you caught with your unit/integration tests?

**Your Answer: i was able to actually catch anything doing this due to it being in the early stages of the project when i actually learned about this but i was testing it and learning how it worked by starting to apply unit test and integration testing check in the application by checking the function outputs and checking if components were rendering correctly.**

## **Q5.** Tell me about the AWS AI chatbot project. How did you design it, and what technologies did you use?

**Your Answer: there was 2 different Chatbots that i worked on. there was the chat bot that answered general user questions and if the user felt the need to they could ask to escalate to a live agent. this chat bot was mainly using Amazon Lex, bedrock, knowledge bases, Amazon Q, AWS Connect. the other Chatbot that i worked on was a chat bot that was able to answer question based off of document and rule excel sheets that we had uploaded to AWS S3 buckets synced into the knowledge bases in Bedrock. This chat bot was supposed to be able to answer question about the website for navigational purposes and also to answer question for lets say if they were filling out a form and didnt know what a form question was exactly asking they could ask the chat bot and the chot would help give a better understanding to the user. this one was actually a chat bot that my Team and I had teamed up with AWS themselves to build. this one had a UI built with Streamlit and was embeded in the application using iframe**

---

## Section 2: React & Frontend Knowledge

## **Q6.** What’s the difference between props and state?

**Your Answer: props are data passed into a component that are immutable in the child. state is a variable that has 2 pieces a variable that holds the data and an updater function that allows the user to update the state variable. to update props in the component you would need a callback function or you can create a state variable and pass the state variable and the updater function if the child component needs to update it.**

## **Q7.** Walk me through what happens when you forget the dependency array in `useEffect`.

**Your Answer: if you do not use a dependency array in a useEffect the hook will trigger everytime the ui changes/re-renders**

## **Q8.** How do you prevent unnecessary re-renders in React?

**Your Answer: depends on what it is but you can use react.memo for components, useMemo for variables, and useCallback for functions.**

## **Q9.** When would you choose Context API over Redux (or vice versa)?

**Your Answer: i would say that you would use Context API for simple global state management and use Redux for more complex statemanagment**

## **Q10.** How would you test a reusable form component? What would you focus on in unit vs. integration tests?

**Your Answer: i would test a reusable form component by testing whats actually render on the page and i would use integration testing for this type of testing**

---

## Section 3: CS Fundamentals

## * **Q11.** What’s the time complexity of searching for an element in an array vs. a hash map?

**Your Answer:**

## **Q12.** How would you check if a string has all unique characters? (Talk through your approach.)

**Your Answer: i think the easiest way would to convert the string to a hash set and then back to a string and compare both strings if they match then there was nothing taken out due to the hasset only accepting unique values. if the strings dont match then the original string had repeating values in it**

## * **Q13.** How would you handle rendering 10,000 rows of data in a React app?

**Your Answer:**

## * **Q14.** When would you use recursion over iteration? Can you give an example?

**Your Answer:**

## **Q15.** How would you design the frontend to handle slow or unreliable API responses?

**Your Answer: i would add a loading state functionailty so that the user knows that soemthing is happening and does not get frustrated thinking that its not working. resulting in a better user experience**

---

## Section 4: Backend Awareness

## * **Q16.** What’s the difference between a POST and PUT request?

**Your Answer:**

## **Q17.** How would you debug a failing API call in your React app?

**Your Answer: i would read the logs and also see if i can get a successful response at all using something like post man to determine where the issue lies first. if it works in postman and not the React app then i know where to start checking**

## * **Q18.** What’s a database index, and why is it important?

**Your Answer:**

---

## Section 5: Behavioral / Culture Fit

## **Q19.** Tell me about a time you had to deliver without complete information. How did you handle it?

**Your Answer: In the Momed Revamp project i had this issue quite a bit. there was many times where i would finish my task fastr then the design team or the BI's team would finish for me to do something else but i knew there was task that still needed to be done so i would take it upon myself to start working in a different task on the project or different section that had been started yet even at times designing it myself keeping  in mind the other designs for other sections. i would proactively be looking for things to do whether it be taking on other tassk or reaching out to other teams to see if i could assist them in anything they needed help on.**

## **Q20.** Describe a time you had to quickly learn a new technology. What was your approach?

**Your Answer: This was my entire time at my last job haha. they had me whering many different hats in the programming world. I i had been given task so many times where i had been given a tak even though i didnt know the technology. the way i would go about it is i would do a lot of research using Udemy and youtube along with practice problems then when AI got really big i started using AI to help excel my learning but AI doesnt know everthing so i still had to read doceumention for  alot of topics.**

## * **Q21.** How do you stay motivated when facing ambiguity?

**Your Answer:**

## **Q22.** Can you give an example of mentoring or guiding a teammate?

**Your Answer: yeah ive had this quite a bit in my last job. i was given an intern where i would assign simple task or answer question for him. also since i was the main person for frontend and developing in AWS i would guide other teamates in how to do certain things. and again with leading the frontend of the provider ortal i had to teach other developers what i did for them to understand how i created the forms and how to use them.**

## **Q23.** Tell me a little about yourself.

**Your Answer: Okay yeah i am a software engineer / cloud developer. my last employer was Wipro Ltd where the main client was State of missouri Medicaid, and sometimes i was other states medicaid too if they were tryinh to win bids. I had worked with Java, Python, React, Typescript Many AWS Services that revolve around developing in the cloud including AI service in AWS. I worked with many different teams help out in all of them. some of those teams were BIA's, Backend Developers, System Admins, which i enjoyed because i like the change and faster pace life style in a job. I was with them for about 3 years before my Wife and i decide to take a leap of faith with a job offere she recieved that would move us here to just get out of the small town we were in to move to a town with a lot more opportunities for both of us.**

## **Q24.** Why are you interested in this role/company?

**Your Answer:Well for one i like that you are working with our armed forces to make things better. my Stepdad was in the Army and i was going to join the Navy with some friends out of high school but i didnt out of respect for my stepdad, he always told me and my brother that he didnt want us go through the things he didnt want that life for us. I really appreciat the military and all they do for us. so it would be nice to be on a team that is working to make things better for them.**

## Technical Knowledge (CS Fundamentals)

## **Q25.** Can you explain the difference between an array and a linked list?

**Your Answer: an array is index based and you to any spot in the indext directly while a liked list you have to go down the chain due to the way the pointers are setup and how it is stored in memory**

## **Q26.** What is Big-O notation? Why is it important?

**Your Answer: The big-o notation is the formual that tells how mch time it takes for a certain function/algorithm to run or how much space it will take up and its important because if you know this then you can find ways to make functions/alogorithms run faster or take upo less space**

## **Q27.** Walk me through how a hash map works internally.

**Your Answer: the only thin i know is that in a hashamap you can only have unique values**

## **Q28.** Explain recursion and give an example where it’s useful.

**Your Answer: recursion is when a function cals its self when doing so get added to a stack and when that stack get full its called a stack overflow which is an issue so you need to inmplement a way of say you can only call your self this many times so that you dont reach that stack overflow point. as far as wher it is useful i am unsure.**

## Coding Questions (Think Aloud!)

## **Q29.** Write a function to reverse a string in Python.

**Your Answer:**

you could use the 2 pointer method which would allow one poiunter to start a the begining and one at the end and they swap values until p1 meets p2 at that point the string should be reveresed

## **Q30.** Given an array of integers, return two numbers that add up to a target. (Two Sum problem)

**Your Answer: for this one if you wanted to get 2 numbers in an array that equal a target number then you could do a 2 sum algorithim where one pointer is at the begingin and one is at the end and keep checking the sum and seeing of it higher or lower which tell you which pointer to move**

## **Q31.** How would you check if a string is a palindrome?

**Your Answer:again you would you 2 pointer one at the end and one at the start and as long as each character is the same till they meet i the middle then its a palindrome otherwise it fails and it is not**

## System Design / Applied Thinking

## **Q32.** How would you design a URL shortener like Bitly? (Talk about storage, scalability, collisions, etc.)

**Your Answer: i have no idea. to be honest but i would love to figure that out sometime maybe in my next project ill try to figure that out**

## **Q33.** If you were building a chat app, how would you handle real-time message delivery?

**Your Answer: I have not built a chat app but i feel like it has something to do with streams**

## Behavioral Questions (STAR Method)

## **Q34.** Tell me about a time you faced a challenging bug and how you solved it.

**Your Answer: i cant think of anything right now**

## **Q35.** Describe a time you had to work in a team where not everyone agreed. What did you do?

**Your Answer: when i first joined my last project the manager had a older way of thinking on styles so i had to figure ways ou tto make things modern but still be able to appease him with what he was wanting. so i would try to infrom him on the new ways of styling today and i would see if he could come to a comprimise or if we could figure out what exactly he was wanting so that i could work around that and still make hime happy**

## **Q36.** What’s a project you’re most proud of, and why?

**Your Answer: all the projects i have done i was very proud due to them throwing me into things with no prior knowledge and on a short deadline and still coming though on top. but if i had to pin point one thing i would say it was the forms build layout that i had created in the Momed project that layed the foundation for how they are building the forms on the revamp project now.**

## Wrap-up

## **Q37.** Do you have any questions for me? (Always prepare 2–3!)

**Your Answer:  i cant think of any can you generate a couple for me ?**

## Q38. **What is the difference between `props` and `state` in React?**

**Your Answer: Props are variables passed down from parent to child and are not able to be changed from with in the child you would need some sort of callback function. state is a variable that has a updater function that you get when you create a state variable. you can pass a state variable and state updater to a child anf the child component can use that that updater to manipulate the variable.**

## Q39. How does React handle reconciliation and the Virtual DOM?

**Your Answer: it makes a clone of VDOM and does a comparison and whatever is different it then replaces that in the current DOM**

## Q40. **What are React hooks, and why were they introduced?**

**Your Answer: they are actions that allow reusability and makes React more efficient in the way it works.**

## Q40. How would you optimize a React app for performance?

**Your Answer: i would use the hooks to store variables, functions or even entire components if needed by using React.memo for components, useMemo for variables, useCallback for functions.**

## What are the benefits of using TypeScript over JavaScript in a React project?

Your Answer: it allows you to use type safety whcih allows you to catch errors early on and reduces bugs that deal with typesafety prior to running the application

## **Q41. Can you explain the difference between `interface` and `type` in TypeScript?**

Your Answer: i cannot (chatgpt can you expalin this for me?)

## **Q41. How would you type a React component’s props and state in TypeScript?**

Your Answer: 

```ts
interface Props {
     name: String;
}

function Example({name}: Props) {
     const [age,setAge] = useState<number>(30);
     retrun (
         <p>the users name is {name} and they are {age} years old</p>
     )
}
```


## **Q41. What’s the difference between `O(n)`, `O(log n)`, and `O(1)` complexity? Can you give real-world examples?**

Your Answer: o(n) means that the time or space complexity is based on the number of values in a array (for example). o(1) means no matter the number of the values in a array the time or space will alway be constant. for o(log n) iam unsure how to expalin this one (chatGPT can you explain this one for me?)

## **Q41. What is the difference between synchronous and asynchronous code execution in JavaScript?**

Your Answer: synchronous means that the code executes line by line. asynchronus means that it can execute while other things are going on.
