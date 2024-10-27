def min_switch_presses(bulbs):
    """
    Given the initial state of N bulbs, where each bulb has a switch that
    toggles its own state and the state of all bulbs to the right, this function
    returns the minimum number of switch presses needed to turn on all bulbs.

    Parameters:
    bulbs (list of int): A list where each element represents the state of a bulb.
                         0 means the bulb is off, and 1 means the bulb is on.

    Returns:
    int: The minimum number of switches to press to turn on all bulbs.
    """
    press_count = 0
    toggle = 0  # Tracks if the state is inverted due to previous presses

    for bulb in bulbs:
        # XOR with toggle to see if the bulb is effectively off
        if bulb ^ toggle == 0:
            press_count += 1
            toggle ^= 1  # Toggle the state for all bulbs to the right

    return press_count

# Example usage
if __name__ == "__main__":
    bulbs = list(map(int, input("Enter bulb states (0 for off, 1 for on): ").split()))
    result = min_switch_presses(bulbs)
    print("Minimum Switch Presses:", result)
