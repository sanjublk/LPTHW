class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, directions):
        return self.paths.get(directions, None)

    def add_paths(self, paths):
        self.paths.update(paths)
