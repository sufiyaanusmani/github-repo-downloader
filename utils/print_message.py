from constants import Colors, Message

def print_message(message, message_type="info"):
    """
    Print a message in the terminal with colors based on message type.

    :param message: The message to print
    :param message_type: The type of the message ('error', 'warning', 'success', 'info')
    """
    if message_type == Message.ERROR:
        color = Colors.RED
    elif message_type == Message.WARNING:
        color = Colors.YELLOW
    elif message_type == Message.SUCCESS:
        color = Colors.GREEN
    else:
        color = Colors.RESET

    # Print the message with the chosen color
    print(f"{color}{message}{Colors.RESET}")
