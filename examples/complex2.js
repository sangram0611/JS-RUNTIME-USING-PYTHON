const d = new Date(2024, 0, 15);   // Jan 15, 2024 (month is 0-indexed)

console.log(d.getFullYear());
console.log(d.getMonth());          // 0 = January
console.log(d.getDate());
console.log(d.getDay());            // 1 = Monday

const now = new Date();
console.log(typeof now.getTime());
console.log(now instanceof Date);
console.log(now.getTime() > 0);