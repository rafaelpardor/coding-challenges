// Challenge: codewars.com/kata/5a2b703dc5e2845c0900005a/

const isDivideBy = (number, a, b) => {
  if (number % a === 0 && number % b === 0) {
    return true
  } else {
    return false
  }
}
