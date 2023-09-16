#!/usr/bin/node
export const mergeSort = function (arr) {
  if (arr.length <= 1) { return arr; }
  // Split the array into two halves
  const middle = Math.floor(arr.length / 2);
  const left = arr.slice(0, middle);
  const right = arr.slice(middle);

  // Recursivley sort both halves
  const leftSorted = mergeSort(left);
  const rightSorted = mergeSort(right);

  // Merge the sorted halves
  return merge(leftSorted, rightSorted);
};

function merge (left, right) {
  const result = [];
  let leftIndex = 0;
  let rightIndex = 0;

  // Compare elements from both arrays and push the smaller one into the result
  while (leftIndex < left.length && rightIndex < right.length) {
    if (left[leftIndex] < right[rightIndex]) {
      result.push(left[leftIndex]);
      leftIndex++;
    } else {
      result.push(right[rightIndex]);
      rightIndex++;
    }
  }

  // Push any remaining elements from the left and right arrays
  return result.concat(left.slice(leftIndex), right.slice(rightIndex));
}
