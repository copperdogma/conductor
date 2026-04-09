.PHONY: test lint skills-sync skills-check methodology-compile methodology-check

test:
	python3 scripts/repo_checks.py test

lint:
	python3 scripts/repo_checks.py lint

skills-sync:
	./scripts/sync-agent-skills.sh

skills-check:
	./scripts/sync-agent-skills.sh --check

methodology-compile:
	python3 scripts/methodology_graph.py compile

methodology-check:
	python3 scripts/methodology_graph.py check

