.PHONY: methodology-compile methodology-check skills-sync skills-check facts package-check
methodology-compile:
	python3 scripts/methodology_graph.py compile
methodology-check:
	python3 scripts/methodology_graph.py check
skills-sync:
	bash scripts/sync-agent-skills.sh
skills-check:
	bash scripts/sync-agent-skills.sh --check
facts:
	python3 scripts/triage_facts.py --json
package-check: methodology-check skills-check
	python3 .agents/skills/setup-methodology/scripts/package.py audit
