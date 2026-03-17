#!/usr/bin/env python3
import sys
import pytest

if __name__ == "__main__":
    # Add pytest-cov arguments if not already provided
    args = sys.argv[1:]
    if "--cov" not in args:
        args.extend(
            [
                "--cov=.",
                "--cov-report=term-missing",
                "--cov-config=src/.coveragerc",
            ]
        )
    sys.exit(pytest.main(args))
