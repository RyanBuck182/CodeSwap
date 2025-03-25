let stocks = [
    ["Champlain Arms Inc.", 50],
    ["Alpha Business LLC", 25],
    ["Zigzap Innovations", 122],
    ["Crypto Hype Man Guy", 9999],
];


window.onload = (event) => {
    loadSTonks();
};


function loadSTonks() {
    let stocksTable = document.getElementById("stocks");
    stocksTable.innerHTML = "";
    for (let i = 0; i < stocks.length; i++) {
        newRow = `<tr class="flex justify-between w-full"><td>${stocks[i][0]}</td><td>${stocks[i][1]}</td></tr>`
        stocksTable.innerHTML += newRow;
    }
}




function crimeThem() {
    let text = document.getElementById("message");


    if (text.value == "Champlain Arms Inc.")
    {
        stocks[0][1] -= 10;
    }
    else if (text.value == "Alpha Business LLC")
    {
        stocks[1][1] -= 10;
    }
    else if (text.value == "Zigzap Innovations")
    {
        stocks[2][1] -= 10;
    }
    else if (text.value == "Crypto Hype Man Guy")
    {
        stocks[3][1] -= 1000000000;
    }




    loadSTonks();
}
