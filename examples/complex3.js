const person = {
    name: "Alice",
    age: 25,
    greet: function () {
        return "Hi, I'm " + this.name;
    }
};

console.log(person.name);
console.log(person["age"]);
console.log(person.greet());

person.city = "Delhi";
person.age = 26;
console.log(person.city);
console.log(person.age);
console.log(Object.keys(person).length);

const person2 = { ...person, name: "Bob" };
console.log(person2.name);
console.log(person2.age);
console.log(person2.city);