.PHONY: help install build clean test publish dev

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install:  ## Install package in editable mode
	uv sync
	uv pip install -e .

build:  ## Build package for distribution
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

dev:  ## Run example app in development mode
	cd examples && uv run python app.py

version:  ## Show current version
	@uv run python -c "import nicegui_scanner; print(f'Version: {nicegui_scanner.__version__}')"

tag:  ## Create and push version tag (usage: make tag VERSION=v0.1.0)
	@if [ -z "$(VERSION)" ]; then echo "Usage: make tag VERSION=v0.1.0"; exit 1; fi
	git tag $(VERSION)
	git push origin $(VERSION)
	@echo "Tag $(VERSION) created and pushed"