class NEODatabase:
    def __init__(self, neos, approaches):
        self._neos = neos
        self._approaches = approaches

        self._pdes_to_index = {}
        for index, neo in enumerate(self._neos):
            self._pdes_to_index[neo.designation] = index

        for approach in self._approaches:
            if approach.designation in self._pdes_to_index.keys():
                approach.neo = self._neos[self._pdes_to_index[approach.designation]]
                self._neos[self._pdes_to_index[approach.designation]
                           ].approaches.append(approach)

        self._des_to_neo = {}
        for neo in self._neos:
            self._des_to_neo[neo.designation] = neo
        self.name_to_neo = {}
        for neo in self._neos:
            self.name_to_neo[neo.name] = neo

    def get_neo_by_designation(self, designation):
        return self._des_to_neo.get(designation.upper(), None)

    def get_neo_by_name(self, name):
        return self.name_to_neo.get(name.capitalize(), None)

    def query(self, filters=()):
        if filters:
            for approach in self._approaches:
                all_pass = True
                for f in filters:
                    if not f(approach):
                        all_pass = False
                        break
                if all_pass:
                    yield approach
        else:
            for approach in self._approaches:
                yield approach
