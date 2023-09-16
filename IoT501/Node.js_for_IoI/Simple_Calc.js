#!/usr/bin/node
const readline = require('readline');
const calc = {
  num1: null,
  num2: null,
  add: () => calc.num1 + calc.num2,
  sub: () => calc.num1 - calc.num2,
  mul: () => calc.num1 * calc.num2,
  div: () => {
    if (calc.num2 === 0) { return 'Division by zero is not allowed'; }
    return calc.num1 / calc.num2;
  }
};
const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
r1.question('Enter the first number: ', (num1) => {
  r1.question('Enter the second number: ', (num2) => {
    r1.question('Enter the op: ', (op) => {
      calc.num1 = parseFloat(num1);
      calc.num2 = parseFloat(num2);
      if (!isNaN(calc.num1) && !isNaN(calc.num2)) {
        switch (op) {
          case '+':
            console.log(calc.add());
            break;
          case '-':
            console.log(calc.sub());
            break;
          case '*':
            console.log(calc.mul());
            break;
          case '/':
            console.log(calc.div());
            break;
        }
      } else { console.log('Invalid input. Please Enter valid numbers.'); }
      r1.close();
    });
  });
});
