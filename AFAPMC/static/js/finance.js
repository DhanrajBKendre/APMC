var tlength = document.getElementById("InvoiceRecords").rows.length;

function arrsum(colnum) {
    var arr = [];
    for (i = 1; i < tlength - 1; i++) {
        var z = parseInt(document.getElementById("InvoiceRecords").rows[i].cells.item(colnum).innerHTML);
        if (isNaN(z)) {

        } else {
            arr.push(z);
        }
    }
    let sum = 0;
    for (const item of arr) {
        sum += item;
    }
    arr.length = 0;
    return sum;
}

document.getElementById("tcount5").innerHTML = arrsum(5);
document.getElementById("tcount6").innerHTML = arrsum(6);
document.getElementById("tcount7").innerHTML = arrsum(7);
document.getElementById("tcount8").innerHTML = arrsum(8);
document.getElementById("tcount9").innerHTML = arrsum(9);
document.getElementById("tcount10").innerHTML = arrsum(10);
document.getElementById("tcount11").innerHTML = arrsum(11);
document.getElementById("tcount12").innerHTML = arrsum(12);
document.getElementById("tcount13").innerHTML = arrsum(13);
document.getElementById("tcount14").innerHTML = arrsum(14);
document.getElementById("tcount15").innerHTML = arrsum(15);
document.getElementById("tcount16").innerHTML = arrsum(16);
document.getElementById("tcount17").innerHTML = arrsum(17);
document.getElementById("tcount18").innerHTML = arrsum(18);
document.getElementById("tcount19").innerHTML = arrsum(19);
document.getElementById("tcount20").innerHTML = arrsum(20);
document.getElementById("tcount21").innerHTML = arrsum(21);
document.getElementById("tcount22").innerHTML = arrsum(22);
document.getElementById("tcount23").innerHTML = arrsum(23);
document.getElementById("tcount24").innerHTML = arrsum(24);
document.getElementById("tcount25").innerHTML = arrsum(25);
document.getElementById("tcount26").innerHTML = arrsum(26);
document.getElementById("tcount27").innerHTML = arrsum(27);