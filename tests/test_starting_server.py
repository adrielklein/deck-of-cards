from unittest.mock import Mock

from flask import Flask

from start_server import start_server


def test_when_user_starts_server_then_app_starts_serving(monkeypatch):
    mocked_run = Mock()
    monkeypatch.setattr(Flask, 'run', mocked_run)
    start_server()
    mocked_run.assert_called_with(host='0.0.0.0', port=5000)
