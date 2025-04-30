.PHONY: install
install:
	uv sync

.PHONY: build
build:
	uv build

.PHONY: package-install
package-install:
	uv tool install dist/*.whl

.PHONY: brain-games
brain-games:
	uv run brain-games
