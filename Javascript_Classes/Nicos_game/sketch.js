//CREAR DOS VARIABLES QUE ALMACENEN LA INFORMACION DE LAS IMAGENES
let img1, img2;

let player1;

let enemies = []


function preload(){

img1 = loadImage("Virus.png");

  
img2 = loadImage("laptop.png");

}


function setup() {
  createCanvas(windowWidth,windowHeight);
  img1.height = img1.height / 7
  img2.height = img2.height / 7
  img1.width = img1.width / 7
  img2.width = img2.width / 7
    
  player1 = new Player(img1 , width/2 , height/2,5)
  
  setInterval(enemyGenerator,1000)
}

function draw() {
  background(13, 182, 227 );
 
  //mostrar player
  player1.show()
  player1.move()
  for (let i=0;i<enemies.length;i++){
  enemies[i].show()
  }
}
  
function enemyGenerator(){
  
  enemies.push(new Enemy ( img2 , random(0,width) , random(0,height), 5 ))
  
  
}


  
