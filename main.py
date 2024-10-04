# Script is very janky it was made in 2 min
import win32api
import win32con
import time
import keyboard

# Define how much to move the mouse
move_amount = 10  # Move right by 10 units
double_move = move_amount * 2  # Move left by double

def move_mouse_right(amount):
    # Relative mouse movement to the right
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, amount, 0, 0, 0)

def move_mouse_left(amount):
    # Relative mouse movement to the left
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -amount, 0, 0, 0)

print("Press 'D' to move mouse right, 'A' to move left. Press ESC to exit.")

while True:
    try:
        # Check if 'D' is pressed
        if keyboard.is_pressed('d'):
            move_mouse_right(move_amount)
            time.sleep(0.01)  # Small delay to make movement smoother
        
        # Check if 'A' is pressed
        if keyboard.is_pressed('a'):
            move_mouse_left(double_move)
            time.sleep(0.01)  # Small delay to make movement smoother

        # Exit on 'Esc' key
        if keyboard.is_pressed('esc'):
            print("Exiting...")
            break

    except:
        break
