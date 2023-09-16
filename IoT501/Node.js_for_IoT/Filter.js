#!/usr/bin/node
exports.filter = function (arr, condition) {
  const filtered = [];
  for (const e of arr) {
    if (condition(e)) { filtered.push(e); }
  }
  return filtered;
};
