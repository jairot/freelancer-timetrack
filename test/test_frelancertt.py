"""test for new plugin"""
import unittest
import pbt

from unittest import mock

from io import StringIO

gctx = pbt.global_ctx
gctx.initial_setup()


class fakecookie(object):
    class main():
        def cookiecutter():
            raise NotImplementedError


class NewTestCase(unittest.TestCase):

    def test_new_is_loaded(self):
        self.assertTrue(gctx.is_command("new"))

    def test_template_list(self):
        with mock.patch('sys.stdout', StringIO()) as out:
            gctx.run("new", ["list"])
            output = out.getvalue().strip()

        self.assertIn("flask", output)

#    def test_new_default(self):
#        fakecookie.main.cookiecutter = mock.MagicMock()
#        with mock.patch.dict('sys.modules', {"cookiecutter.main": fakecookie.main}):
#            gctx.run("new", [])
#        fakecookie.main.cookiecutter.assert_called_once_with(
#            "https://github.com/jairot/cookiecutter-simplepypackage")
#
#    def test_new_django(self):
#        fakecookie.main.cookiecutter = mock.MagicMock()
#        with mock.patch.dict('sys.modules', {"cookiecutter.main": fakecookie.main}):
#            gctx.run("new", ["django"])
#        fakecookie.main.cookiecutter.assert_called_once_with(
#            "https://github.com/pydanny/cookiecutter-django")
#
#    def test_new_flask(self):
#        fakecookie.main.cookiecutter = mock.MagicMock()
#        with mock.patch.dict('sys.modules', {"cookiecutter.main": fakecookie.main}):
#            gctx.run("new", ["flask"])
#        fakecookie.main.cookiecutter.assert_called_once_with(
#            "https://github.com/sloria/cookiecutter-flask")
#
#    def test_new_custom(self):
#        fakecookie.main.cookiecutter = mock.MagicMock()
#        with mock.patch.dict('sys.modules', {"cookiecutter.main": fakecookie.main}):
#            gctx.run("new", ["https://github.com/god/thisrepodoesnotexist"])
#        fakecookie.main.cookiecutter.assert_called_once_with(
#            "https://github.com/god/thisrepodoesnotexist")

    def test_new_update(self):
        gctx.fetch_plugin_file = mock.MagicMock()
        gctx.run("new", ["update"])
        gctx.fetch_plugin_file.assert_called_once_with("new", "templates.json")

    def test_new_update_and_list(self):
        gctx.fetch_plugin_file = mock.MagicMock()
        gctx.run("new", ["update", "list"])
        gctx.fetch_plugin_file.assert_called_once_with("new", "templates.json")
