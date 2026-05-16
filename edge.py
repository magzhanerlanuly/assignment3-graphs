class Edge:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination

    def __str__(self):
        return f"{self.source} -> {self.destination}"