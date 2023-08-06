class Bird
{
  constructor(birdImg, xBird, yBird)
  {
    this.img = birdImg;
    this.x = xBird;
    this.y = yBird;
  }
  display()
  {
    imageMode(CENTER);
    image(this.img, /*-this.img.width/2, -this.img.height/2*/ 0, 0);
  }
}