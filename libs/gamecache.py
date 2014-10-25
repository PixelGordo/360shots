import os

import xcrapper

s_CACHE_FILE = os.path.join('media', 'gamecache.txt')


class Database:
    def __init__(self):
        self._ds_entries = {}

        if os.path.isfile(s_CACHE_FILE):
            self._load_data()

        else:
            o_file = open(s_CACHE_FILE, 'w')
            o_file.close()

    def _load_data(self):
        """
        Method to read all the cached information (id and title) from the offline database.

        :return: Nothing
        """

        o_file = open(s_CACHE_FILE, 'r')

        for s_line in o_file:
            s_line = s_line.strip()
            s_id = s_line.partition('\t')[0]
            s_title = s_line.partition('\t')[2]

            self._ds_entries[s_id] = s_title

        o_file.close()

    def _write_data(self):
        """
        Method to save the cached database to disk.

        :return: Nothing
        """

        ld_data_elements = []

        for s_key, s_value in self._ds_entries.iteritems():
            d_data_element = {'id': s_key, 'title': s_value}
            ld_data_elements.append(d_data_element)

        ld_data_elements = sorted(ld_data_elements, key=lambda d_data_element: d_data_element['title'])

        o_file = open(s_CACHE_FILE, 'w')

        for d_data_element in ld_data_elements:
            o_file.write('%s\t%s\n' % (d_data_element['id'], d_data_element['title']))

        o_file.close()

    def get_title_by_id(self, s_id):

        try:
            s_title = self._ds_entries[s_id]

        except KeyError:
            s_title = xcrapper.id_to_title(s_id)

            self._ds_entries[s_id] = s_title
            self._write_data()

        return s_title

    def get_id_by_title(self, s_title):
        pass

    def get_items(self):
        return len(self._ds_entries)