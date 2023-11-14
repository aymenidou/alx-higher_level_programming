#!/usr/bin/node
let publicCount = 0;
exports.logMe = function (item) {
  console.log(publicCount + ': ' + item);
  publicCount++;
};
