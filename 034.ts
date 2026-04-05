function pentagon(n: number): number {
    return (n * (3 * n - 1)) / 2;
}

function generateDictionaryPentagon(
    initialIndex: number,
    endIndex: number
): Array<number> {
    const dictionary: Array<number> = [];
    const firstIndex: number = initialIndex;

    while (initialIndex <= firstIndex + endIndex) {
        const pentagonNumber: number = pentagon(initialIndex);
        dictionary.push(pentagonNumber);
        initialIndex++;
    }

    return dictionary;
}

function checkPentagon(a: number, b: number): boolean {
    return [a, b, a + b, Math.abs(a - b)].every(item =>
        dictionaryPentagon.includes(item)
    );
}

const dictionaryPentagon: Array<number> = generateDictionaryPentagon(1, 1000);
const currentElement: Array<number> = [];
let lowestDifferencePentagon: number | null = null;

for (let i: number = 0; i < dictionaryPentagon.length; i++) {
    let lowest: boolean = false;
    for (let j: number = 0; j < dictionaryPentagon.length; j++) {
        if (currentElement.includes(i + j + Math.abs(i - j))) continue;
        if (
            !lowestDifferencePentagon &&
            i + j >= (dictionaryPentagon.length - 1) * 2
        ) {
            dictionaryPentagon.push(...generateDictionaryPentagon(j + 2, 1000));
        }

        const a: number = dictionaryPentagon[i];
        const b: number = dictionaryPentagon[j];

        const isPentagon: boolean = checkPentagon(a, b);
        if (!isPentagon) continue;

        const difference: number = Math.abs(a - b);
        if (difference <= (lowestDifferencePentagon || difference)) {
            lowestDifferencePentagon = difference;
            lowest = true;
            break;
        }
        currentElement.push(i + j + Math.abs(i - j));
    }
    if (lowest) break;
}

console.log(lowestDifferencePentagon);
