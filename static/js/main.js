

window.addEventListener("DOMContentLoaded", (event) => {
    var socket = io.connect("http://" + document.domain + ":" + location.port );

    document.onkeydown = function(e){
        switch(e.keyCode){
            case 37:
                socket.emit("move1", {dx:-1, dy:0});
                break;
            case 38:
                socket.emit("move1", {dx:0, dy:-1});
                break;
            case 39:
                socket.emit("move1", {dx:1, dy:0});
                break;
            case 40:
                socket.emit("move1", {dx:0, dy:1});
                break;

            //for second player

            case 81:
                socket.emit("move2", {dx:-1, dy:0});
                break;
            case 90:
                socket.emit("move2", {dx:0, dy:-1});
                break;
            case 68:
                socket.emit("move2", {dx:1, dy:0});
                break;
            case 83:
                socket.emit("move2", {dx:0, dy:1});
                break;

        }
        


    };
    
    var btn_n = document.getElementById("go_n");
    btn_n.onclick = function(e) {
        console.log("Clicked on button north");
        socket.emit("move1", {dx:0, dy:-1});
        
    };
    
    var btn_s = document.getElementById("go_s");
    btn_s.onclick = function(e) {
        console.log("Clicked on button south");
        socket.emit("move1", {dx:0, dy:1});
        
    };


    var btn_w = document.getElementById("go_w");
    btn_w.onclick = function(e) {
        console.log("Clicked on button w");
        socket.emit("move1", {dx:-1, dy:0});
        
    };
    

    var btn_e = document.getElementById("go_e");
    btn_e.onclick = function(e) {
        console.log("Clicked on button e");
        socket.emit("move1", {dx:1, dy:0});
        
    };

    //buttons for player 2 :

    var btn_n2 = document.getElementById("go_n2");
    btn_n2.onclick = function(e) {
        console.log("Clicked on button north");
        socket.emit("move2", {dx:0, dy:-1});
        
    };
    
    var btn_s2 = document.getElementById("go_s2");
    btn_s2.onclick = function(e) {
        console.log("Clicked on button south");
        socket.emit("move2", {dx:0, dy:1});
        
    };


    var btn_w2 = document.getElementById("go_w2");
    btn_w2.onclick = function(e) {
        console.log("Clicked on button w");
        socket.emit("move2", {dx:-1, dy:0});
        
    };
    

    var btn_e2 = document.getElementById("go_e2");
    btn_e2.onclick = function(e) {
        console.log("Clicked on button e");
        socket.emit("move2", {dx:1, dy:0});
        
    };

    //button to add player

    var add_button = document.getElementById("add_player");
    add_button.onclick = function(e) {
        console.log("Clicked on add player");
        socket.emit("add_player", {nb:1});
    };
    


    socket.on("response_move1", function(DATA){
        console.log(DATA);
        data = DATA[0];
        lifes = DATA[1];
        for( var i=0; i<data.length; i++){
            
            var cell_id = "cell " + data[i].i + "-" + data[i].j;
            var span_to_modif = document.getElementById(cell_id);
            span_to_modif.className = data[i].content;
        }
        for ( var j=0; j<lifes.length; j++){
            var life = document.getElementById("life" + (j+1).toString());
            life.innerHTML = "Vies Joueur" +(j+1).toString() + " : " + lifes[j].toString();
            if (j==1){
                life.style.visibility = "visible";
            }
        }
       
    });

    socket.on("response_move2", function(DATA){
        console.log(DATA);
        data = DATA[0];
        lifes = DATA[1];

        for( var i=0; i<data.length; i++){
            
            var cell_id = "cell " + data[i].i + "-" + data[i].j;
            var span_to_modif = document.getElementById(cell_id);
            span_to_modif.className = data[i].content;
        }
        var boutons_caches = document.getElementById("thekeypad2");
        boutons_caches.style.visibility = "visible";
        var bouton_a_cacher = document.getElementById("add_player") ;
        bouton_a_cacher.style.visibility = "hidden";
        var texte_a_montrer = document.getElementById("Msg_adding") ;
        texte_a_montrer.style.visibility = "visible" ;
        
        for ( var j=0; j<lifes.length; j++){
            var life = document.getElementById("life" + (j+1).toString());
            life.innerHTML = "Vies Joueur" +(j+1).toString() + " : " + lifes[j].toString();
            if (j==1){
                life.style.visibility = "visible";
            }
        }

    });

    socket.on("response_adding", function(DATA){
        console.log(DATA);
        data = DATA[0];
        lifes = DATA[1];

        var cell_id = "cell " + data[0].i + "-" + data[0].j;
        var span_to_modif = document.getElementById(cell_id);
        span_to_modif.className = data[0].content;

        var boutons_caches = document.getElementById("thekeypad2");
        boutons_caches.style.visibility = "visible";
        var bouton_a_cacher = document.getElementById("add_player") ;
        bouton_a_cacher.style.visibility = "hidden";
        var texte_a_montrer = document.getElementById("Msg_adding") ;
        texte_a_montrer.style.visibility = "visible" ;

        for ( var j=0; j<lifes.length; j++){
            var life = document.getElementById("life" + (j+1).toString());
            life.innerHTML = "Vies Joueur" +(j+1).toString() + " : " + lifes[j].toString();
            if (j==1){
                life.style.visibility = "visible";
            }
        }
    });
    
    
});
