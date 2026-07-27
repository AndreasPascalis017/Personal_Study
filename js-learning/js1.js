//don't forget to add ; mark
// we use seperate script file to make it a cleaner environment and easier access
// we can execute script using command prompt by going to the file location and run the command
console.log('Hello World');
// to declare a variable use let

let name = 'Andreas'; //using single quote '' is more common in javascript (but using " " is fine)
console.log(name);

// Rules of naming variables
// 1. cannot be a reserved keyword (let, if, else, var, etc)
// 2. The name should be meaningful
// 3. cannot start with a number
// 4. cannot contain a space or hyphon (-)
// 5. variable names are case sensitive.

// let firstName; This format is called camel notation where the second word in capital
// let Firstname; these two are different variables

// let firstName = "Andreas", lastName = "Tristan"; this is not wrong
// But this is the more modern way.
let firstName = "Andreas";
let lastName = "Tristan";

// let interestRate = 0.3;
// interestRate = 1;
// console.log(interestRate);

// There are situations where we don't want the variable's value to change
// this is where we use costant.

const interestRate = 0.3; // Constant locked the value of our assign value.
// interestRate = 1;
console.log(interestRate);

// There are 2 categories of types
// 1. primitive/ value types (String, Number, Boolean, Undefined, and Null)
// 2. reference types

// The list below are examples of primitive types
// let name = "Andreas";  String Literal
// let age = 30; Number Literal
// let isApproved = true; Boolean Literal
// let firsName; if we don't initialize it, it will be undefined by default or we can still assign undefined on it.
// let lastName = null; is used when we wanted to explicitly clear the value of  a variable
// let selectedColor = null;

// Javascript are dynamic languages
// Static means when we assign a value it cannot be change
// dynamic means the opposite.
// ctrl + l to clear the browser console.
// JavaScript do not have integer or float only number

let age = 30;
let isApproved = true; // in Javascript boolean is type with all lower case.
let selectedColor = null;

// Reference Types
// consists:
// Object = used to encompass multiple related variable meant to make a cleaner code.
// Array
// Function

// In object use : instead of = to assign a value.
let person = {
    name: 'Andreas',
    age: 30
}; // Object Literal

// There 2 ways to change its properties
// 1. Dot notation (object.properties = ...)
person.name = 'Vilvo';
// 2. Bracket notation (obejct[properties] = ...)
person['name'] = 'Mary';

console.log(person.name);

// Arrays
let selectedColors = ['red', 'blue']; // [] is an empty array
console.log(selectedColors); // array index started at 0 
selectedColors[0] = 'green'; // one way to change its value
selectedColors[2] = 100; // one way to add an array
console.log(selectedColors);
console.log(selectedColors.length);

// in Javascript an array isn't locked to one specific types. it can be consist of multiple different types
// Functions

// This is a function that performing a task
function greet(name, lastName) {
    console.log('Hello ' + name + ' ' + lastName);
} // function do not have to be end with ; because we are not declaring it like a variable

greet('Andreas', 'Pascalis'); // remember name here is called a parameter while 'Andreas' is called an argument
greet('Bill'); // assuming you don't assign the second parameter by default it'll be undefined

// Types of functions
// Calculate a value

function square(number) {
    return number * number;
}

console.log(square(5));