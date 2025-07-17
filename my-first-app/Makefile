# Makefile for the Hello Env project

# Use.PHONY to declare targets that are not files, preventing conflicts.
.PHONY: build

# Define variables for consistency and easy updates.
IMAGE_NAME := hello-env
IMAGE_TAG  := latest

# The 'build' target recipe.
build:
	@echo "Building Docker image: $(IMAGE_NAME):$(IMAGE_TAG)..."
	@docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
	@echo "Build complete. Image: $(IMAGE_NAME):$(IMAGE_TAG)"