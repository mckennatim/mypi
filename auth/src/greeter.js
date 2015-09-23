// greeter.js
class Greeter {
    constructor(message) {
      this.message = message;
    }

    greet() {
      var element = document.querySelector('#message');
      element.innerHTML = this.message;
    }
}

var greeter = new Greeter('hey freakin dog Uli');
greeter.greet();