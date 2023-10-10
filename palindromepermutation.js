
function isPermutationOfPalindrome(str) {
    const charCount = {};
    const formattedStr = str.toLowerCase().replace(/\s/g, '');

    for (const char of formattedStr) {
        charCount[char] = (charCount[char] || 0) + 1;
    }

    let oddCount = 0;

    for (const count of Object.values(charCount)) {

        if (count % 2 !== 0) {
            oddCount++;

            if (oddCount > 1) {
                return false;
            }
        }
    }

    return true;
}

// Should be true
console.log(isPermutationOfPalindrome("tacocat"));
console.log(isPermutationOfPalindrome("T a c t Coa"));
console.log(isPermutationOfPalindrome("taCocat"));
console.log(isPermutationOfPalindrome("OOv"));

// Should be false
console.log(isPermutationOfPalindrome("not a palindrome"));
console.log(isPermutationOfPalindrome("ha ppy"));
console.log(isPermutationOfPalindrome("Bree A"));
