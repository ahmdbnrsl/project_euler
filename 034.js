"use strict";
function pentagon(n) {
    return (n * (3 * n - 1)) / 2;
}
function generateDictionaryPentagon(initialIndex, endIndex) {
    const dictionary = [];
    const firstIndex = initialIndex;
    while (initialIndex <= firstIndex + endIndex) {
        const pentagonNumber = pentagon(initialIndex);
        dictionary.push(pentagonNumber);
        initialIndex++;
    }
    return dictionary;
}
function checkPentagon(a, b) {
    return [a, b, a + b, Math.abs(a - b)].every(item => dictionaryPentagon.includes(item));
}
const dictionaryPentagon = generateDictionaryPentagon(1, 1000);
const currentElement = [];
let lowestDifferencePentagon = null;
for (let i = 0; i < dictionaryPentagon.length; i++) {
    let lowest = false;
    for (let j = 0; j < dictionaryPentagon.length; j++) {
        if (currentElement.includes(i + j + Math.abs(i - j)))
            continue;
        if (!lowestDifferencePentagon &&
            i + j >= (dictionaryPentagon.length - 1) * 2) {
            dictionaryPentagon.push(...generateDictionaryPentagon(j + 2, 1000));
        }
        const a = dictionaryPentagon[i];
        const b = dictionaryPentagon[j];
        const isPentagon = checkPentagon(a, b);
        if (!isPentagon)
            continue;
        const difference = Math.abs(a - b);
        if (difference <= (lowestDifferencePentagon || difference)) {
            lowestDifferencePentagon = difference;
            lowest = true;
            break;
        }
        currentElement.push(i + j + Math.abs(i - j));
    }
    if (lowest)
        break;
}
console.log(lowestDifferencePentagon);
