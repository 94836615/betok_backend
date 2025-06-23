# Tests for Betok

This directory contains unit tests for the Betok application.

## Test Structure

- `conftest.py`: Contains pytest fixtures used across multiple test files
- `test_models.py`: Tests for the database models
- `test_videos_api.py`: Tests for the videos API endpoints
- `test_crud_operations.py`: Tests for CRUD operations

## Running Tests

You can run the tests using the following command from the project root:

```bash
pytest
```

Or using the Makefile:

```bash
make run_test
```

## Adding New Tests

When adding new tests, follow these guidelines:

1. Create test files with the prefix `test_`
2. Create test functions with the prefix `test_`
3. Use the fixtures defined in `conftest.py` when possible
4. Follow the Arrange-Act-Assert pattern in your tests
5. For async tests, use the `@pytest.mark.asyncio` decorator

## Mocking

The tests use mocking to isolate the code being tested from external dependencies:

- Database: Uses an in-memory SQLite database
- MinIO: Uses unittest.mock to mock the MinIO client
- External services: Should be mocked as needed