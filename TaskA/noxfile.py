import nox


@nox.session(python=["3.9"])
def tests(session):
    session.install("pytest")
    session.run("pytest", "app_test.py")


@nox.session(python=["3.9"])
def lint(session):
    session.install("flake8")
    session.run("flake8", "bubbleSort.py")