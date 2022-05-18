from collections import defaultdict


class RouteTrie:
    def __init__(self, handler):
        self.root = RouteTrieNode(handler)

    def insert(self, paths, handler):
        current_node = self.root
        for path in paths:
            current_node.insert(path)
            current_node = current_node.children[path]
        current_node.handler = handler

    def find(self, paths):
        current_node = self.root
        for path in paths:
            if path not in current_node.children:
                return None
            else:
                current_node = current_node.children[path]
        return current_node.handler


class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler

    def insert(self, path):
        self.children[path] = RouteTrieNode()


class Router:
    def __init__(self, handler, not_found_handler):
        self.routeTrie = RouteTrie(handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        self.routeTrie.insert(self.split_path(path), handler)

    def lookup(self, path):
        handler = self.routeTrie.find(self.split_path(path))

        return self.not_found_handler if handler is None else handler 

    def split_path(self, path):
        path = path.replace("/", "")
        return path.split("/") if path else []

##Testcase

router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler'
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler'
print(router.lookup("/home/about/me")) # should print 'not found handler'

assert router.lookup("/") == "root handler"
assert router.lookup("/home") == "not found handler"
assert router.lookup("/home/about") == "about handler"
assert router.lookup("/home/about/") == "about handler"
assert router.lookup("/home/about/me") == "not found handler"
assert router.lookup("") == "root handler"
assert router.lookup("/home/about/us") == "not found handler"