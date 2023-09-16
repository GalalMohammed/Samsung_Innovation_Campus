#!/usr/bin/node
export const deepClone = function (obj) {
// Handle non-object types and null
  if (obj === null || typeof obj !== 'object') {
    return obj;
  }

  // Create a new object or array based on the original's constructor
  const clone = Array.isArray(obj) ? [] : {};

  // Iterate through each key in the object
  for (const key in obj) {
    if (Object.prototype.hasOwnProperty.call(obj, key)) {
      // Recursively clone nested objects and arrays
      clone[key] = deepClone(obj[key]);
    }
  }

  return clone;
};
