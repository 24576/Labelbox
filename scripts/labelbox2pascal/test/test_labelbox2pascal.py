import json
import os

import labelbox2pascal as lb2pa
import pytest
import xmltodict

class TestFromJSON():
    def results_output(self):
        TEST_OUTPUT_DIR = 'test-results'
        if not os.path.isdir(TEST_OUTPUT_DIR):
            os.makedirs(TEST_OUTPUT_DIR)
        return TEST_OUTPUT_DIR

    def test_wkt_1(self):
        lb2pa.from_json('test-fixtures/labelbox_1.json', self.results_output(),
                        self.results_output())

    def test_wkt_2(self):
        lb2pa.from_json('test-fixtures/labelbox_2.json', self.results_output(),
                        self.results_output())
    def test_v2_wkt(self):
        lb2pa.from_json('test-fixtures/v2_wkt.json', self.results_output(),
                        self.results_output())

    def test_v3_wkt(self):
        lb2pa.from_json('test-fixtures/v2_wkt.json', self.results_output(),
                        self.results_output())

    def test_xy_1(self):
        lb2pa.from_json('test-fixtures/labelbox_xy_1.json',
                        self.results_output(), self.results_output(),
                        label_format='XY')
    def test_v3_xy(self):
        lb2pa.from_json('test-fixtures/v2_wkt.json', self.results_output(),
                        self.results_output())

    def test_v3_wkt_bndbox(self):
        fixture = 'test-fixtures/v3_wkt_rectangle.json'
        with open(fixture, 'r') as f:
            annotation_file_path = self.results_output() + '/' + json.load(f)[0]['ID'] + '.xml'

        lb2pa.from_json(fixture,
                        self.results_output(), self.results_output(),
                        label_format='WKT')

        with open(annotation_file_path, 'r') as f:
            annotation = xmltodict.parse(f.read())
            assert 'bndbox' in annotation['annotation']['object']

    def test_bad_label_format(self):
        with pytest.raises(lb2pa.UnknownFormatError):
            lb2pa.from_json('test-fixtures/labelbox_xy_1.json',
                            self.results_output(), self.results_output(),
                            label_format='INVALID')
