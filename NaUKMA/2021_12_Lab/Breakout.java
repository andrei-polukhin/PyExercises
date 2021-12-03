import acm.graphics.*;
import acm.program.*;
import acm.util.*;

import java.awt.*;
import java.awt.event.*;

public class Breakout extends GraphicsProgram {
    public static final int APPLICATION_WIDTH = 400;
    public static final int APPLICATION_HEIGHT = 600;

    /** Dimensions of game board (usually the same) */
    private static final int WIDTH = APPLICATION_WIDTH;
    private static final int HEIGHT = APPLICATION_HEIGHT;

    private static final int PADDLE_WIDTH = 60;
    private static final int PADDLE_HEIGHT = 10;

    /** Offset of the paddle up from the bottom of the lowest brick */
    private static final int PADDLE_Y_OFFSET = 30;

    private static final int NBRICKS_PER_ROW = 10;

    private static final int NBRICK_ROWS = 10;

    private static final int BRICK_SEP = 4;

    private static final int BRICK_WIDTH =
        (WIDTH - (NBRICKS_PER_ROW - 1) * BRICK_SEP) / NBRICKS_PER_ROW;

    private static final int BRICK_HEIGHT = 8;

    private static final int BALL_RADIUS = 10;

    private static final int BRICK_Y_OFFSET = 70;

    private static final int NTURNS = 3;

    /** Ball velocity */
    private double vx, vy;

    /** Random number generator for velocity */
    private final RandomGenerator rgen = RandomGenerator.getInstance();

    private static final int DELAY = 10;

    /** Distinct paddle and ball objects */
    private GRect paddle;
    private GOval ball;

    private int brickCounter = NBRICKS_PER_ROW * NBRICK_ROWS;

    public void run() {
        for (int i=0; i < NTURNS; i++) {
            setWorld();
            playGame();

            // win
            if (brickCounter == 0) {
                ball.setVisible(false);
                notifyWin();
                break;
            }

            // missed ball - try again
            if (brickCounter > 0) {
                removeAll();
            }
        }

        // all 3 balls used - loss
        if (brickCounter > 0) {
            notifyLoss();
        }
    }

    private void setWorld() {
        this.setSize(WIDTH, HEIGHT);
        drawBricks();
        drawPaddle();
        drawBall();

        addMouseListeners();

        brickCounter = NBRICKS_PER_ROW * NBRICK_ROWS;
    }

    private void drawBricks() {
        for (int row = 0; row < NBRICK_ROWS; row++) {
            for (int column = 0; column < NBRICKS_PER_ROW; column++) {
                // let's calculate the abscissa and the ordinate of the brick

                double	x = (
                    // start at the center width
                    (double) getWidth() / 2 -
                    // subtract half of the bricks (width) in the row
                    ( (double) NBRICKS_PER_ROW*BRICK_WIDTH) / 2 -
                    // subtract half of the separations (width) between the bricks in the row
                    ((NBRICKS_PER_ROW-1) * (double) BRICK_SEP) / 2 +
                    // add brick width and separation for next bricks
                    column * (BRICK_WIDTH + BRICK_SEP)
                );

                double	y = (
                    // start at the given length from the top for the first row
                    (double) Breakout.BRICK_Y_OFFSET +
                    // add a brick height and a brick separation for each of the following rows
                    row * (BRICK_HEIGHT + BRICK_SEP)
                );

                // add brick
                GRect brick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);
                add(brick);
                brick.setFilled(true);

                // set bricks' colors
                if (row < 2) {
                    brick.setColor(Color.RED);
                } else if (row <= 3) {
                    brick.setColor(Color.ORANGE);
                } else if (row <= 5) {
                    brick.setColor(Color.YELLOW);
                } else if (row <= 7) {
                    brick.setColor(Color.GREEN);
                } else {
                    brick.setColor(Color.CYAN);
                }
            }
        }
    }

    private void drawPaddle() {
        // default is the middle of the screen
        double x = (double) getWidth() / 2 - (double) PADDLE_WIDTH / 2;
        // subtracting paddle offset and height is vital for spacing
        double y = getHeight() - PADDLE_Y_OFFSET - PADDLE_HEIGHT;

        paddle = new GRect (x, y, PADDLE_WIDTH, PADDLE_HEIGHT);
        paddle.setFilled(true);
        add(paddle);
    }

    public void mouseMoved(MouseEvent e) {
        /* subtract the half a paddle's width if we are out of the screen
        to prevent paddle going off the screen */
        if ((e.getX() > PADDLE_WIDTH / 2) && (e.getX() < getWidth() - PADDLE_WIDTH / 2)) {
            paddle.setLocation(
            e.getX() - (double) PADDLE_WIDTH / 2,
            getHeight() - PADDLE_Y_OFFSET - PADDLE_HEIGHT
            );
        }

    }

    private void drawBall() {
        double x = (double) getWidth() / 2 - BALL_RADIUS;
        double y = (double) getHeight() / 2 - BALL_RADIUS;

        ball = new GOval(x, y, BALL_RADIUS, BALL_RADIUS);
        ball.setFilled(true);
        add(ball);
    }

    private void playGame() {
        waitForClick();
        getBallVelocity();
        while (true) {
            moveBall();

            // prevent going off the top of the screen
            if (ball.getY() >= getHeight()) {
                break;
            }

            // win scenario
            if (brickCounter == 0) {
                break;
            }
        }
    }

    private void getBallVelocity() {
        vy = 4.0;
        vx = rgen.nextDouble(1.0, 3.0);
        if (rgen.nextBoolean(0.5)) {
            vx = -vx;
        }

    }

    private void moveBall() {
        ball.move(vx, vy);

        // check for walls
        // need to get vx and vy at the point closest to 0 or the other edge
        if ((ball.getX() - vx <= 0 && vx < 0 ) || (ball.getX() + vx >= (getWidth() - BALL_RADIUS * 2) && vx > 0)) {
            vx = -vx;
        }

        // no need to check the bottom wall
        if ((vy < 0 && ball.getY() - vy <= 0)) {
            vy = -vy;
        }

        // check for other objects
        GObject collider = getCollidingObject();
        if (collider == paddle) {
            /*
            1) we need to make sure that the ball only bounces off the top part of the paddle;
            2) we estimate the point to be greater or equal to the height at which the ball hits the paddle
               but less than the height where the ball hits the paddle minus 4.
            */

            if(
                ball.getY() >= getHeight() - PADDLE_Y_OFFSET - PADDLE_HEIGHT - BALL_RADIUS * 2 &&
                ball.getY() < getHeight() - PADDLE_Y_OFFSET - PADDLE_HEIGHT - BALL_RADIUS * 2 + 4
            ) {
                vy = -vy;
            }
        }

        // touching the brick
        else if (collider != null) {
            remove(collider);
            brickCounter--;
            vy = -vy;
        }

        pause (DELAY);
    }

    private GObject getCollidingObject() {
        if ((getElementAt(ball.getX(), ball.getY())) != null) {
            return getElementAt(ball.getX(), ball.getY());
        }
        if (getElementAt( (ball.getX() + BALL_RADIUS * 2), ball.getY()) != null) {
            return getElementAt(ball.getX() + BALL_RADIUS * 2, ball.getY());
        }
        if (getElementAt(ball.getX(), (ball.getY() + BALL_RADIUS * 2)) != null){
            return getElementAt(ball.getX(), ball.getY() + BALL_RADIUS * 2);
        }
        if (getElementAt((ball.getX() + BALL_RADIUS * 2), (ball.getY() + BALL_RADIUS * 2)) != null) {
            return getElementAt(ball.getX() + BALL_RADIUS * 2, ball.getY() + BALL_RADIUS * 2);
        }

        // no objects present
        return null;
    }

    private void notifyLoss() {
        GLabel loss = new GLabel(
        "Game Lost!",
        (double) getWidth() / 2,
        (double) getHeight() / 2
        );
        loss.move(-loss.getWidth() / 2, -loss.getHeight());
        loss.setColor(Color.RED);
        add(loss);
    }

    private void notifyWin() {
        GLabel win = new GLabel(
        "Game Won!",
        (double) getWidth() / 2,
        (double) getHeight() / 2
        );
        win.move(-win.getWidth() / 2, -win.getHeight());
        win.setColor(Color.RED);
        add(win);
    }
}
