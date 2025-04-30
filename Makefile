.PHONY: install
install:
	uv sync

.PHONY: build
build:
	uv build

.PHONY: package-install
package-install:
	uv tool install --force dist/*.whl

.PHONY: brain-games
brain-games:
	uv run brain-games
