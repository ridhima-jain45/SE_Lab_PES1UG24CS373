"""
click_detection: figures out whether a click landed on a balloon.
"""


def check_pop(balloons, click_pos):
    """
    Returns the balloon that was clicked, or None if the click missed
    every balloon.
    """
    for balloon in balloons:
        dx = click_pos[0] - balloon.x
        dy = click_pos[1] - balloon.y
        distance_squared = dx * dx + dy * dy

        # Both sides are squared, so clicks anywhere inside the circle,
        # including the edge, are accepted.
        if distance_squared <= balloon.radius * balloon.radius:
            return balloon
    return None
