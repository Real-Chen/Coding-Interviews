# 面试题37：序列化二叉树

# 二叉树数据结构
class BinaryTreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# 序列化：树->序列
def serialize(root):
    serial = []
    if not root:
        serial.append(None)
    else:
        serial.append(root.val)
        serial += serialize(root.left)
        serial += serialize(root.right)
    return serial

# 反序列化：序列->树
def deserialize(serial):
    if not serial:
        return
    val = serial.pop(0)
    if not val:
        return None
    node = BinaryTreeNode(val)
    node.left = deserialize(serial)
    node.right = deserialize(serial)
    return node

if __name__ == '__main__':
    serial = [1, 2, 4, None, None, None, 3, 5, None, None, 6, None, None]
    root = deserialize(serial)
    print(serialize(root))
