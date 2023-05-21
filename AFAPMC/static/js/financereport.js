datearr = document.getElementsByClassName("ldate");
var darr = [];
for (i = 0;i<datearr.length;i++){
    darr.push(datearr[i].innerHTML);
}
lharr = document.getElementsByClassName("lname");
var larr = [];
for (i=0;i<lharr.length;i++){
    larr.push(lharr[i].innerHTML);
}
var uniquelarr = new Set(larr);
var settoarr = Array.from(uniquelarr);
// document.getElementById("lhname").innerHTML = document.getElementById("InvoiceRecords").rows[1].cells.item(2).innerHTML;
document.getElementById("lhname").innerHTML = settoarr;
document.getElementById("lhsdate").innerHTML = darr[0];
document.getElementById("lhedate").innerHTML = darr[darr.length-1];
document.getElementById("lhamount").innerHTML = arrsum(27);

if (settoarr.length == 0){
    document.getElementById("statements").style.display = "none";
}