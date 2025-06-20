### Challenge 1 (HARD)

```javascript
/**
   * You're assisting in the creation of an algorithm for a novel game where a character hops between 
two arrays following certain rules. The game starts at the first index (1-based) of an array, arrayA.

    The value at the character's current position in arrayA determines the index it jumps to on the second array, arrayB. Upon landing 
on arrayB, it does the same thing: the value at the current position specifies the index it jumps to in arrayA. This iteration 
continues until the character lands on an index in arrayA that it has already visited, at which point the game concludes.

    Your task is to develop a JavaScript function simulating this gameplay. The function receives two equal-length arrays of integers, 
arrayA and arrayB, each containing n elements (1 ≤ n ≤ 100). It should return an array consisting of the 1-based indices on arrayB 
that the character visited before a position on arrayA was repeated.

    Each element in the input arrays ranges from 1 to n, indicating the next 1-based index that the character will jump to in the other
array. The function guarantees that each jump always results in a valid position within the same-length arrays, and a position 
in arrayA will inevitably be revisited.

    Can you devise a function that proficiently simulates this gameplay?

    Example

    For arrayA = [1, 3, 2, 5, 4] and arrayB = [5, 4, 3, 2, 1] the output should be [1, 4, 3, 2, 5] since it first lands at the first 
position in arrayB (the resulting array is [1]), then goes to the fifth position in arrayA, then returns to the fourth position 
in arrayB (the resulting array becomes [1, 4]), etc.
  */


function solution(arrayA, arrayB) {
  
  console.log("ArrayA: ", arrayA);
  console.log("ArrayB: ", arrayB);

  let visited = new Set();
  let visitedInB = [];
  let index = 0;

  while (!visited.has(index)) {
    // start in arrayA
    visited.add(index);
    let posB = arrayA[index]

    visitedInB.push(arrayA[index]);
    index = arrayB[posB - 1] - 1;
    //go back to array using ArrayB index value -1
  }

  console.log(visitedInB);

  return visitedInB;
}

module.exports = { solution };
```

Notes :

Here’s what you can focus on to get stronger at these types of problems:

* **Indexing:** Practice converting between 0-based and 1-based indices. Many array problems require careful attention to this detail.
* **Simulation:** Get comfortable simulating step-by-step processes, especially when alternating between two structures (like arrays).
* **Tracking State:** Practice using sets or arrays to track what you’ve visited or seen before, and know when to stop a loop.
* **Tracing by Hand:** Before coding, walk through a small example on paper. Write down each step and see how the indices and values change.
* **Pattern Recognition:** Notice the repeating patterns in the problem (e.g., always jump from A to B, then B to A).

### Challenge 2 (EASY)

```javascript
/*
	You are provided with a list of n integers, where n ranges from 2 to 200, inclusive. The task is to return a list of pairs, each containing an integer and its reverse counterpart.

	In this context, the reverse counterpart of a number is the number with its digits reversed. For example, the reverse counterpart of 123 is 321.

	You must iterate through the list to find the reverse counterpart for each integer. If this reversed number exists in the list, create a pair with the original number and its reverse counterpart. If not, skip it.

	Your output should be a list of pairs with the original integers and their reverse counterparts. The integers in the given list will range from 10 to 9999, inclusive, and each integer in the list is unique.

	Note: The reverse counterpart of a single digit number is the same number. For numbers that result in leading zeros when reversed (e.g., 100 becomes 001, which is 1), consider only the integer value (i.e., 1). It's guaranteed that the original list will not contain integers with leading zeros.

	For example, for numbers = {12, 21, 34, 43, 56, 65}, the output should be solution(numbers) = {{12, 21}, {21, 12}, {34, 43}, {43, 34}, {56, 65}, {65, 56}}.
*/


function solution(numbers) {
    // TODO: implement solution here
  
    let reverseMatches = []
  
    numbers.forEach(num => {
        let currentNum = num;
        let reverseNum = parseInt(num.toString().split("").reverse().join(""));
  
        // console.log(`current Number: ${currentNum} | reverse Number: ${reverseNum}`);
  
        if (numbers.includes(reverseNum)) {
            reverseMatches.push([currentNum, reverseNum]);
        }
    });
  
    // console.log(`reverse Matches:`);
    // console.log(reverseMatches);
  
    return reverseMatches
  
}

module.exports = { solution };
```

### Challenge 3 (EASY)

```javascript
/*
You are given an array of n integers, where n ranges from 2 to 200, inclusive. The elements in the array range from -200 to 200, inclusive. Your task is to return an array where each element is the sum of a pair composed of an element and its 'opposite' element.

By 'opposite', we mean that in an array of n elements, the first and last elements are paired, the second and second-to-last elements are paired, and so on. If the array is of odd length, the middle element pairs with itself.

The method should handle both positive and negative integers and be capable of dealing with an odd number of elements in the list.

For example, given an input array [1, 2, 3, 4, 5], your method should return [6, 6, 6]. This is because the first element 1 plus the last element 5 equals 6, the second element 2 plus the second-to-last element 4 equals 6, and the middle element 3 plus itself equals 6.
*/

function solution(numbers) {
  // TODO: Implement solution here

  let n = numbers.length;
  let oppsums = [];

  for (let i = 0; i < n/2; i++) {
    let currentEl = numbers[i];
    let oppositeEl = numbers[n - i - 1];
  
    oppsums.push(currentEl + oppositeEl);
  }
  
  console.log(oppsums);
  
  return oppsums;
}

module.exports = { solution };
```

### Challenge 4 (EASY)

```javascript
/*
You are given an integer n where n ranges from 1 to 10^8, inclusive. Your task is to write a function that calculates and returns the product of the odd digits of n, without converting n into a string.

For example, if n equals 43172, the output should be 21, because the product of the odd digits 3, 1, and 7 is 21.

Please note that if n has no odd digits, your function should return 0.

You are expected to solve this task by using a while loop. Good luck!
*/

function solution(n) {
    // TODO: implement
    let oddSum = 0;
    let firstIteration = true;

    while (n > 0) {
        let digit = n % 10; // this grabs the last digit 
        if (digit % 2 !== 0) { // checks iff the digit is odd 
            if (firstIteration) {
                oddSum = digit;
                firstIteration = false;
            } else {
                oddSum = oddSum * digit; // multiples digit whats currently in oddSum
            }
        }
        n = Math.floor(n / 10); // removes the last digit
    }

    return oddSum;
}

module.exports = { solution };
```

### Challenge 5 (EASY)

```javascript
/*
Your task is to construct a function that accepts an integer n and returns the integer with the same digits as n, but in reverse order. You should implement your solution using a while loop.

For instance, if the input is 12345, the output should be 54321.

Keep in mind that n will always be a positive integer between 1 and 10^8.

Do not use built-in functions that convert the integer to another data type, such as a string, to reverse it. Solve the problem purely using mathematical operations and loop constructs. Note that when the result has leading zeros, you should consider only the integer value (e.g., 1230 becomes 321 after the operation).
*/

function solution(n) {
    // TODO: implement the solution here

    let reversedNum = 0;
  
    console.log(n);

    while (n > 0) {
        //grab the last digit
        let lastDigit = n % 10;
  
        console.log("digit: ", lastDigit);
  
        //add the last digit to the reversedNum var and multiply by 10 each time to get the place that number to the end essentially telling it what tenths place to put the number
        reversedNum = reversedNum * 10 + lastDigit;

        // remove the last number from n
        n = Math.floor(n / 10);
  
  
    }

    console.log(reversedNum);
  
    return reversedNum;
}

module.exports = { solution };
```

### Challenge 6 (EASY)

```javascript
/*
Your task is to implement a function that duplicates every digit in a given non-negative integer number, n. For example, if n equals 1234, the function should return 11223344.

To prevent possible integer overflow, it is guaranteed that n will be a non-negative integer that does not exceed 10^4. Solve this task without converting n into a string or performing any other type of casting. Your job is to work strictly with integer operations.

Keynote:
Focus on the essence of the problem, which is processing each digit of the number independently while maintaining the digit order. There is no need to look for mathematical patterns or clever simplifications; plain and straightforward processing will suffice. Utilize the toolbox of basic programming skills: loops, conditions, and mathematical operations. Good luck!
*/

function solution(n) {
    // TODO: Implement the solution

    let doubles = 0;
    console.log(n)
    let tenths = 1;

    while (n > 0) {
        // grab the first digit
        let lastDigit = n % 10;
  
        doubles += (lastDigit * tenths) ;
        tenths = tenths *10;
        doubles += (lastDigit * tenths) ;
  
        n = Math.floor(n/10);
  
        tenths = tenths *10;
    }
  
    return doubles
}

module.exports = { solution };
```

### Challenge 7 (EASY)

```javascript
/*
You are tasked with writing a function that takes a positive integer n, as an input and returns the number of consecutive equal digits in the number. Specifically, your function should identify pairs of digits in n that are equal and consecutive and return the count of these pairs. Note that only pairs of two consecutive equal digits should be counted, and larger groups should be considered as multiple pairs.

For instance, if n = 113224, it contains two groups of consecutive equal digits: 11 and 22. Therefore, the output should be 2. For n = 444, the output should also be 2, as there are two groups of 44 in this number.

In cases where no consecutive equal digits are found, the function should return 0. For example, if n = 13579 or n = 345672, the output should be 0 as there are no groups of consecutive equal digits in these numbers.

Keep in mind that n will be a positive integer ranging from 1 to 10^8, inclusive.

Note: You are not permitted to convert the number into a string or any other iterable structure for this task. You should work directly with the number.
*/


function solution(n) {
    // TODO: implement
    let consecDigits = 0;
    let prevNum = 0;
    let firstIteration = true;
    let tenths = 1;
  
    console.log("n: ", n);

    while (n > 0) {
        let currentDigit = n % 10;

        if (!firstIteration) {
            if (currentDigit === prevNum) {
                consecDigits++;
                tenths = tenths * 10;
            }
        } else {
            firstIteration = false;
        }
  
        prevNum = currentDigit;
        n = Math.floor(n / 10);
    }

    console.log(consecDigits);
    return consecDigits;
}

module.exports = { solution };
```

### Challenge 7 (EASY)

```javascript
/*
In this task, you are given a string composed of lowercase English alphabet letters ('a' to 'z'). The length of the string will range from 1 to 100 characters. Your challenge is to create a new string resulting from a unique order of character selection from the original string.

You need to develop a JavaScript function, function specialOrder(inputString), which takes inputString as an argument. The resulting string begins with the last character of the inputString, then selects the second-to-last character, continuing in reverse order until you reach the middle character of the string. Then, start with the first character of the inputString, proceed to the second character, and continue in this manner until you reach the middle character.

For example, if the inputString is "abcdefg", the function should return "gfedabc".

Keep in mind the following constraints while creating your function:

The input string contains only lowercase English letters ('a' to 'z').
The length of the input string is between 1 and 100, inclusive.
*/


function specialOrder(inputString) {
    // TODO: Implement function
    let splitString = inputString.split("");
    let n = splitString.length;
  
    let firstHalf = splitString.slice(0,n/2);
    let secondHalf = splitString.slice((n/2), n);
  
    let specialString = `${secondHalf.reverse().join("")}${firstHalf.join("")}`;

    return specialString;
}

module.exports = { specialOrder };
```

### Challenge 8 (EASY)

```javascript
/*
In this task, you are given a string s, and your goal is to produce a new string following a specific pattern. You are to take characters in sets of three, reverse the characters in each set, and then place them back into the string in their original positions, preserving the reverse order within each set. If 1 or 2 characters remain at the end (because the length of the string is not divisible by 3), they should be left as they are.

The string s contains only lowercase English letters, with its length ranging from 1 to 300, inclusive.

For example, if you are given the input 'abcdef', the output should be 'cbafed'. For the input 'abcdefg', your function should provide 'cbafedg'.
*/

function reversedTripleChars(s) {
    // TODO: Implement the function that reforms the string as described above

    let n = s.length;
    let num = 3;
    let i = 0
    let sArr = s.split("");

    console.log(s);

    let specialString = ""

    while (true) {

        let groups = sArr.slice(i, i + num);
        console.log(groups, " -- ", groups.length);

        if (groups.length === 3) {
            specialString += groups.reverse().join("");
        } else { specialString += groups.join(""); }
        i += num;
        if (i >= n) break;
    }

    console.log(specialString);
    return specialString;
}

module.exports = { solution: reversedTripleChars };
```

### Challenge 9 (EASY)

```javaScript
/*
You are provided with an array of n integers, where n can range from 1 to 200, inclusive. Your task is to create a new array that takes two pairs of 'opposite' elements from the original array at each iteration, starting from the center and moving towards both ends, to calculate the resulting multiplication of each pair.

By 'opposite' elements, we mean pairs of elements symmetrically located relative to the array's center. If the array's length is odd, the center element doesn't have an opposite and should be included in the result array as is.

Each element in the array can range from -100 to 100, inclusive.

For example, if the input array is [1, 2, 3, 4, 5], the returned array should be [3, 8, 5]. This is because the center element 3 remains as it is, the multiplication of 2 and 4 is 8, and the multiplication of 1 and 5 is 5.

*/


function solution(numbers) {
    // TODO: Implement the solution here.
  
    let n = numbers.length;
    let oppsProd = []
    let left, right;
    let mid = Math.floor(n/2);
  
    console.log(numbers);
  
    //check for even or odd
    if(n%2 === 1) {
        oppsProd.push(numbers[mid]);
        left = mid - 1;
        right = mid + 1;
    } else {
        left = mid - 1;
        right = mid;
    }
  
    while(left >=0 && right < n){
        let product = numbers[left--] * numbers[right++];
        oppsProd.push(product);
    } 
  
    console.log(oppsProd);
  
    return oppsProd;
  
}

module.exports = { solution };
```

### Challenge 10

```javascript
/*
You are given an array of n integers, where n can range from 1 to 500, inclusive. Your task is to create a new array in which each element is a string, determined by pairing elements from the middle to both ends of the original array.

If the original array has an odd length, pair the middle element with 0. If the original array has an even length, start pairing from the two middle elements. Continue the pairing by alternating elements from the left and the right until all elements have been paired.

After creating the paired elements, return the new array of pairs as strings. Ultimately, your result should be an array of strings, each representing a pair of integers separated by a space. Each element within a pair, as well as within the array, can range from -1000 to 1000, inclusive.

For example, if the input is numbers = [1, 2, 3, 4, 5], the output should be ["3 0", "2 4", "1 5"]. Similarly, if the input is numbers = [1, 2, 3, 4], the output should be ["2 3", "1 4"].
*/

function solution(numbers) {
    // TODO: Implement the function to pair the elements from the middle to ends of the array
  
    let n = numbers.length;
    let left, right;
    let mid = Math.floor(n/2);
    let pairArr = [];
    console.log(numbers);
  
    if (n%2 === 1) {
        pairArr.push(`${numbers[mid]} 0`);
        left = mid - 1;
        right = mid + 1;
    } else {
        left = mid - 1;
        right = mid;
    }
  
    while(left >= 0 && right <= n) {
        pairArr.push(`${numbers[left--]} ${numbers[right++]}`);
    }
  
    console.log(pairArr);
  
    return pairArr;
  
}

module.exports = { solution };
```

### Challenge 11 (MEDIUM)

```javascript
/*
You are provided with an array of n integers, where n ranges from 1 to 500 and is always an odd number. The elements of the array span values from 
− 10^6 to 10^6, inclusive. The goal is to return a new array constructed by traversing the initial array in a specific order, outlined as follows:

Begin with the middle element of the array.
For each subsequent pair of elements, alternate between taking two elements from the left and two elements from the right, relative to the middle. Take those two elements and place it to the back of the newly constructed array preserving the order of the elements in the pair.
If fewer than two elements remain on either side, include all the remaining elements from that side.
Continue this process until all elements of the array have been traversed.
For example, for array = [1, 2, 3, 4, 5, 6, 7], your function should return [4, 2, 3, 5, 6, 1, 7]. And for array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], your function should return [6, 4, 5, 7, 8, 2, 3, 9, 10, 1, 11].
*/


function unusualTraversal(array) {
    // TODO: implement this function

    let n = array.length;
    let newArr = [];
    let right, left;
    let mid = Math.floor(n / 2);
    console.log("array ",array);

    if (n % 2 === 1) {
        newArr.push(array[mid]);
        right = mid + 1;
        left = mid - 1;
    } else {
        right = mid;
        left = mid - 1;
    }

    while (left >= 0 && right <= n) {
        if(array[left-1]) {
            newArr.push(array[left-1]);
            newArr.push(array[left]);
            left-=2;
        } else {
            newArr.push(array[left--]);
        }
  
        if(array[right+1]) {
            newArr.push(array[right]);
            newArr.push(array[right+1]);
            right+=2;
        } else {
            newArr.push(array[right++]);
        }
  
    }

    console.log(newArr);
    return newArr;
}

module.exports = { unusualTraversal };
```

### Challenge 12 (MEDIUM)

```javascript
/*
In this task, you are to write a JavaScript function that implements the concept of Run-Length Encoding (RLE) on an alphanumeric input string. Run-length encoding is a simple form of data compression where sequences of data entities that are the same are stored as a single data entity along with its count. Each count must immediately follow the character it is associated with.

Your function's name should be encodeRLE. It takes a string as an input argument and returns a new string that represents the input's run-length encoding.

Your function should operate only on alphanumeric characters (numbers 0-9 and uppercase and lowercase letters A-Z, a-z). For any other types of characters in the string, simply ignore them and do not include them in the final encoded output.

For instance, if the input string is "aaabbcccdde", the output should be "a3b2c3d2e1". If the input string includes non-alphanumeric characters, such as "aaa@@bb!!c#d**e", the output should be "a3b2c1d1e1".

We assume that the given input string could have up to 500 characters.
*/

function encodeRLE(s) {
    // TODO: implement
  
    let groups = [];
    let currentGroupChar = "";
    let currentGroupCount = 0;
    let n = s.length;
  
    for(let i = 0; i < n; i++) {
        let char = s[i];
  
        if(/^[a-zA-Z0-9]$/.test(char)) {
            if (char === currentGroupChar) {
                currentGroupCount++;
            } else {
                if (currentGroupChar !== "") {
                    groups.push(`${currentGroupChar}${currentGroupCount}`);
                }
                currentGroupChar = char;
                currentGroupCount = 1;
            }
        }
    }
  
    if (currentGroupChar !== "") {
        groups.push(`${currentGroupChar}${currentGroupCount}`);
    }
  
    return groups.join("");
  
}

module.exports = { solution: encodeRLE };
```

### Challenge 13

```javascript
/*
Your task is to write a JavaScript function that takes in a string and identifies all the consecutive groups of identical characters within it, with the analysis starting from the end of the string rather than from its beginning. A group is defined as a segment of the text where the same character is repeated consecutively.

Your function should return an array of strings. Each string will consist of the repeating character and the number of its repetitions separated by a space. For instance, if the input string is "aaabbcccdde", the function should output: [ "e 1", "d 2", "c 3", "b 2", "a 3" ].

Note that the input string cannot be empty; in other words, it must contain at least one character, and its length must not exceed 500 characters. The return should also be in reverse order, starting from the group of repeated characters at the end of the string and moving backward.

Also note that unlike the previous exercise, this task requires you to consider every character in the string, including symbols.
*/

function solution(s) {
    // TODO: implement the algorithm to find consecutive groups of characters in the reverse order

    let groups = []; //create the array to hold the groups
    let currentChar = ""; // create the var that holds the current charbeing looked at
    let currentCharCount = 0; // create the var that holds the char count

    let reversedS = s.split("").reverse().join("");
    let n = reversedS.length; // length of the string

    for (let i = 0; i < n; i++) {
        let char = reversedS[i];
  
        // check of char is the same as the current character being counted
        if(char === currentChar) {
            currentCharCount++;
        } else { 
            // once no more of the same chars are found check if current char group is not empty if so push to the groups array 
            if(currentChar !== "") {
                groups.push(`${currentChar} ${currentCharCount}`);
            }
  
            //set the currentchar to the new char being checked and count to 1
            currentChar = char;
            currentCharCount = 1;
        }
    }
  
    //make sure to add the remining sinle char if any
    if (currentChar !== "") {
        groups.push(`${currentChar} ${currentCharCount}`);
    }
  
    return groups;
}

module.exports.solution = solution; 
```

### Challenge 14

```javascript
/*
In this task, you are required to write a JavaScript function that takes a string as input and identifies all consecutive groups of identical pairs of characters within it. A group can be defined as a segment of the text where the same pair of characters is repeated consecutively.

Your function should return a string representing all the repeating character pairs and the number of their repetitions. For instance, if the input string is "aaabbabbababaca", your function should output: "aa1ab1ba1bb1ab2ac1a1". Note that if the length of the input string is odd, the last character is not paired with any other and is just added to the resulting string with repetition count 1.

The length of the string will not exceed 500 characters.
*/

function solution(s) {
    // TODO: Implement the function here

    let groups = [];
    let currentSegGroup = "";
    let currentSegGroupCount = 0;

    let n = s.length;
    console.log(s);

    for (let i = 0; i < n; i += 2) {
        let seg
        seg = s[i];
        if (s[i + 1] !== undefined) {
            seg += s[i + 1];
        }

        if (currentSegGroup === seg) {
            currentSegGroupCount++;
        } else {
            if (currentSegGroup !== "") {
                groups.push(`${currentSegGroup}${currentSegGroupCount}`);
            }

            currentSegGroup = seg;
            currentSegGroupCount = 1;
        }
    }

    if (currentSegGroup !== "") {
        groups.push(`${currentSegGroup}${currentSegGroupCount}`);
    }
  
    return groups.join("");
}

module.exports = { solution };
```

### Challenge 15

```javascript
/*
You are given a string of n characters, with n varying from 1 to 1000, inclusive. Your task is to write a JS function that takes this string as input, applies the following operations, and finally returns the resulting string.

Split the given string into individual words, using a space as the separator.
Convert each word into a list of its constituent characters, and shift each list of characters once to the right (with the last element moving to the first position).
After the rotations, reassemble each word from its list of characters.
Join all the words into a single string, separating adjacent words with a single space.
Return this final string as the function's output.
The constraints for the problem are as follows:

The input string will neither start nor end with a space, nor will it have multiple consecutive spaces.
Each word will contain only alphabets and digits, and its length will range from 1 to 10.
The words are case-sensitive; for example, 'word' and 'Word' are considered distinct.
Your program should output a single string with the words rotated by their lengths while preserving their original order.

As an illustration, consider the input string "abc 123 def". Applying the stated operations results in the output "cab 312 fde".
*/

function solution(s) {
    // TODO: Implement the solution here

    let words = s.split(" ");

    let specialString = words.map((item, index) => {
        let newItem = item.split("");
        let returnArr = [];
        for (let i = 0; i < newItem.length; i++) {
            if (i === 0) {
                returnArr.push(newItem[newItem.length - 1]);
            } else returnArr.push(newItem[i-1]);
        }
        return returnArr.join("");
    })

    console.log(specialString.join(" "));
    return specialString.join(" ");
}

module.exports = { solution };


// ------------------- ALTERNATIVE WAY ------------------

function solution(s) {
    let words = s.split(" ");

    let specialString = words.map((item, index) => {
	// first part > grabs the last and puts it first  
	//last part > grabs the indexs 0 to the second to last excluding the last so it will not grab the last index 
        return item.slice(-1) + item.slice(0, -1); 
    })

    console.log(specialString.join(" "));
    return specialString.join(" ");
}

module.exports = { solution };
```

### Challenge 16

```javascript
/*
Given a string consisting of words separated by whitespace, your task is to write a function that accepts this string. It then replaces each character in the words with the corresponding character opposite in the English alphabet and stitches them all together to form a new string.

Here's what you need to consider:

The input string will include between 1 and 100 words.
A word is composed of characters ranging from a to z or A to Z. So, if a word contains a lowercase 'a', for instance, it should be replaced with 'z', 'b' with 'y', 'c' with 'x', and so on, maintaining the same case. For words with an uppercase 'A', it should be replaced with 'Z', 'B' with 'Y', 'C' with 'X', and so forth, while preserving the uppercase.
The given string will not start or end with a space, and there will be no occurrence of double spaces.
After transforming the characters of the words, form a new string by taking the last word first and appending the remaining words in their original order, each separated by spaces.
Note: The opposite letter mappings are as follows: a ↔ z, b ↔ y, c ↔ x, ..., m ↔ n, n ↔ m, ..., x ↔ c, y ↔ b, z ↔ a. The mapping is case-sensitive.

Example

For the input string "CapitaL letters", the output should be "ovggvih XzkrgzO".
*/

function solution(inputStr) {
    // TODO: implement the string transformation function

    let splitInputStr = inputStr.split(" ");
    let reverseStrings = splitInputStr.reverse();
    console.log("OG: ", inputStr);
    console.log("reverseStrings: ",reverseStrings);

    let encryptedWords = reverseStrings.map(word => {
        let splitRevWord = word.split("");
  
        let encryptedChars = splitRevWord.map(char => {
            let charCode = char.charCodeAt(0)
            let oppChar;

            if (/^[a-z]$/.test(char)) {
                oppChar = String.fromCharCode(219 - charCode);
                // console.log(`--LowerCase char--`);
                // console.log(`${char} -> ${oppChar}`);
            }
  
            if (/^[A-Z]$/.test(char)) {
                oppChar = String.fromCharCode(155 - charCode);
                // console.log(`--UpperCase char--`);
                // console.log(`${char} -> ${oppChar}`);
            }
            return oppChar;
        });
  
        return encryptedChars.join("");
    });
  
    encryptedWords.reverse();
  
    let lastIndexVal = encryptedWords[encryptedWords.length -1];
    encryptedWords.splice(encryptedWords.length-1,1);
    encryptedWords.splice(0,0, lastIndexVal);
  
    console.log(encryptedWords);
    return encryptedWords.join(" ");
}

module.exports = { solution };
```

### Challenge 17 (EASY)

```javascript
/*
You are given a string filled with words. Your task is to write a JavaScript function that takes this string as input. Your function should then capitalize the first letter of each word while making the rest of the letters lowercase. Finally, it should recombine the words into a new string where every word starts with a capital letter.

Here's what to keep in mind:

The input string will contain between 1 and 100 words.
Each word is a sequence of characters separated by white space.
Words consist of characters ranging from a to z, A to Z, 0 to 9, or even an underscore _.
The provided string will not start or end with a space, and it will not contain double spaces.
After capitalizing the first character of each word and converting the rest to lowercase, the program should return a single string in which the words maintain their original order.
If the first character of a word is not a letter (like a number or an underscore), keep that first character as is, but still make the rest of the characters lowercase.
Ignore cases where punctuation marks are attached to words (such as "Hello," or "world!"). Punctuation attached to words should not prevent the word from being capitalized based on the given rules.

Example

For the input string "SoME rAndoM _TeXT", the output should be "Some Random _text".
*/

function solution(inputStr) {
    // TODO: implement the function

    let splitInputStr = inputStr.split(" ");

    let cammelCaseString = splitInputStr.map((word) => {
        let splitWord = word.split("");

        let cCWord = splitWord.map((char, index) => {
            if (index === 0) {
                return char.toUpperCase()
            } else return char.toLowerCase();
        })
  
        return cCWord.join("");
    })

    console.log(cammelCaseString.join(" "));
    return cammelCaseString.join(" ");
}

module.exports = { solution };
```

### Challenge 18 (EASY-MEDIUM)

```javascript
/*
Let's imagine you are given a string that contains a series of words separated by a hyphen ("-"). Each word in the string can be a lowercase letter from 'a' to 'z' or a set of digits representing a number from 1 to 26. Your task is to parse this string and swap the type of each word: convert numbers into their corresponding English alphabet letters, and letters into their numerical equivalents. This means '1' should convert to 'a', and 'a' should convert to '1'.

You need to return a new string with the converted words, rejoined with hyphens.

Ensure you maintain the original order of the words from the input string in your output string.

The input string's length should range from 1 to 1000 for this exercise. The string will never be empty, always containing at least one valid lowercase letter or numerical word.

Remember, the transformation of words should be limited to converting numbers from 1 to 26 into their corresponding letters from 'a' to 'z', and vice versa.

Example

For the input string "1-a-3-c-5", the output should be "a-1-c-3-e".
*/

function solution(s) {
    // TODO: Implement the function that could solve the task
    let alphabetStartPosition = "a".charCodeAt(0);
    let alphabetEndPosition = "z".charCodeAt(0);

    let newStringArr = [];
    let numberStr = "";
    // newString += String.fromCharCode(alphbetStartPostion + parseInt(char) - 1);

    let sSplit = s.split("-");
  
    console.log("----- s: ",s);

    sSplit.forEach(item => {
        let isNotNumber = isNaN(item);
  
        if (!isNotNumber) {
            newStringArr.push(String.fromCharCode(alphabetStartPosition + parseInt(item) - 1));
        } else {
            newStringArr.push(26- alphabetEndPosition + item.charCodeAt(0));
        }
    })
  
    console.log("-output: ", newStringArr.join("-"));
    return newStringArr.join("-");
}

module.exports = { solution };
```

### Challenge 19 (MEDIUM)

```javascript
/*
You are given a string s of length n, with n ranging from 1 to 500 inclusive. This string represents the complex and jumbled record of a sports game. It combines player names and scores but lacks a uniform structure. The player names consist of words made up of lowercase English alphabets (a-z), while the scores are integers ranging from 1 to 100 inclusive.

Your mission involves writing a JavaScript function function parseAndSumScores(s) {}. This function should parse the given string, isolate the integers representing player scores, and return the sum of these scores.

For instance, for the input string, "joe scored 5 points, while adam scored 10 points and bob scored 2, with an extra 1 point scored by joe", your function should return the sum 5 + 10 + 2 + 1, which totals 18.
*/

function parseAndSumScores(s) {
    // TODO: implement
  
    let scores = [];
    let score = "";
    let scoreTotal = 0;
    console.log(s);
    for(let char of s) {
        if(!isNaN(char) && char !== " "){
            score += char;
        } else if (char !== "" && score !== "") {
            scores.push(parseInt(score));
            score = "";
        }
    }
  
    if (score !== "") {
        scores.push(parseInt(score));
    }
  
    console.log(scores);
  
  
    scores.forEach(item => {
        scoreTotal += item;
    }) 
  
    console.log(scoreTotal);
    return scoreTotal;
}

module.exports = { parseAndSumScores };
```

### Challenge 20 (MEDIUM)

```javascript
You are provided with a string of alphanumeric characters in which each number, regardless of the number of digits, is always followed by at least one alphabetic character before the next number appears. The task requires you to return a transformed version of the string wherein the first alphabetic character following each number is moved to a new position within the string and characters in between are removed.

Specifically, for each number in the original string, identify the next letter that follows it, and then reposition that character to directly precede the number. All spaces and punctuation marks between the number and the letter should be removed.

The length of the string s ranges from 3 to 10^6 (inclusive), and the string contains at least one number. The numbers in the string are all integers and are non-negative.

Here is an example for better understanding:

Given the string:

"I have 2 apples and 5! oranges and 3 grapefruits."

The function should return:

"I have a2pples and o5ranges and g3rapefruits."

In this instance, the character 'a' following the number 2 is moved to come before the 2, the 'o' succeeding the 5 is placed before the 5, and the 'g' subsequent to the 3 is repositioned to precede the 3. Punctuation marks and spaces are disregarded as they are not alphabetic characters.

Please note that the operation should maintain the sequential order of the numbers and the rest of the text. Considering this, the task is not solely about dividing a string into substrings but also about modifying them. This will test your expertise in Java string operations and type conversions./*

*/

function solution(input) {
    // TODO: implement your solution here
    // split the sting up into parts 
    // see waht part is a number then add the number to the following part 
    // make sure the following part has the number come after the first character
    // finally convert to a sting again

    let splitString = input.split(" ");
    let number = ""
    let newString = "";

    console.log(input);

    for (let i = 0; i < input.length; i++) {
        if(!isNaN(input[i]) && input[i] !== " "){
            while(true) {
                if (/^[a-zA-Z]$/.test(input[i])) {
                    newString += input[i] + number;
                    number = ""
                    break;
                } else if (!isNaN(input[i]) && input[i] !== " "){
                    number += input[i];
                }
                i++;
            }  
        } else{
            newString += input[i];   
        }
    }
    console.log(newString);
    return newString;
}

module.exports.solution = solution;
```

### Challenge 21 (EASY-MED)

```javascript
/*
You are given two input arguments: a list of strings timePoints and an integer addedSeconds. Each string in timePoints is in the format "HH:MM:SS", representing a valid time from "00:00:00" to "23:59:59" inclusive. The integer addedSeconds represents a number of seconds, ranging from 1 to 86,400. Your task is to create a new function, addSecondsToTimes(timePoints, addedSeconds), which takes these two arguments and returns a new list of strings. Each string in the returned list is the new time, calculated by adding the provided addedSeconds to the corresponding time in timePoints, formatted in HH:MM:SS.

The list timePoints contains n strings, where n can be any integer from 1 to 100 inclusive. The time represented by each string in timePoints is guaranteed to be valid. The total time, after adding addedSeconds, can roll over to the next day.

Example

For timePoints = ['10:00:00', '23:30:00'] and addedSeconds = 3600, the output should be ['11:00:00', '00:30:00'].
*/

function addSecondsToTimes(timePoints, addedSeconds) {
  // TODO: implement the function
  
  console.log("TimePoints: ", timePoints);
  console.log("addedSeconds: ", addedSeconds);
  
  let newTimePoints = [];
  
  timePoints.forEach(timePoint => {
    let splitTimePoint = timePoint.split(":");
  
    let totalSeconds = 0;
    let hours = parseInt(splitTimePoint[0]);
    let mins = parseInt(splitTimePoint[1]);
    let secs = parseInt(splitTimePoint[2]);
  
  
    totalSeconds = (hours * 60 * 60) + (mins * 60) + secs;
  
    console.log("total Seconds: ", totalSeconds);
  
    totalSeconds = (totalSeconds + addedSeconds) % (24 * 60* 60);
   
    let newHours = Math.floor(totalSeconds / (60 * 60));
    totalSeconds %= (60*60);
    let newMins = Math.floor(totalSeconds / 60);
    let newSecs = totalSeconds %= 60;
  
    newTimePoints.push(`${String(newHours).padStart(2,'0')}:${String(newMins).padStart(2,'0')}:${String(newSecs).padStart(2,'0')}`);
  });
  
  
  console.log(newTimePoints);
  return newTimePoints;
  
}

module.exports = { addSecondsToTimes };
```

### Challenge 22

```javascript
/*
You are given a time period formatted as a string in the HH:MM:SS - HH:MM:SS format. HH:MM:SS represents the time in hours, minutes, and seconds form, and the hyphen (-) separates the start time from the end time of the period.

Your task is to calculate how many minutes pass from the start time until the end time.

Here are some guidelines:

The input times are always valid time strings in the HH:MM:SS format, with HH ranging from 00 to 23, and MM and SS from 00 to 59.
The output should be an integer, representing the total length of the time period in minutes.
The start time of the period will always be earlier than the end time, so periods that cross over midnight (like 23:00:00 - 01:00:00) are not considered.
We are interested in the number of times the time passes some HH:MM:00 after the start time until the end time. Any remaining seconds should be disregarded; for instance, a period of "12:15:00 - 12:16:59" represents 1 minute, not 2, and a period of "12:14:59 - 12:15:00" also represents 1 minute.
Your function should look like this:

function timePeriodLength(timePeriod) {
  // Your implementation goes here
}

Where timePeriod is a string formatted as HH:MM:SS - HH:MM:SS. The function should return a single integer that represents the total length of the specified time period in minutes.

Example:

timePeriodLength("12:15:30 - 14:00:00");
// should return 105
*/

function timePeriodLength(timePeriod) {
  // TODO: implement the function
  console.log(timePeriod);
  
  let timePeriods = timePeriod.split(" - ");
  console.log(timePeriods);
  
  let startTimeMins= 0;
  let endTimeMins = 0;
  
  for(let i = 0; i<timePeriods.length; i++) {
    let timeInMins = 0;
    let timeSplit = timePeriods[i].split(":");
  
    let hoursM = parseInt(timeSplit[0]) * 60;
    let mins = parseInt(timeSplit[1]);
  
    timeInMins += hoursM + mins;
   
    i === 0 ? startTimeMins = timeInMins : endTimeMins = timeInMins 
  }
  
  let minuteMarks = (endTimeMins) - (startTimeMins);
  
  console.log("minuteMarks:", minuteMarks);
  
  
  return minuteMarks;
  
}

module.exports = { solution: timePeriodLength };
```
