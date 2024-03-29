

class TSTNode:
    def __init__(self, data="") -> None:
        self.data = data
        self.isend: bool = False
        self.eq = None
        self.left = None
        self.right = None



class TST:
    def __init__(self) -> None:
        self.root = None
    
    def is_empty(self):
        return self.root is None
 
    def search(self, root, key):
        if root is None:
            return False
        #
        if ord(key[0]) < ord(root.data): 
            return self.search(root.left, key[:])
        elif ord(key[0]) > ord(root.data): 
            return self.search(root.right, key[:])
        #
        else:
            if len(key) > 1:
                return self.search(root.eq, key[1:])
            else:
                if root.isend == True:
                    return True
                else:
                    return False
        

    def insert(self, root, word):
        """word most be str"""
        if not isinstance(word, str):
            raise TypeError(f"TST.insert() expected string, but {type(word)} found")
        if len(word) == 0:
            return None
        #
        if not root:
            root = TSTNode(word[0])
        #
        temp = root
        while len(word) > 0:
            if ord(temp.data) > ord(word[0]):
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = TSTNode(word[0])
                    temp = temp.left
            #
            if ord(temp.data) < ord(word[0]):
                if temp.right:
                    temp = temp.right
                else:
                    temp.right = TSTNode(word[0])
                    temp = temp.right
            #
            else:
                if len(word) == 1:
                    temp.isend = True
                    break
                else:
                    if temp.eq:
                        temp = temp.eq
                        word = word[1:]
                    else:
                        temp.eq = TSTNode(word[1])
                        temp = temp.eq
                        word = word[1:]
        #
        return root
    
    # End of class


def traverseTSTUtil(root, buffer, depth): 
    if root: 
        traverseTSTUtil(root.left, buffer, depth) 
        buffer[depth] = root.data 
        if root.isend: 
            print("".join(buffer[:depth+1])) 
        traverseTSTUtil(root.eq, buffer, depth+1) 
        traverseTSTUtil(root.right, buffer, depth) 


def traverseTST(root): 
    buffer = [''] * 50
    traverseTSTUtil(root, buffer, 0) 


def show_same_prefix_Util(root, key, depth):
    if root is None:
        return False
    #
    if ord(key[0]) < ord(root.data): 
        return show_same_prefix_Util(root.left, key[:], depth)
    elif ord(key[0]) > ord(root.data): 
        return show_same_prefix_Util(root.right, key[:], depth)
    #
    else:
        if len(key) > 1:
            return show_same_prefix_Util(root.eq, key[1:], depth+1)
        if len(key) == 1:
            buffer = [''] * 50
            traverseTSTUtil(root.eq, buffer, depth)

def show_same_prefix(root, word):
    show_same_prefix_Util(root, key=word, depth=0)

                
            
            


tst = TST()

tst.root = tst.insert(tst.root, "0")
tst.root = tst.insert(tst.root, "01")
tst.root = tst.insert(tst.root, "012")
tst.root = tst.insert(tst.root, "0123")
tst.root = tst.insert(tst.root, "01234")
tst.root = tst.insert(tst.root, "012345")
# print(tst.search(tst.root, "012"))
# print(tst.search(tst.root, "acd"))
# print(tst.search(tst.root, "1cd"))
# traverseTST(tst.root)
show_same_prefix(tst.root, "012")

