def direction(facing: str, turn: int):
    sides = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    if facing not in sides:
        return "Side does not exist"
    initial = sides.index(facing)
    if turn >= 0:
        turn %= 360
    else:
        turn %= -360
    steps = turn / 45
    new = initial + steps
    if new > len(sides) - 1:
        new -= len(sides)
    elif new < 0:
        new += len(sides)
    return sides[int(new)]
