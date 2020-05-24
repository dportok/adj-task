MAJOR?=0
MINOR?=1

VERSION=$(MAJOR).$(MINOR)

DOCKER_IMAGE_NAME = adjust:$(VERSION)


default: build

all: build pep8 pylint test

build:
	@echo "#"
	@echo "# 🐳 Building the image for the CLI tool"
	@echo "#"
	@docker build -t $(DOCKER_IMAGE_NAME) .

pep8: build
	@echo "#"
	@echo "# 🔎 Cheking code syntax using pep8"
	@echo "#"
	@docker run --rm \
	--entrypoint sh \
	$(DOCKER_IMAGE_NAME) -c "pep8 adjust.py"

pylint: build pep8
	@echo "#"
	@echo "# 🔎 Cheking code syntax using pylint"
	@echo "#"
	@docker run --rm \
	--entrypoint sh \
	$(DOCKER_IMAGE_NAME) -c "pylint adjust.py"

test: build
	@echo "#"
	@echo "# 💥 Running unit tests"
	@echo "#"
	@docker run --rm \
	--network="host" \
	--entrypoint sh \
	$(DOCKER_IMAGE_NAME) -c "pytest test_adjust.py"