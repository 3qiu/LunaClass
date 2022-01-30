function age() {
  var birthYear=prompt ('which year did you born? enter it as xxxx');
  var ageThen=Math.trunc(2026-birthYear);
  
  document.getElementById("inputAge").innerHTML= '<big>You will become '+ ageThen + ' years old when it is <b>2026</b>!</big>';
}
age();