
function operations() {
  var h=prompt ('enter the height of the cylinder in"cm"');
  var r=prompt ('enter the radius of the cylinder in "cm"');
  var v=Math.trunc(3.14*r*r*h);
  
  document.getElementById("input1").innerHTML= '<strong>V=π*r^2*h</strong><br>';
  document.getElementById("input2").innerHTML="<b>Result V= </b>"+v;
}

operations();

