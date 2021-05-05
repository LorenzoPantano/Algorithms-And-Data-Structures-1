
from AlberoAVL import AVLTree
from ListaConcatenataDictionary import LinkedListDictionary

def listaToAVL(lista):
    """Funzione per trasformare una lista collegata in un
    albero AVL
    :param: lista collegata
    :return: Albero AVL formato dagli elementi della lista collegata
    """
    tree = AVLTree()
    future_node = lista.theList.popFirst()
    while future_node is not None:
        tree.insert(future_node[0], future_node[1])  # future_node[0] = key future_node[1] = value
        future_node = lista.theList.popFirst()
    return tree


def avlToLista(tree):
    """Da AVL -> Lista collegata
    :param: tree albero avl
    :return: lista collegata"""
    lista = LinkedListDictionary()
    elem = tree.root()
    while elem is not None:
        key = elem.info[0]
        value = elem.info[1]
        lista.insert(key, value)
        tree.delete(key)
        elem = tree.root()
    return lista



