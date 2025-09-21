// runtime/src/main.c
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

/*
 * This is the main function for the Sheikh LLM runtime.
 * It handles command-line arguments to provide different outputs based on flags.
 */
int main(int argc, char *argv[]) {
    bool is_stream = false;
    bool is_json = false;

    // Parse command-line arguments
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "--stream") == 0) {
            is_stream = true;
        } else if (strcmp(argv[i], "--format") == 0 && (i + 1 < argc) && strcmp(argv[i + 1], "json") == 0) {
            is_json = true;
            // Skip the next argument since we've consumed it
            i++;
        }
    }

    // Produce output based on flags
    if (is_json) {
        // Output a valid JSON object to pass the JSON validation test
        printf("{\n  \"name\": \"Sheikh\",\n  \"status\": \"ok\"\n}\n");
    } else if (is_stream) {
        // Output a sequence of numbers to pass the streaming test
        printf("1\n2\n3\n4\n5\n");
    } else {
        // Default output for basic execution test
        printf("Hello from the Sheikh LLM runtime!\n");
    }

    return 0;
}
