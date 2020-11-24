from doblemente_enlazada import DoubleLinkedList


if __name__ == "__main__":

    ls = DoubleLinkedList()
    print(f"Esta vacia?  {ls.is_empty()}")
    ls.append(5)
    ls.append(6)
    ls.append(7)
    ls.append(8)
    ls.transversal()
    ls.get_size()
    ls.find_from_head(3)
    ls.remove_from_head(7)
    ls.transversal()
    ls.reverse_transversal()