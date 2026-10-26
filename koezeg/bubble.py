"""Draws the speech bubble around the text."""

import textwrap

# The maximum number of characters on one line inside the bubble.
DEFAULT_WIDTH = 40


def wrap_text(text, width=DEFAULT_WIDTH):
    """Split the text into a list of lines that are at most `width` long."""
    lines = textwrap.wrap(text, width)
    if len(lines) == 0:
        # Empty text: use one empty line, so the bubble still works.
        lines = [""]
    return lines


def make_bubble(text, width=DEFAULT_WIDTH, mode="say"):
    """Return the speech bubble for `text` as one string (with newlines)."""
    lines = wrap_text(text, width)

    # Find the length of the longest line.
    longest = 0
    for line in lines:
        if len(line) > longest:
            longest = len(line)

    border_length = longest + 1
    top = " " + "_" * border_length
    bottom = " " + "-" * border_length

    result = [top]

    if len(lines) == 1:
        # One line: < text >
        if mode=="think":
            result.append("( " + lines[0].ljust(longest) + " )")    
        else:                  
            result.append("< " + lines[0].ljust(longest) + " >")
    else:
        # More lines: the first and last line get special corners.
        # ljust() adds spaces on the right so every line is equally long.
        # Note: in Python a backslash must be written twice: "\\"
        for i in range(len(lines)):
            padded = lines[i].ljust(longest)
            if i == 0:
                result.append("/ " + padded + " \\")
            elif i == len(lines):
                result.append("\\ " + padded + " /")
            else:
                result.append("| " + padded + " |")

    result.append(bottom)
    return "\n".join(result)
