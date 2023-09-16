#!/usr/bin/node
exports.reverseString = function (str) {
  let reversed = '';
  for (const c of str) {
    reversed = c + reversed;
  }
  return reversed;
};
