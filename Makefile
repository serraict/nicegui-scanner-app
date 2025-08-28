.PHONY: help install build clean test publish dev dev-pages version releasable release-next-patch release-next-minor 

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install:  ## Install package in editable mode
	uv sync
	uv pip install -e .

build:  ## Build package for distribution
	python copy_zxing.py
	uv build

clean:  ## Clean build artifacts
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

test:  ## Test the package installation
	cd examples && uv run python app.py &
	@echo "Example app started at http://localhost:3001"
	@echo "Press Ctrl+C to stop"

publish:  ## Publish to PyPI (requires PyPI token)
	@echo "Building package..."
	uv build
	@echo "Publishing to PyPI..."
	uv publish
	@echo "Package published successfully!"

dev:
	cd examples && uv run python app.py

dev-pages:
	cd examples && uv run python pages.py

# Get current version from git describe (same logic as uv build)
GIT_VERSION := $(shell git describe --tags 2>/dev/null || echo "v0.0.0")
BASE_VERSION := $(shell echo $(GIT_VERSION) | sed 's/^v//' | sed 's/-.*//')
NEXT_PATCH := $(shell echo $(BASE_VERSION) | awk -F. '{$$3=$$3+1; print $$1"."$$2"."$$3}')
NEXT_MINOR := $(shell echo $(BASE_VERSION) | awk -F. '{$$2=$$2+1; $$3=0; print $$1"."$$2"."$$3}')

version:
	@echo "Git describe: $(GIT_VERSION)"
	@echo "Base version: $(BASE_VERSION)"
	@echo "Next patch: $(NEXT_PATCH)"
	@echo "Next minor: $(NEXT_MINOR)"

releasable:
	@if [ -n "$$(git status --porcelain)" ]; then \
		echo "There are uncommitted changes or untracked files"; \
		exit 1; \
	fi
	@if [ "$$(git rev-parse --abbrev-ref HEAD)" != "main" ]; then \
		echo "Not on main branch"; \
		exit 1; \
	fi
	@if [ "$$(git rev-parse HEAD)" != "$$(git rev-parse origin/main)" ]; then \
		echo "Local branch is ahead of origin"; \
		exit 1; \
	fi

release-next-patch: releasable  ## Release next patch version
	@echo "Releasing patch version $(NEXT_PATCH)..."
	git tag "v$(NEXT_PATCH)"
	git push origin main --tags
	@echo "Released v$(NEXT_PATCH)"

release-next-minor: releasable  ## Release next minor version
	@echo "Releasing minor version $(NEXT_MINOR)..."
	git tag "v$(NEXT_MINOR)"
	git push origin main --tags
	@echo "Released v$(NEXT_MINOR)"

release: release-next-patch