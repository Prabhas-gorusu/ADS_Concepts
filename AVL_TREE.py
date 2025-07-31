class TreeNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    if node is None:
        return 0
    return node.height

def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = max(height(y.left), height(y.right)) + 1
    x.height = max(height(x.left), height(x.right)) + 1

    return x

def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = max(height(x.left), height(x.right)) + 1
    y.height = max(height(y.left), height(y.right)) + 1

    return y

def get_balance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

def insert(root, key):
    if not root:
        return TreeNode(key)
    elif key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    balance = get_balance(root)

    if balance > 1 and key < root.left.data:
        return right_rotate(root)
    if balance < -1 and key > root.right.data:
        return left_rotate(root)
    if balance > 1 and key > root.left.data:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and key < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete_node(root, key):
    if not root:
        return root

    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None or root.right is None:
            temp = root.left if root.left else root.right
            if temp is None:
                temp = root
                root = None
            else:
                root = temp
        else:
            temp = min_value_node(root.right)
            root.data = temp.data
            root.right = delete_node(root.right, temp.data)

    if root is None:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    balance = get_balance(root)

    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.data, end=" ")
        in_order_traversal(root.right)

def free_avl_tree(root):
    if root:
        free_avl_tree(root.left)
        free_avl_tree(root.right)
        del root

def main():
    root = None
    running = True
    while running:
        print("\nAVL Tree Operations:")
        print("1. Insert a node")
        print("2. Delete a node")
        print("3. In-order Traversal")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter the key to insert: "))
            root = insert(root, key)
        elif choice == 2:
            key = int(input("Enter the key to delete: "))
            root = delete_node(root, key)
        elif choice == 3:
            print("In-order Traversal: ", end="")
            in_order_traversal(root)
            print()
        elif choice == 4:
            free_avl_tree(root)
            print("Exiting...")
            running = False
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
