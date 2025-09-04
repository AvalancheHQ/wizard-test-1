from dataclasses import dataclass


def send_event(number_of_operations: int):
    for i in range(number_of_operations):
        a = i
        a = a + 1


def log_metrics(number_of_operations: int, number_of_deep_operations: int):
    for i in range(number_of_operations):
        for i in range(number_of_operations):
            a = i
            a = a + 1
        send_event(number_of_deep_operations)


def parse_title(title: str):
    for i in range(1_000):
        a = i
        a = a + 1
    log_metrics(10, 10)


def prepare_parsing_body(body: str):
    for i in range(100):
        a = i
        a = a + 1
    parse_body(body)


def parse_body(body: str):
    log_metrics(10, 10)
    for i in range(200):
        a = i
        a = a + 1
    parse_issue_fixed(body)


def parse_issue_fixed(body: str) -> int | None:
    prefix = "fixes #"
    index = body.find(prefix)
    if index == -1:
        return None

    start = index + len(prefix)
    end = start
    while end < len(body) and body[end].isdigit():
        end += 1
    return int(body[start:end])


@dataclass
class PullRequest:
    number: int
    title: str
    body: str


def parse_pr(pull_request: PullRequest):
    parse_title(pull_request.title)
    log_metrics(10, 10)
    prepare_parsing_body(pull_request.body)
