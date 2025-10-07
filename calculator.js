const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function ask(question) {
  return new Promise(resolve => rl.question(question, answer => resolve(answer)));
}

async function calculator() {
  while (true) {
    console.log("----------CALCULATOR----------");

    const a = parseFloat(await ask("Write first number: "));
    const b = parseFloat(await ask("Write second number: "));
    const islem = await ask("Select the action you want to perform (+, -, *, /): ");

    if (islem === "+") {
      console.log("result:", a + b);
    } else if (islem === "-") {
      console.log("result:", a - b);
    } else if (islem === "*") {
      console.log("result:", a * b);
    } else if (islem === "/") {
      console.log("result:", a / b);
    } else {
      console.log("invalid transaction");
    }

    console.log("action completed.\n");
  }
}

calculator();
