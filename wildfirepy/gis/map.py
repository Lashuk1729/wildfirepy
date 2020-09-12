import h5py
from wildfirepy.gis.mapfactory import MapFactory

__all__ = ['Map']


class Map(MapFactory):

    def __init__(self, data=None, **kwargs):
        super().__init__(data, **kwargs)
        if data is None and len(kwargs) == 0:
            raise ValueError

        self.data = self.load_data()

    def _get_all_objects(self, data):
        h5_objs = []
        data.visit(h5_objs.append)
        return h5_objs

    def _get_all_datasets(self, data):
        grids = self.Viirs1KmLoader.get_grids(data)
        h5_objs = self._get_all_objects(data)
        all_datasets = [obj for grid in grids for obj in h5_objs if isinstance(data[obj], h5py.Dataset) and grid in obj]
        return all_datasets

    def get_all_fire_objects(self):
        return self._get_all_objects(self.data['fire'])

    def get_all_fire_datasets(self):
        return self._get_all_datasets(self.data['fire'])
