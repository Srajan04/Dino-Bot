import math
import time

import keyboard
import pyautogui as gui


# Function to get the color of a pixel in an image
def get_pixel_color(image, x_coordinate, y_coordinate):
    pixel = image.load()
    return pixel[x_coordinate, y_coordinate]


# Main function to start the Dino Bot
def start_dino_bot():
    # Define the region for the screenshot
    screenshot_x, screenshot_y, screenshot_width, screenshot_height = 60, 200, 1210, 340

    # Initialize jump times
    current_jump_time = 0
    previous_jump_time = 0

    # Initialize time while jumping and interval time
    current_time_while_jumping = 0
    previous_interval_time = 0

    # Define the y-coordinates for obstacle detection
    (
        obstacle_lower_y,
        obstacle_upper_y,
        obstacle_search_start_x,
        obstacle_search_end_x,
    ) = 288, 230, 940, 1000
    bird_y_coordinate = 220

    time.sleep(5)  # Wait for 5 seconds to launch chrome://dino
    while True:
        # Break the loop if 'q' is pressed
        if keyboard.is_pressed("q"):
            break

        # Take a screenshot of the game
        screenshot_image = gui.screenshot(
            region=(screenshot_x, screenshot_y, screenshot_width, screenshot_height)
        )
        screenshot_image.save("dino_bot.jpg")  # Save the screenshot for debugging
        background_color = get_pixel_color(
            screenshot_image, 100, 100
        )  # Get the background color

        # Scan the screenshot for obstacles
        for i in reversed(range(obstacle_search_start_x, obstacle_search_end_x)):
            # If an obstacle is detected, jump
            if (
                get_pixel_color(screenshot_image, i, obstacle_lower_y)
                != background_color
                or get_pixel_color(screenshot_image, i, obstacle_upper_y)
                != background_color
            ):
                keyboard.press("up")  # Press the 'up' key to jump
                current_jump_time = time.time()  # Update the jump time
                current_time_while_jumping = current_jump_time
                break
            # If a bird is detected, duck
            if (
                get_pixel_color(screenshot_image, i, bird_y_coordinate)
                != background_color
            ):
                keyboard.press("down")  # Press the 'down' key to duck
                time.sleep(0.4)  # Wait for a while before releasing the 'down' key
                keyboard.release("down")
                break

        # Calculate the time interval between jumps
        interval_time = current_time_while_jumping - previous_jump_time

        # If the interval time has changed, adjust the obstacle search end x-coordinate
        if previous_interval_time != 0 and math.floor(interval_time) != math.floor(
            previous_interval_time
        ):
            obstacle_search_end_x += 5
            if obstacle_search_end_x >= screenshot_width:
                obstacle_search_end_x = screenshot_width

        # Update the previous jump time and interval time
        previous_jump_time = current_jump_time
        previous_interval_time = interval_time


# Start the Dino Bot
start_dino_bot()
