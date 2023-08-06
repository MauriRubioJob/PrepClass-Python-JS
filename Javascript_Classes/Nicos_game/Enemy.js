class Enemy {


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
this.Y += this.vel
this.X += this.vel
}


}