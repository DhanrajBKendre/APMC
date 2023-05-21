function cashcount() {
    var arr = [];
    for (i = 1;i<tlength-1;i++){
        if (document.getElementById("InvoiceRecords").rows[i].cells.item(28).innerHTML== "Cash"){
            arr.push(parseInt(document.getElementById("InvoiceRecords").rows[i].cells.item(27).innerHTML))
        } else {

        }
    }
    let sum = 0;
    for (const item of arr) {
        sum += item;
    }
    arr.length = 0;
    return sum;
}


function chequecount() {
    var arr = [];
    for (i = 1;i<tlength-1;i++){
        if (document.getElementById("InvoiceRecords").rows[i].cells.item(29).innerHTML=="Cheque"){
            arr.push(parseInt(document.getElementById("InvoiceRecords").rows[i].cells.item(27).innerHTML))
        } else {

        }
    }
    let sum = 0;
    for (const item of arr) {
        sum += item;
    }
    arr.length = 0;
    return sum;
}


function upicount() {
    var arr = [];
    for (i = 1;i<tlength-1;i++){
        if (document.getElementById("InvoiceRecords").rows[i].cells.item(31).innerHTML=="UPI"){
            arr.push(parseInt(document.getElementById("InvoiceRecords").rows[i].cells.item(27).innerHTML))
        } else {

        }
    }
    let sum = 0;
    for (const item of arr) {
        sum += item;
    }
    arr.length = 0;
    return sum;
}
document.getElementById("tcount28").innerHTML = cashcount();
document.getElementById("tcount29").innerHTML = chequecount();
document.getElementById("tcount31").innerHTML = upicount();