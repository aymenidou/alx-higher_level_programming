#!/usr/bin/node
const Rectangle = class {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let i = 0; i < this.width; i++) {
        line += 'X';
      }
      console.log(line);
    }
  }
};
module.exports = Rectangle;
