# SnakeGame

Snake is a video game genre where the player maneuvers a growing line in order to eat food,
that becomes a primary obstacle to itself as it grow.
Turtle Module of the Python Standard Library is primarily used in this project.
The Project is completely Object Oriented.

The Steps involved are :

1. Creating the Snake Body :
   The Snake body is created in the Snake class.
   The initial snake consists of 3 blocks(turtles) created using the Turtle class.
   
2. Moving the Snake :
   The position of only the first block(Head of the Snake) is changed and the other blocks
   come to the position of the block present in front of them.
   
3. Controlling the Snake :
   The Arrow keys are used to control the Snake to go Up, Down, Left and Right.
   The Snake cannot go in the opposite direction.
   
4. Creating the Food :
   The Food is created in the Food class which inherits the Turtle class.
   The Food turtle is place at a random position on the screen generated using the
   randint(a, b) function of the random module, where a and b are the lower and upper boundaries.
   
5. Creating the Scoreboard :
   The Scoreboard is created in the ScoreBoard class which inherits the Turtle class.
   The Score is increased by 1 when the Snake collides with the Food.
   
6. Detecting the collision with the Food :
   The Snake is considered collided with the Food when the distance between the snake head
   Turtle instance and the food Turtle instance is less than 15 px.
   
7. Detecting the collision with the boundaries :
   The size of the Game Screen is 600 x 600 px. The Snake is considered collided with the boundarld sy
   once the position of the snake head Turtle instance surpasses the range (-280, 280) x and y coordinate both.
   
8. Detecting the collision with the Snake's own tail :
   The Snake is considered collided with its own tail once the distance of the snake head Turtle instance from
   its other segments is less than 10 px. Here we avoid checking the distance with the snake head itself, as it
   would stop the game in the beginning only.
