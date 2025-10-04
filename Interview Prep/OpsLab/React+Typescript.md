### Day 1 – React + TypeScript Core

(Questions Only – No Answers Yet)

**1. What’s the difference between props and state in React? Why is one immutable and the other mutable?**

Answer: Props are passed from parent to child. while state is internal to the component. props are the ones that are immutable due to the actual variable being held in the parent component. but you could update the prop if the was a callback function that was passed as another prop to update the variable.

**2. Why do we pass a dependency array like `[count]` into `useEffect`? What happens if we omit it or use the wrong dependencies?**

Answer: we pass an depency array to useEffect because without it it would trigger the useEffect function everytime the UI re-renders. the dependency array allow you to say hey only  do this function if the dependency value changes. if you leave it blank though it will only trigger on the inital load of the component.

**3. Can you explain the difference between the Context API and Redux for state management? When would you choose one over the other?**

Answer: Context API is the React built in way of managing simple global state you could use it in components for forms for example. Redux is a more complicated but useful library for managing complex global state. this could be used for holding themes data that would persist across the whole site all the time.

**4. What’s the difference between controlled and uncontrolled inputs in React?**

Answer: controlled is where the data is managed with state by React. uncontrolled is when the data is managed by the DOM giving it control of how its stored.

**5. Why does React require keys in lists, and what issues can arise if keys are not used correctly?**

Answer: Keys in React are important because it creates uniqueness in List. without this it could  trigger issue with how React update the UI. without them it could cause the List to be updated/re-rendered unintentionally

**6. What are Error Boundaries in React, and when would you use them?**

Answer: Error Boundaries are to essential a fallback where if a component fails the user will se a component like "Sorry Somthing went wrong". its to gracefully handle errors that could crash the whole application

**7. What’s the difference between an interface and a type alias in TypeScript?**

Answer: interfaces are better with outlinning objects and allows you to merge interfaces together. type alias is better for things like unions since you are able to do that with type.

**8. Can you explain how Generics work in TypeScript, both for functions and React components?**

Answer: Generics are one of the best way to create reusable components and functions. it says hey this function can take in X as a type and x is what is passed when calling the function or component

**9. What are some common TypeScript utility types (Partial, Pick, Omit, Record) and when would you use each?**

Answer: some common utillity types are partial pick omit and record. partial would be used for if you wanted to make an interface all optional. pick would do as the name says and you pick which attributes you want to use or allow. omit is where you tell it which attirbutes you want to ignore or that you dont want to allow.  record is one that allows you to create an object out of a union type.

**10. Can you explain the difference between union types and intersection types in TypeScript?**

Answer: Union is saying that it can be any type that is provide when you create the union. intersection that a variable or object has attribute from more than one interface.

**11. What’s the difference between `any` and `unknown` in TypeScript? Why is `unknown` generally safer?**

Answer: any is like the get out of jail free card it allows you to escape typescript but should only  be used temporarily. unknown is also a way to accept any type but it is safer becasue it forces you to do a check first before using the variable.

**12. How do optional (`?`) and `readonly` modifiers work in TypeScript, and what are their use cases?**

Answer: optional says that it is not mandatory for this attribute to be used while readonly means that it can not be tampered with after intialization.  optional could be used for a object interface for a form saying that some attibutes of the object are required and some are optional. readonly could be used for example in some websites after creating your profile you can change the username that would be readonly

**13. What are React keys and why are they important?**

Anwser: React keys as in kys for list are ways to uniquely identify listem items without causing the Dom to have to creat it from scratch it can reuse pieces.

**14. What is the difference between `useMemo` and `useCallback`? When would you use one over the other?**

Answer: useMemo is for memoizing function results useCallback is to memoize a entire function. if the function has a large hefty calulation but you dont need that to rerender the function you can just use the useCallback, but if you just need to memoize the result then use useMemo

**15. What problem do React hooks solve compared to class components?**

Answer: (ChatGPT i need your help on this one please expalin this to me)

**16. How does TypeScript improve React code quality and developer experience?**

Answer: it allows a developer to catch issue eraly on instead of waiting for it to run then realize something is wrong. it also give much better error logs to find the root cause of the issue. it would allow a nother developer to jump in and see what is going on much easier then in normarl javascript. it also allows the use of code completion and suggestions.

**17. What’s the difference between interface merging and type aliasing in TypeScript?**

Answer: interface merging allows 2 or more interfaces to create a single one. type aliasing is saying that the type can be any of the types listed.
