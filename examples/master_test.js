// 1. Variables + coercion
let a = "10";
let b = 5;
console.log(a + b);
console.log(Number(a) + b);

// 2. Loop sum
let sum = 0;
for (let i = 1; i <= 5; i++) {
    sum += i;
}
console.log(sum);

// 3. Function
function square(x) {
    return x * x;
}
console.log(square(6));

// 4. Arrow function
const add = (x, y) => x + y;
console.log(add(3, 7));

// 5. Array
let arr = [1, 2, 3];
console.log(arr);

// 6. String
let str = "thunder";
console.log(str.toUpperCase());

// 7. Boolean
console.log(true && false);

// 8. Undefined
let x;
console.log(x);