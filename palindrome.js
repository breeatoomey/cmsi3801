
class LinkedList {

    constructor(next, data) {
        this.data = data;
        this.next = next;
    }

    append(data) {
        let tail = new LinkedList(null, data);
        let current = this;

        while (current.next !== null) {
            current = current.next;
        }

        current.next = tail;
    }
}

function isPalindrome(head) {
    let current = head;
    let reversed = reverseLinkedList(head);

    for (i = 0; i < reversed.length; i++) {

        if (current.data !== reversed.pop()) {
            return false;
        }

        current = current.next;
    }

    return true;
}

function reverseLinkedList(head) {
    let current = head;
    let stack = [];

    while (current !== null) {
        stack.push(current.data);
        current = current.next
    }

    return stack;
}

// should return false
let notPalindrome1 = new LinkedList(null, "a");
notPalindrome1.append("b");
notPalindrome1.append("c");

let notPalindrome2 = new LinkedList(null, "h");
notPalindrome2.append("e");
notPalindrome2.append("l")
notPalindrome2.append("l")
notPalindrome2.append("o")

console.log(isPalindrome(notPalindrome1)); 
console.log(isPalindrome(notPalindrome2)); 

// should return true
let isPalindrome1 = new LinkedList(null, "a");
isPalindrome1.append("b");
isPalindrome1.append("a");

let isPalindrome2 = new LinkedList(null, "m");
isPalindrome2.append("o");
isPalindrome2.append("m");

console.log(isPalindrome(isPalindrome1)); 
console.log(isPalindrome(isPalindrome2)); 