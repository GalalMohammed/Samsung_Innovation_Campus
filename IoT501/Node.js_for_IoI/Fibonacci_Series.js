#!/usr/bin/node
exports.fibonacci = function (n) {
  const fib = [1, 1];
  if (n < 3) { return fib.slice(0, n); }
  while (fib.length < n) {
    fib.push(fib[fib.length - 1] + fib[fib.length - 2]);
  }
  return fib;
};
