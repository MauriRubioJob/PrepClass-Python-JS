let player
let playerX
let playerY

let enemy
let enemyXCoords = []
let enemyYCoords = []
let enemyVelocities = []

let forwardPressed = false
let backwardPressed = false
let leftPressed = false
let rightPressed = false

let bulletXCoords = []
let bulletYCoords = []
let bulletVelocities = []

let time = 0

function preload() {
  player = loadImage("rhino.png")
  enemy = loadImage("chicken.png")
}

function setup() {
  createCanvas(windowWidth, windowHeight)
  
  imageMode(CENTER)
  textAlign(CENTER, CENTER)
  textSize(100)
  fill(0)
  
  // Make the images a bit smaller
  player.width = player.width / 3
  player.height = player.height / 3
  enemy.width = enemy.width / 3
  enemy.height = enemy.height / 3
  
  // Put the player in the middle of the screen
  playerX = width / 2
  playerY = height / 2
  
  // Spawn an enemy every 500 milliseconds
  setInterval(spawnEnemy, 500)
}

function draw() {
  background(220);
  
  // Display and update the time
  text(time, width / 2, height / 2)
  time = round(millis() / 1000)
  
  // Display the player
  image(player, playerX, playerY)
  
  // Player movement
  if (forwardPressed == true) {
    playerY = playerY - 4
  }
  if (backwardPressed == true) {
    playerY = playerY + 4
  }
  if (leftPressed == true) {
    playerX = playerX - 4
  }
  if (rightPressed == true) {
    playerX = playerX + 4
  }
  
  // Bullets
  for (let i = 0; i < bulletXCoords.length; i++) {
    let x = bulletXCoords[i]
    let y = bulletYCoords[i]
    let speed = bulletVelocities[i]
    
    // Draw the bullet
    square(x, y, 5)
    
    // Move the bullet
    x = x + speed.x
    y = y + speed.y
    
    // Save the updated bullet
    bulletXCoords[i] = x
    bulletYCoords[i] = y
    
    // Loop through all the enemies and remove any hit by the bullet
    for (let j = enemyXCoords.length - 1; j >= 0; j--) {
      let distance = dist(x, y, enemyXCoords[j], enemyYCoords[j])
      if (distance < 25) {
        enemyXCoords.splice(j, 1)
        enemyYCoords.splice(j, 1)
        enemyVelocities.splice(j, 1)
      }
    }
    
  }
  
  // Deleting bullets off the screen
  for (let i = bulletXCoords.length - 1; i >= 0; i--) {
    let x = bulletXCoords[i]
    let y = bulletYCoords[i]
    
    if (y < 0 || y > height || x < 0 || x > width) {
      bulletXCoords.splice(i, 1)
      bulletYCoords.splice(i, 1)
      bulletVelocities.splice(i, 1)
    }
  }
  
  // Enemies
  for (let i = 0; i < enemyXCoords.length; i++) {
    let x = enemyXCoords[i]
    let y = enemyYCoords[i]
    let speed = enemyVelocities[i]
    
    // Draw the enemy
    image(enemy, x, y)
    
    // Update the speed
    let differenceX = playerX - x
    let differenceY = playerY - y
    let velocity = createVector(differenceX, differenceY)
    velocity.setMag(2)
    
    // Move the enemy
    x = x + speed.x
    y = y + speed.y
    
    // Save the updated enemy
    enemyXCoords[i] = x
    enemyYCoords[i] = y
    enemyVelocities[i] = velocity
    
    // Game over
    if (dist(playerX, playerY, x, y) < 25) {
      fill(255, 0, 0, 100)
      rect(0, 0, width, height)
      noLoop()
    }
  }
}


function mousePressed() {
  let differenceX = mouseX - playerX
  let differenceY = mouseY - playerY
  let bullet = createVector(differenceX, differenceY)
  bullet.setMag(20)
  
  bulletXCoords.push(playerX)
  bulletYCoords.push(playerY)
  bulletVelocities.push(bullet)
}


function keyPressed() {
  if (keyCode == 87) {
    forwardPressed = true
  }
  if (keyCode == 83) {
    backwardPressed = true
  }
  if (keyCode == 65) {
    leftPressed = true
  }
  if (keyCode == 68) {
    rightPressed = true
  }
}


function keyReleased() {
  if (keyCode == 87) {
    forwardPressed = false
  }
  if (keyCode == 83) {
    backwardPressed = false
  }
  if (keyCode == 65) {
    leftPressed = false
  }
  if (keyCode == 68) {
    rightPressed = false
  }
}


function spawnEnemy() {
  let chosenSide = random(["top", "bottom", "left", "right"])
  if (chosenSide == "top") {
    let x = random(0, width)
    let y = 0
    enemyXCoords.push(x)
    enemyYCoords.push(y)
    enemyVelocities.push(createVector())
  }
  if (chosenSide == "bottom") {
    let x = random(0, width)
    let y = height
    enemyXCoords.push(x)
    enemyYCoords.push(y)
    enemyVelocities.push(createVector())
  }
  if (chosenSide == "left") {
    let x = 0
    let y = random(0, height)
    enemyXCoords.push(x)
    enemyYCoords.push(y)
    enemyVelocities.push(createVector())
  }
  if (chosenSide == "right") {
    let x = width
    let y = random(0, height)
    enemyXCoords.push(x)
    enemyYCoords.push(y)
    enemyVelocities.push(createVector())
  }
}




