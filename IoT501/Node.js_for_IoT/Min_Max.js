#!/usr/bin/node
exports.Min_Max = function (arr) {
  return [arr.reduce((prev, ele) => prev > ele ? ele : prev, arr[0]), arr.reduce((prev, ele) => prev < ele ? ele : prev, arr[0])];
};
