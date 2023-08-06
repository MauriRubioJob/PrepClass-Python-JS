// Contains the info of the canvas
let canvas;

// Contains the images
let birdImg, pipeDownImg, pipeUpImg;

// bird vector containing Bird class info
let bird;

// yPipe stores the value of the new pipe y position created
let yPipe;

// Vector that holds all
let pipes;


let velocity = 0;
let angle = 0;
let jumpSpeed = 10;
let pipeSpeed = -2;
let speed = 1.5;


let timer;
let i;
let gameOverFlag = false;
let score = 0, highScore = 0;

function preload()
{
  loadImages();
  loadSounds();
}

function setup() 
{
  canvas = createCanvas(1000, 500);
  setObjects();
  setSounds();
  canvas.mousePressed(jump);
}

function draw() 
{
  background(backgroundImg);
  
  birdMovement();
  
  crashManager();
    
  pipeGenerator();
  
  showScore();
}

function keyPressed()
{ 
  if(keyCode === 32)
  {
    jump();
  }
  
  if(keyCode === 82 && gameOverFlag)
  {
    restart();
  }
}

function birdMovement()
{
  push();
  translate(bird.x, bird.y);
  if(!gameOverFlag)
  fall();
  angle = map(velocity, -jumpSpeed, jumpSpeed, -PI/4, PI/4);
  rotate(angle);
  boundaries();
  bird.display();
  pop();
}

function jump()
{
  if(!gameOverFlag)
  {
    jumpSound.play();
    if (velocity > -jumpSpeed) 
    {
      velocity = -jumpSpeed;
    }
    //velocity*= friction;
    bird.y += velocity * speed; 
  }
  
}

function fall()
{
  if(velocity < jumpSpeed)
  {
    velocity ++;
  }
  bird.y += velocity * speed;
}

function boundaries()
{
  if(bird.y > height)
  {
    bird.y = height;
    velocity = 0;
  }
  else if(bird.y < 0)
  {
    bird.y = 0;
  }
}

function pipeGenerator()
{
  if(!gameOverFlag)
    timer += deltaTime/1000;
  
  if(timer >= 4 && i<4)
  {
    i++;
    yPipe = height-100 - floor(random(0, height-200));
    pipes[i] = new Pipe(pipeDownImg, pipeUpImg, width, yPipe);
    timer = 0;
  }
  else if(timer >= 4 && i>=4)
  {
    i = 0;
    yPipe = height-100 - floor(random(0, height-200));
    pipes[i] = new Pipe(pipeDownImg, pipeUpImg, width, yPipe);
    timer = 0;
  }
}

function crash(element)
{
  //crashDown
  if(bird.y > element.y && ((bird.x + bird.img.width/2 > element.x+25 && bird.x + bird.img.width/2 < element.x + element.imgDown.width-25)|| (bird.x - bird.img.width/2 > element.x+25 && bird.x - bird.img.width/2 < element.x + element.imgDown.width-25)))
  {
    //console.log("choca abajo");
    gameOver();
  }
  
  //crashUp
  if(bird.y < element.y - 175 && ((bird.x + bird.img.width/2 > element.x +25 && bird.x + bird.img.width/2 < element.x + element.imgDown.width-25) || (bird.x - bird.img.width/2 > element.x +25 && bird.x - bird.img.width/2 < element.x + element.imgDown.width-25)))
  {
    //console.log("choca arriba");
    gameOver();
  }
}

function crashManager()
{
  for(let element of pipes)
  {
    if(!gameOverFlag)  
      element.move();
    crash(element);
    countScore(element);
    element.display();
  }
}

function gameOver()
{
  if(!gameOverFlag)
      gameOverSound.play();
  gameOverFlag = true;
  mainMusic.stop();
  push();
    
  fill(255, 255, 0);
  textSize(32);
  textAlign(CENTER);
  text("GAME OVER", width/2, height/2)
  textSize(25);
  text("(Press 'r' to restart)", width/2, height/2 + 30);

  // noLoop();
  pop();
    
}

function restart()
{
  setObjects();
  gameOverFlag = false;
}

function setObjects()
{
  i = 0;
  timer = 0;
  pipes = [];
  if(score > highScore)
    highScore = score;
  score = 0;
  bird = new Bird(birdImg, width/5, height/2);
  pipes[i] = new Pipe(pipeDownImg, pipeUpImg, width, height/2);
  mainMusic.loop();
}

function setSounds()
{
  jumpSound.setVolume(0.025);
  scoreSound.setVolume(0.3);
  mainMusic.loop();
}

function showScore()
{
  push();
  fill(255);
  textAlign(LEFT);
  textSize(25);
  text("Score: " + score, 30, 30);
  text("High Score: " + highScore, 30, 60);
  pop();
}

function countScore(element)
{
  if(bird.x - bird.img.width/2 == element.x + element.imgDown.width-24)
  {
    scoreSound.play();
    score++;
  }
}

function loadSounds()
{
  mainMusic = loadSound('Flappy_Fantasy.wav');
  gameOverSound = loadSound('Game_over.wav');
  jumpSound = loadSound('Jump.wav');
  scoreSound = loadSound('Score.wav');
}

function loadImages()
{
  birdImg = loadImage('Chocobo_64x64.png');
  pipeDownImg = loadImage('PipeDown128x512.png');
  pipeUpImg = loadImage('PipeUp128x512.png');
  backgroundImg = loadImage('background.jpg');
}