from summarizer import summarize_text
import sys
import os

# Add the project directory to the system path for module imports
sys.path.append('c:\\Users\\camer\\OneDrive\\Desktop\\coding projects\\Ai Summarizer')

# Read raw text from logs.txt
with open("data/logs.txt", "r") as f:
    raw_text = f.read()

# Summarize the raw text using the summarize_text function
summary = summarize_text(raw_text)

# Print the summary to the console
print("SUMMARY:\n", summary)

# Print the current system path for debugging purposes
print(sys.path)

# Print the current working directory for debugging purposes
print("Current working directory:", os.getcwd())

# Basic test to ensure the summarizer is working
def test_summarizer():
    test_text = "This is a test log entry."
    test_summary = summarize_text(test_text)
    assert "test log" in test_summary, "Test failed: Summary does not contain expected content."

# Run the test
test_summarizer()