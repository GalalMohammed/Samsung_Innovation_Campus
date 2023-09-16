#!/usr/bin/node
export const memorize = function (func) {
  const cache = {}; // object to store cached results

  return function (...args) {
    const key = JSON.stringify(args); // Create a unique key based on input arguments

    if (cache[key] === undefined) {
    // If the result is not cached compute and cache it
      cache[key] = func(...args);
    }

    return cache[key]; // Return the cached result
  };
};
