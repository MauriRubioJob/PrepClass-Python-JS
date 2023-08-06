class Pipe
{
  constructor(pipeDownImg, pipeUpImg, xPipe, yPipe)
  {
    this.imgUp = pipeUpImg;
    this.imgDown = pipeDownImg;
    this.x = xPipe;
    this.y = yPipe;
  }
  display()
  {
    image(this.imgDown, this.x, this.y);
    image(this.imgUp, this.x, this.y - 175 - this.imgUp.height);
  }
  
  move()
  {
    this.x += pipeSpeed;
  }
}