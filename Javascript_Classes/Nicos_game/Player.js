class Player{
  //Propiedades
constructor(IMAGEN, POS_X, POS_Y, VEL ){

this.img = IMAGEN
this.X = POS_X
this.Y = POS_Y
this.vel = VEL

}

show(){
image(this.img,this.X,this.Y)
}
move(){


// FLECHA ARRIBA (38), 
if(keyIsDown  (38)){
this.Y -= this.vel
}

  
//FLECHA ABAJO (40),
  if(keyIsDown   (40)){
Pos_y1 += this.vel
}
  
  
// FLECHA DERECHA (37),
  if(keyIsDown (37)){
Pos_x1 -= this.vel
}

  
//FLECHA IZQUIERDA (39), 
  
if(keyIsDown   (39)){
Pos_x1 += this.vel
}
  

}
}
