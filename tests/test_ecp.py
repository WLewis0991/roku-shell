from unittest.mock import patch, Mock
import typer
import pytest
import requests
from roku_shell.ecp import press_key


@patch("roku_shell.ecp.requests.post")
def test_press_key_success(mock_post):
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_post.return_value = mock_response

    press_key("192.168.1.100", "Home")

    mock_post.assert_called_once_with(
        "http://192.168.1.100:8060/keypress/Home", timeout=5
    )


@patch("roku_shell.ecp.requests.post")
def test_press_key_connection_error(mock_post):
    mock_post.side_effect = requests.ConnectionError("Connection refused")

    with pytest.raises(typer.Exit) as exc_info:
        press_key("192.168.1.100", "Home")

    assert exc_info.value.exit_code == 1


@patch("roku_shell.ecp.requests.post")
def test_press_key_http_error(mock_post):
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
    mock_post.return_value = mock_response

    with pytest.raises(typer.Exit) as exc_info:
        press_key("192.168.1.100", "Home")

    assert exc_info.value.exit_code == 1


@patch("roku_shell.ecp.requests.post")
def test_press_key_timeout(mock_post):
    mock_post.side_effect = requests.Timeout("Request timed out")

    with pytest.raises(typer.Exit) as exc_info:
        press_key("192.168.1.100", "Home")

    assert exc_info.value.exit_code == 1
