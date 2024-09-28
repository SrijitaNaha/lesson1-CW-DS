# Object Oriented Programming
# Focus on real life entities to write code


class Fruit:
    """
    A class representing a fruit with its attributes and methods.
    """

    def __init__(self, color, taste, shape, preference):
        """
        Initializes a Fruit object with its attributes.

        Args:
            color (str): The color of the fruit.
            taste (str): The taste of the fruit.
            shape (str): The shape of the fruit.
            preference (int): The preference level of the fruit.
        """
        self.color = color
        self.taste = taste
        self.shape = shape
        self.preference = preference

    # Getters
    @property
    def shape(self):
        """
        Gets the shape of the fruit.

        Returns:
            str: The shape of the fruit.
        """
        return self._shape

    # Setters
    @shape.setter
    def shape(self, new_shape):
        """
        Sets the shape of the fruit.

        Args:
            new_shape (str): The new shape of the fruit.
        """
        self._shape = new_shape

    # Custom Methods
    def increase_preference(self):
        """
        Increases the preference level of the fruit by 1.
        """
        self.preference += 1

    def show_fruit(self):
        """
        Prints the details of the fruit.
        """
        print(
            f"Hello I am a fruit with {self.color}, {self.shape}, {self.taste}, {self.preference}"
        )


# Example usage
if __name__ == "__main__":
    apple = Fruit("red", "sour", "round", 1)
    apple.show_fruit()
    apple.increase_preference()

    print(apple.shape)
    apple.shape = "sphere"
    apple.show_fruit()

    banana = Fruit("yellow", "sweet", "cylinder", 2)
    banana.show_fruit()
    banana.increase_preference()
    banana.show_fruit()
