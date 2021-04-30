
class SequenceIterator:
    """ An iterator for python's sequence type"""

    def __init__(self, sequence):
        """
            init seq refernce and starting point as negative 1,
            so next can start with zero.
        """
        self._seq = sequence
        self._k = -1

    def __iter__(self):
        return self

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()
