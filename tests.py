"""
Test the Sprockets Command Line Interface

"""
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import mock

from sprockets import cli


class Package(object):

    def __init__(self, name, module_name):
        self.name = name
        self.module_name = module_name


class InitializationTests(unittest.TestCase):

    @mock.patch('argparse.ArgumentParser.parse_args')
    @mock.patch('pkg_resources.iter_entry_points')
    def setUp(self, iter_entry_points, parse_args):
        self.iter_entry_points = iter_entry_points
        self.parse_args = parse_args

        self.app_points = [Package('tapp', 'sstubs.app')]
        self.ctrl_points = [Package('tcontroller', 'sstubs.controller')]
        self.plugin_points = [Package('tplugin', 'sstubs.plugin')]

        def entry_point_side_effect(*args, **kwargs):
            if kwargs.get('group') == 'sprockets.controller':
                return iter(self.ctrl_points)
            elif kwargs.get('group') == 'sprockets.plugin':
                return iter(self.plugin_points)
            elif kwargs.get('group') == 'sprockets.test_http.app':
                return iter(self.app_points)

        self.iter_entry_points.side_effect = entry_point_side_effect
        self.obj = cli.CLI()

    def test_pkg_resources_iterated(self):
        calls = [mock.call(group='sprockets.controller'),
                 mock.call(group='sprockets.plugin')]
        self.iter_entry_points.assert_has_calls(calls)

    def test_controller_imported(self):
        for attr in ['add_cli_arguments', 'main']:
            self.assertTrue(hasattr(self.obj._controllers.get('tcontroller'),
                                    attr))

    def test_plugin_is_imported(self):
        for attr in ['initialize', 'on_start', 'on_shutdown']:
            self.assertTrue(hasattr(self.obj._plugins.get('tplugin'), attr))



