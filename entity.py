# 

class Entity:
    def __init__(self, x, y, width, height):
        """
        Initialize a new Entity object with the given x, y, width, and height.

        Parameters
        ----------
        x : int
            The x-coordinate of the entity.
        y : int
            The y-coordinate of the entity.
        width : int
            The width of the entity in pixels.
        height : int
            The height of the entity in pixels.

        Returns
        -------
        None
        """

        self.x = x
        self.y = y
        self.width = width
        self.height = height