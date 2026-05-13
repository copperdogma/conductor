.PHONY: test lint skills-sync skills-check methodology-compile methodology-check supply-chain-scan

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

supply-chain-scan:
	python3 scripts/npm_supply_chain_scan.py --projects projects.yaml --include-root --project-key conductor --project-name Conductor
