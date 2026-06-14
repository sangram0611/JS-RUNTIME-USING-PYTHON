// Student grade processor
const students = [
    { name: "Alice", score: 92 },
    { name: "Bob",   score: 74 },
    { name: "Carol", score: 88 },
    { name: "Dave",  score: 61 },
    { name: "Eve",   score: 95 }
];

function getGrade(score) {
    if (score >= 90) return "A";
    if (score >= 80) return "B";
    if (score >= 70) return "C";
    return "F";
}

const results = students.map(s => ({
    name: s.name,
    grade: getGrade(s.score)
}));

const passed = students.filter(s => s.score >= 70);
const avg = students.reduce((acc, s) => acc + s.score, 0) / students.length;
const top = students.reduce((best, s) => s.score > best.score ? s : best);

console.log(results.map(r => r.name + ": " + r.grade).join(", "));
console.log(passed.length);
console.log(avg);
console.log(top.name);

// String manipulation
const names = students.map(s => s.name.toUpperCase());
console.log(names.join(" | "));

// Spread + sort
const scores = [...students].sort((a, b) => b.score - a.score);
console.log(scores[0].name);
console.log(scores[scores.length - 1].name);