import time
import sys

def timer_with_static_text(duration_seconds):
    # Print the static text that will live below the timer first
    print("\n") # Leave a blank line for the timer
    print("--- STATUS PANEL ---")
    print("Task: Processing data logs...")
    print("System Status: Operational")
    print("--------------------")
    
    # Move cursor up 5 lines to get back to the timer position
    sys.stdout.write("\033[5F")
    sys.stdout.flush()

    for remaining in range(duration_seconds, -1, -1):
        # 1. Clear the current line and print the updated timer
        sys.stdout.write(f"\033[KTimer: {remaining} seconds remaining\n")
        
        # 2. Move the cursor back up 1 line so it's ready for the next loop
        sys.stdout.write("\033[1F")
        sys.stdout.flush()
        
        time.sleep(1)
        
    # Move cursor down past the static text when finished so the prompt resets cleanly
    sys.stdout.write("\033[5E")
    sys.stdout.flush()
    print("Timer finished!")

timer_with_static_text(1400)
