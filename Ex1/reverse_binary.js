

function reversebinary (n) {


  return parseInt(n.toString(2).split('').reverse().join(''), 2);
}


function reversebinary (n) {
  
  var r = 0;
  
  do {
    r = (r << 1) + (n & 1);
  } while ((n = n >> 1));
  
  return r;
}
console.log(reversebinary(13)); // 11
console.log(reversebinary(47)); // 61