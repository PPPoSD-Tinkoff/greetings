from greetings import greet


def test_greet_the_world():
    assert greet("world") == "Hello, world!"
