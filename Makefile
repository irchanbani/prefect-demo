.PHONY: prepare-dev
prepare-dev:
	@echo "Preparing your development environment..."; \
	PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --dev
