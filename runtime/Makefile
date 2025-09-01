# Makefile for Sheikh Runtime

# Compiler and flags
CC = gcc
CFLAGS = -O2 -Wall -Wextra -pthread
LDFLAGS = -lm

# Source files and target binary
SRC_DIR = src
SRC_FILES = $(wildcard $(SRC_DIR)/*.c)
TARGET = sheikh

# Default target
all: build

# Build the runtime
build: $(TARGET)

$(TARGET): $(SRC_FILES)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC_FILES) $(LDFLAGS)

# Clean up build artifacts
clean:
	rm -f $(TARGET)

# Run the runtime (for testing)
run: build
	./$(TARGET) --model ../model/sheikh.gguf --prompt "Hello, Sheikh!"

# Install the runtime
install: build
	install -m 755 $(TARGET) /usr/local/bin/

.PHONY: all build clean run install
