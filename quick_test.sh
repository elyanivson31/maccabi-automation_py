#!/bin/bash
# Quick test runner for encryption setup
# Run this script to verify that encryption is working correctly

echo "=================================="
echo "Quick Encryption Test Runner"
echo "=================================="
echo ""

# Check if encryption key is set
if [ -z "$TEST_DATA_ENCRYPTION_KEY" ]; then
    echo "⚠️  WARNING: TEST_DATA_ENCRYPTION_KEY is not set!"
    echo ""
    echo "Please set it first:"
    echo "  export TEST_DATA_ENCRYPTION_KEY='your-key-here'"
    echo ""
    echo "Or add it to your ~/.bashrc or ~/.zshrc"
    echo ""
    exit 1
fi

echo "✓ Encryption key is set"
echo ""

# Run verification script
echo "Running comprehensive verification..."
echo ""
python3 verify_encryption.py

exit_code=$?

if [ $exit_code -eq 0 ]; then
    echo ""
    echo "✓ All encryption tests passed!"
else
    echo ""
    echo "✗ Some tests failed. Please check the output above."
fi

exit $exit_code
