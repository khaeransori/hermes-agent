"""khaeransori/pstack-hermes is a default tap and its provider label is a working --source filter."""

import argparse

from hermes_cli.subcommands.skills import build_skills_parser
from tools.skills_hub_github import GitHubAuth, GitHubSource, _provider_filter_of, github_provider_for


def test_pstack_tap_label_is_an_accepted_source_filter():
    repos = {t["repo"] for t in GitHubSource(GitHubAuth()).taps}
    assert "khaeransori/pstack-hermes" in repos
    label = github_provider_for("khaeransori/pstack-hermes")
    assert label
    assert _provider_filter_of(label.lower()) == label.lower()

    parser = argparse.ArgumentParser(prog="hermes")
    build_skills_parser(parser.add_subparsers(dest="command"), cmd_skills=lambda a: None)
    assert parser.parse_args(["skills", "search", "x", "--source", label.lower()]).source == label.lower()
