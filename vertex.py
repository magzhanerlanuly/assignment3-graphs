class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id

    def get_id(self):
        return self.id

    def __str__(self):
        return str(self.id)