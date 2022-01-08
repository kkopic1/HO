function Custom() {
    // Get the checkbox
    var checkBox = document.getElementById("inlineRadio2");
    // Get the output text
    var text = document.getElementById("custom");
    var button = document.getElementById("buttonMakePlan");
    var goal = document.getElementById("goal");

    var value = goal.options[goal.selectedIndex].value;
    console.log(value); 
  
    // If the checkbox is checked, display the output text
    if (checkBox.checked == true){
      text.style.display = "block";
      button.style.top = "1190px";
      button.style.left = "880px";
    } 
    if(value == "1"){
        var cijena = document.getElementById("Cijena");
        cijena.style.display = "none";
    }
    if(value == "2"){
      var kalorije = document.getElementById("Kalorije");
      kalorije.style.display = "none";
    }
    if(value == "3"){
      var zeljezo = document.getElementById("Zeljezo");
      zeljezo.style.display = "none";
    }
    if(value == "4"){
      var sol = document.getElementById("Sol");
        sol.style.display = "none";
    }
    
  }

  function Default() {
    // Get the checkbox
    var checkBox = document.getElementById("inlineRadio1");
    // Get the output text
    var text = document.getElementById("custom");
    var button = document.getElementById("buttonMakePlan");
    
    // If the checkbox is checked, display the output text
    if (checkBox.checked == true){
      text.style.display = "none";
      button.style.top = "670px";
      button.style.left = "790px";
    
    }
  }

  function Change(){
    // Get the checkbox
    var checkBox = document.getElementById("inlineRadio2");
    // Get the output text
    var text = document.getElementById("custom");
    var button = document.getElementById("buttonMakePlan");
    var goal = document.getElementById("goal");

    var value = goal.options[goal.selectedIndex].value;
    console.log(value); 
  
    // If the checkbox is checked, display the output text
    if (checkBox.checked == true){
      var cijena = document.getElementById("Cijena");
      cijena.style.display = "block";
      var kalorije = document.getElementById("Kalorije");
      kalorije.style.display = "block";
      var zeljezo = document.getElementById("Zeljezo");
      zeljezo.style.display = "block";
      var sol = document.getElementById("Sol");
      sol.style.display = "block";
      text.style.display = "block";
      button.style.top = "1190px";
      button.style.left = "880px";
    } 
    if(value == "1"){
        var cijena = document.getElementById("Cijena");
        cijena.style.display = "none";
    }
    if(value == "2"){
      var kalorije = document.getElementById("Kalorije");
      kalorije.style.display = "none";
    }
    if(value == "3"){
      var zeljezo = document.getElementById("Zeljezo");
      zeljezo.style.display = "none";
    }
    if(value == "4"){
      var sol = document.getElementById("Sol");
        sol.style.display = "none";
    }
    
  }



  

  document.getElementById("input0").defaultValue = "0";
  document.getElementById("input1").defaultValue = "2400";
  document.getElementById("input2").defaultValue = "48";
  document.getElementById("input3").defaultValue = "360";
  document.getElementById("input4").defaultValue = "80";
  document.getElementById("input5").defaultValue = "2600";
  document.getElementById("input6").defaultValue = "75";
  document.getElementById("input7").defaultValue = "350";
  document.getElementById("input8").defaultValue = "300";
  document.getElementById("input9").defaultValue = "1500";
  document.getElementById("input10").defaultValue = "18";
  document.getElementById("input11").defaultValue = "1000";