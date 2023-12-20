#!/usr/bin/python3
""" """
import unittest
import os
import sys
import json
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class test_console(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'HBNBCommand'

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        """ """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_create_default(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            self.assertTrue(os.path.exists('file.json'))
            output = f.getvalue().strip()
            with open('file.json', 'r') as f:
                file = json.load(f)
                self.assertTrue('BaseModel.' + output in file.keys())

    def test_create_kwargs_correct(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place name=\"California\"')
            self.assertTrue(os.path.exists('file.json'))
            output = f.getvalue().strip()
            with open('file.json', 'r') as f:
                file = json.load(f)
                self.assertTrue('Place.' + output in file.keys())
                self.assertEqual(file['Place.' + output]['name'], 'California')

    def test_create_kwargs_incorrect(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place amenity_ids=3')
            self.assertTrue(os.path.exists('file.json'))
            output = f.getvalue().strip()
            with open('file.json', 'r') as f:
                file = json.load(f)
                self.assertTrue('Place.' + output in file.keys())
                with self.assertRaises(KeyError):
                    file['Place.' + output]['amenity_ids']

    def test_create_kwargs_int(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place number_rooms=3')
            self.assertTrue(os.path.exists('file.json'))
            output = f.getvalue().strip()
            with open('file.json', 'r') as f:
                file = json.load(f)
                self.assertTrue('Place.' + output in file.keys())
                self.assertEqual(file['Place.' + output]['number_rooms'], 3)

    def test_create_kwargs_float(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place latitude=3.14')
            self.assertTrue(os.path.exists('file.json'))
            output = f.getvalue().strip()
            with open('file.json', 'r') as f:
                file = json.load(f)
                self.assertTrue('Place.' + output in file.keys())
                self.assertEqual(file['Place.' + output]['latitude'], 3.14)

    def test_create_kwargs_str_with_space(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place name=\"New_York\"')
            self.assertTrue(os.path.exists('file.json'))
            output = f.getvalue().strip()
            with open('file.json', 'r') as f:
                file = json.load(f)
                self.assertTrue('Place.' + output in file.keys())
                self.assertEqual(file['Place.' + output]['name'], 'New York')

    def test_create_kwargs_types(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place city_id=\"0001\"')
            self.assertTrue(os.path.exists('file.json'))
            output = f.getvalue().strip()
            with open('file.json', 'r') as f:
                file = json.load(f)
                self.assertTrue('Place.' + output in file.keys())
                self.assertEqual(type(file['Place.' + output]['city_id']), str)
                self.assertEqual(file['Place.' + output]['city_id'], '0001')

    def test_create_kwargs_multiple(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place name=\"California\"\
                                  city_id=\"0001\"')
            self.assertTrue(os.path.exists('file.json'))
            output = f.getvalue().strip()
            with open('file.json', 'r') as f:
                file = json.load(f)
                self.assertTrue('Place.' + output in file.keys())
                self.assertEqual(file['Place.' + output]['name'], 'California')
                self.assertEqual(file['Place.' + output]['city_id'], '0001')
