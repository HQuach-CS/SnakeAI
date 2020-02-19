class Snake {
  constructor() {
    // 0 = Begin
    // 1 = In Progress
    // 2 = Dead
    this.isAlive = 1;
    this.snake = [
      { x: Math.floor(Math.random() * 20), y: Math.floor(Math.random() * 20) }
    ];
    this.food = {
      x: Math.floor(Math.random() * 20),
      y: Math.floor(Math.random() * 20)
    };
    this.draw();
  }

  Move(dir) {
    for (let i = this.snake.length - 1; i > 0; i--) {
      this.snake[i] = this.snake[i - 1];
    }
    this.snake[0].x += dir.x;
    this.snake[0].y += dir.y;
  }

  get status() {
    return this.isAlive;
  }

  draw() {
    // Get Canvas Property
    var canvas = document.getElementById("myCanvas");
    const ctx = canvas.getContext("2d");
    // Clear Canvas
    ctx.clearRect(0, 0, 400, 400);

    // Draw Grid
    for (var i = 0; i < 20; i++) {
      for (var j = 0; j < 20; j++) {
        ctx.beginPath();
        ctx.rect(i * 20, j * 20, i * 20 + 20, j * 20 + 20);
        ctx.stroke();
      }
    }
    // Draw Snake
    for (var i = 0; i < this.snake.length; i++) {
      ctx.fillStyle = "green";
      ctx.fillRect(this.snake[i].x * 20, this.snake[i].y * 20, 20, 20);
    }

    // Draw Food
    ctx.fillStyle = "red";
    ctx.fillRect(this.food.x * 20, this.food.y * 20, 20, 20);
  }
}

var move = [
  { x: -1, y: 0 },
  { x: 0, y: -1 },
  { x: 1, y: 0 },
  { x: 0, y: 1 }
];

function run(game) {
  setTimeout(
    function() {
      if (game.isAlive == 1) {
        game.draw();
        run(game);
      }
    },
    1000,
    game
  );
}

$(document).ready(function() {
  game = new Snake();
  run(game);
});
