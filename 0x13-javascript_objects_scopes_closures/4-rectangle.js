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

  rotate () {
    this.width += this.height;
    this.height = this.width - this.height;
    this.width = this.width - this.height;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
module.exports = Rectangle;
