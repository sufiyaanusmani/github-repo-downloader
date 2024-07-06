from constants import Colors

def print_message(message, message_type="info"):
    """
    Print a message in the terminal with colors based on message type.

    :param message: The message to print
    :param message_type: The type of the message ('error', 'warning', 'success', 'info')
    """
    if message_type == "error":
        color = Colors.RED
    elif message_type == "warning":
        color = Colors.YELLOW
    elif message_type == "success":
        color = Colors.GREEN
    else:
        color = Colors.RESET

    # Print the message with the chosen color
    print(f"{color}{message}{Colors.RESET}")