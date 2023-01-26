            var numChoix = 0

            var numImg = 0

            var nbRetourne = 0


            function retourne1_1(){
                    nbRetourne = nbRetourne+1;
                    document.getElementById("1-1").src="img/cadavre2.png";
                    document.getElementById("1-1").alt="image du tracé d'un cadavre";
                    if (numChoix==0){
                            numChoix=1;
                            numImg=2;
                            
                    }
                    else {
                            numChoix=0;
                            if (nbRetourne==8){setTimeout(gagner,1000);}
                            if (numImg!=2){setTimeout(rejouer,1000);}
                    }
                    
            }
                
                        
            
            function retourne1_3(){
                    nbRetourne = nbRetourne+1;
                    document.getElementById("1-3").src="img/sang4.png";
                    document.getElementById("1-3").alt="image d'une tache de sang'";
                    if (numChoix==0){
                            numChoix=1;
                            numImg=4;
                            
                    }
                    else {
                            numChoix=0;
                            if (nbRetourne==8){setTimeout(gagner,1000);}
                            if (numImg!=4){setTimeout(rejouer,1000);}
                    }
                    
            }
            
            
            
            function retourne2_1(){
                    nbRetourne = nbRetourne+1;
                    document.getElementById("2-1").src="img/bande1.png";
                    document.getElementById("2-1").alt="image de bandes jaunes de police";
                    if (numChoix==0){
                            numChoix=1;
                            numImg=1;
                            
                    }
                    else {
                            numChoix=0;
                            if (nbRetourne==8){setTimeout(gagner,1000);}
                            if (numImg!=1){setTimeout(rejouer,1000);}
                    }
                    
            }

            
            
            function retourne2_2(){
                    nbRetourne = nbRetourne+1;
                    document.getElementById("2-2").src="img/couteau3.png";
                    document.getElementById("2-2").alt="image d'un couteau de cuisine'";
                    if (numChoix==0){
                            numChoix=1;
                            numImg=3;
                            
                    }
                    else {
                            numChoix=0;
                            if (nbRetourne==8){setTimeout(gagner,1000);}
                            if (numImg!=3){setTimeout(rejouer,1000);}
                    }
                    
            }

            
            
            function retourne2_3(){
                    nbRetourne = nbRetourne+1;
                    document.getElementById("2-3").src="img/cadavre2.png";
                    document.getElementById("2-3").alt="image du tracé d'un cadavre";
                    if (numChoix==0){
                            numChoix=1;
                            numImg=2;
                            
                    }
                    else {
                            numChoix=0;
                            if (nbRetourne==8){setTimeout(gagner,1000);}
                            if (numImg!=2){setTimeout(rejouer,1000);}
                    }
                    
            }

            
            
            function retourne3_1(){
                    nbRetourne = nbRetourne+1;
                    document.getElementById("3-1").src="img/sang4.png";
                    document.getElementById("3-1").alt="image d'une tache de sang'";
                    if (numChoix==0){
                            numChoix=1;
                            numImg=4;
                            
                    }
                    else {
                            numChoix=0;
                            if (nbRetourne==8){setTimeout(gagner,1000);}
                            if (numImg!=4){setTimeout(rejouer,1000);}
                    }
                    
            }

            
            
            function retourne3_2(){
                    nbRetourne = nbRetourne+1;
                    document.getElementById("3-2").src="img/couteau3.png";
                    document.getElementById("3-2").alt="image d'un couteau de cuisine";
                    if (numChoix==0){
                            numChoix=1;
                            numImg=3;
                            
                    }
                    else {
                            numChoix=0;
                            if (nbRetourne==8){setTimeout(gagner,1000);}
                            if (numImg!=3){setTimeout(rejouer,1000);}
                    }
                    
            }

        
            
            function retourne3_3(){
                    nbRetourne = nbRetourne+1;
                    document.getElementById("3-3").src="img/bande1.png";
                    document.getElementById("3-3").alt="image de bandes jaunes de police";
                    if (numChoix==0){
                            numChoix=1;
                            numImg=1;
                            
                    }
                    else {
                            numChoix=0;
                            if (nbRetourne==8){setTimeout(gagner,1000);}
                            if (numImg!=1){setTimeout(rejouer,1000);}
                    }
                    
            }

            

            
            function piege(){
                    numImg=5;
                    document.getElementById("1-2").src="img/colombe5.png";
                    document.getElementById("1-2").alt="image d'une colombe";
                    setTimeout(rejouer,1000);
            }
            
            
            
            function rejouer(){
                    nbRetourne = 0;
                    if (numImg==5) {
                            alert("Dommage ! Vous avez retourné la carte piège, vous avez définitivement perdu");
                            document.getElementById("1-1").src="img/cadavre2.png";
                            document.getElementById("1-1").alt="image du tracé d'un cadavre";
                            document.getElementById("1-3").src="img/sang4.png";
                            document.getElementById("1-3").alt="image d'une tache de sang";
                            document.getElementById("2-1").src="img/bande1.png";
                            document.getElementById("2-1").alt="image de bandes jaunes de police";
                            document.getElementById("2-2").src="img/couteau3.png";
                            document.getElementById("2-2").alt="image d'un couteau de cuisine";
                            document.getElementById("2-3").src="img/cadavre2.png";
                            document.getElementById("2-3").alt="image du tracé d'un cadavre";
                            document.getElementById("3-1").src="img/sang4.png";
                            document.getElementById("3-1").alt="image d'une tache de sang";
                            document.getElementById("3-2").src="img/couteau3.png";
                            document.getElementById("3-2").alt="image d'un couteau de cuisine";
                            document.getElementById("3-3").src="img/bande1.png";
                            document.getElementById("3-3").alt="image de bandes jaunes de police";
                    }
                    else {
                            alert("Dommage ! Vous avez perdu, recommencez");
                            document.getElementById("1-1").src="img/interrogation.png";
                            document.getElementById("1-1").alt="image d'un point d'interrogation rouge";
                            document.getElementById("1-3").src="img/interrogation.png";
                            document.getElementById("1-3").alt="image d'un point d'interrogation rouge";
                            document.getElementById("2-1").src="img/interrogation.png";
                            document.getElementById("2-1").alt="image d'un point d'interrogation rouge";
                            document.getElementById("2-2").src="img/interrogation.png";
                            document.getElementById("2-2").alt="image d'un point d'interrogation rouge";
                            document.getElementById("2-3").src="img/interrogation.png";
                            document.getElementById("2-3").alt="image d'un point d'interrogation rouge";
                            document.getElementById("3-1").src="img/interrogation.png";
                            document.getElementById("3-1").alt="image d'un point d'interrogation rouge";
                            document.getElementById("3-2").src="img/interrogation.png";
                            document.getElementById("3-2").alt="image d'un point d'interrogation rouge";
                            document.getElementById("3-3").src="img/interrogation.png";
                            document.getElementById("3-3").alt="image d'un point d'interrogation rouge";
                    }
                    numChoix=0;
            }
            
            
            
            function gagner(){
                    alert("Bravo ! Vous avez gagné !");
                    document.getElementById("1-2").src="img/colombe5.png";
                    document.getElementById("1-2").alt="image d'une colombe";
            }
        

        
        