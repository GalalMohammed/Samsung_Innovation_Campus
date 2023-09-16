#!/usr/bin/node
exports.sumArray = function (arr) {
  return arr.reduce((pre, ele) => pre + ele, 0);
};
