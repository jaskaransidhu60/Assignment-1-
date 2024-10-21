class StaticArrayException(Exception):
    """Custom exception for Static Array class."""
    pass

class StaticArray:
    """Implementation of a Static Array Data Structure."""

    def __init__(self, size: int = 10) -> None:
        if size < 1:
            raise StaticArrayException('Array size must be a positive integer')
        self._size = size
        self._data = [None] * size

    def get(self, index: int):
        """Return value from given index."""
        if index < 0 or index >= self.length():
            raise StaticArrayException('Index out of bounds')
        return self._data[index]

    def set(self, index: int, value) -> None:
        """Set value at the given index."""
        if index < 0 or index >= self.length():
            raise StaticArrayException('Index out of bounds')
        self._data[index] = value

    def length(self) -> int:
        """Return the length of the StaticArray."""
        return self._size

    def __str__(self) -> str:
        """String representation of the StaticArray."""
        return f"STAT_ARR Size: {self._size} {self._data}"
