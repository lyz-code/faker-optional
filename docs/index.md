[![Actions Status](https://github.com/lyz-code/faker-optional/workflows/Tests/badge.svg)](https://github.com/lyz-code/faker-optional/actions)
[![Actions Status](https://github.com/lyz-code/faker-optional/workflows/Build/badge.svg)](https://github.com/lyz-code/faker-optional/actions)
[![Coverage Status](https://coveralls.io/repos/github/lyz-code/faker-optional/badge.svg?branch=master)](https://coveralls.io/github/lyz-code/faker-optional?branch=master)

Wrapper over other Faker providers to return their value or `None`. Useful to
create data of type `Optional[Any]`.

# Installing

```bash
pip install faker-optional
```

# A Simple Example

```python
from faker import Faker
from faker_optional import OptionalProvider

fake = Faker()
fake.add_provider(OptionalProvider)

fake.optional_int()
# None

fake.optional_int()
# 1234
```

# Usage

`OptionalProvider` uses existent faker providers to create the data, so you can
use the provider method arguments.

For example, `optional_int` uses the [`python provider
pyint`](https://faker.readthedocs.io/en/master/providers/faker.providers.python.html#faker.providers.python.Provider.pyint),
so you can use the `min_value`, `max_value`, and `step` arguments. Every
`optional_` method accepts the float `ratio` argument between `0` and `1`, with
a default value of `0.5` to define what percent of results should be `None`,
a greater value will mean that less results will be `None`.

Check the [supported methods](reference.md). If you want one that's not
included, it's really easy to implement it yourself, [please make a pull
request](contributing.md).
# References

As most open sourced programs, `faker-optional` is standing on the shoulders of
giants, namely:

[Pytest](https://docs.pytest.org/en/latest)
: Testing framework, enhanced by the awesome
    [pytest-cases](https://smarie.github.io/python-pytest-cases/) library that made
    the parametrization of the tests a lovely experience.

[Mypy](https://mypy.readthedocs.io/en/stable/)
: Python static type checker.

[Flakehell](https://github.com/life4/flakehell)
: Python linter with [lots of
    checks](https://lyz-code.github.io/blue-book/devops/flakehell/#plugins).

[Black](https://black.readthedocs.io/en/stable/)
: Python formatter to keep a nice style without effort.

[Autoimport](https://github.com/lyz-code/autoimport)
: Python formatter to automatically fix wrong import statements.

[isort](https://github.com/timothycrosley/isort)
: Python formatter to order the import statements.

[Pip-tools](https://github.com/jazzband/pip-tools)
: Command line tool to manage the dependencies.

[Mkdocs](https://www.mkdocs.org/)
: To build this documentation site, with the
[Material theme](https://squidfunk.github.io/mkdocs-material).

[Safety](https://github.com/pyupio/safety)
: To check the installed dependencies for known security vulnerabilities.

[Bandit](https://bandit.readthedocs.io/en/latest/)
: To finds common security issues in Python code.

[Yamlfix](https://github.com/lyz-code/yamlfix)
: YAML fixer.

# Contributing

For guidance on setting up a development environment, and how to make
a contribution to *faker-optional*, see [Contributing to
faker-optional](https://lyz-code.github.io/faker-optional/contributing).
