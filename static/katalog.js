

function DeactiveAll(){
    var izbornik = document.getElementById("izbornik");
    for (var i = 0; i < izbornik.childNodes.length; i++) {
        var node = izbornik.childNodes[i];
        if (node.nodeType == Node.ELEMENT_NODE && node.nodeName == "A") {
            node.className = "nav-link";
        }
    }  
}

function Active1(){
    DeactiveAll();
    var currentActive = document.getElementById("1");
    currentActive.className="nav-link active";  
}


function Active2(){
    DeactiveAll();
    var currentActive = document.getElementById("2");
    currentActive.className="nav-link active";
}

function Active3(){
    DeactiveAll();
    var currentActive = document.getElementById("3");
    currentActive.className="nav-link active";
}

function Active4(){
    DeactiveAll();
    var currentActive = document.getElementById("4");
    currentActive.className="nav-link active";
}
function Active5(){
    DeactiveAll();
    var currentActive = document.getElementById("5");
    currentActive.className="nav-link active";
}

function Active6(){
    DeactiveAll();
    var currentActive = document.getElementById("6");
    currentActive.className="nav-link active";
}
function Active7(){
    DeactiveAll();
    var currentActive = document.getElementById("7");
    currentActive.className="nav-link active";
}
function Active8(){
    DeactiveAll();
    var currentActive = document.getElementById("8");
    currentActive.className="nav-link active";
}

function Active9(){
    DeactiveAll();
    var currentActive = document.getElementById("9");
    currentActive.className="nav-link active";
}
function Active10(){
    DeactiveAll();
    var currentActive = document.getElementById("10");
    currentActive.className="nav-link active";
}

