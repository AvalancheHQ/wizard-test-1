import pytest
from parse_pr import PullRequest, parse_pr


body = open("tests/pr_body.txt").read()


@pytest.mark.benchmark
def test_parse_pr(benchmark):
    @benchmark
    def _():
        parse_pr(
            PullRequest(
                number=1,
                title="title",
                body=body,
            )
        )
