import badger2040
import time


# Draw an overlay box with a given message within it
def warning(
        message: str, display=None, timeout: int = 0,
        width: int = badger2040.WIDTH, height: int = badger2040.HEIGHT,
        line_spacing: int = 20, text_size: float = 0.6
):
    if display is None:
        display = badger2040.Badger2040()
        display.led(128)

    # Draw a light grey background
    display.pen(12)
    display.rectangle((badger2040.WIDTH - width) // 2, (badger2040.HEIGHT - height) // 2, width, height)

    # Take the provided message and split it up into
    # lines that fit within the specified width
    words = message.split(" ")

    lines = []
    current_line = ""
    for word in words:
        if display.measure_text(current_line + word + " ", text_size) < width:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    lines.append(current_line.strip())

    display.pen(0)
    display.thickness(2)

    # Display each line of text from the message, centre-aligned
    num_lines = len(lines)
    for i in range(num_lines):
        length = display.measure_text(lines[i], text_size)
        current_line = (i * line_spacing) - ((num_lines - 1) * line_spacing) // 2
        display.text(lines[i], (badger2040.WIDTH - length) // 2, (badger2040.HEIGHT // 2) + current_line, text_size)

    display.update()
    time.sleep(timeout)
