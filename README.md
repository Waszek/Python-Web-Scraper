# Python Scraper Project

A Python learning project that demonstrates web scraping, API client interactions, database operations, and unit testing practices.

## Project Structure

This project contains the following Python files organized by functionality:

---

## Core Modules

### **api_client.py**

Fetches data from external APIs and stores it in a SQLite database.

**Key Functions:**

- `extract_company_name(user_data)` - Extracts the company name from user data dictionary
- `main()` - Fetches users from JSONPlaceholder API and stores them in the database
- `fetch_and_save_posts()` - Fetches posts from JSONPlaceholder API and stores them in the database

**Behavior:**

- Connects to the JSONPlaceholder public API (`https://jsonplaceholder.typicode.com`)
- Retrieves a list of users and their company information
- Retrieves a list of posts with user associations
- Handles connection errors and HTTP errors gracefully with try-except blocks
- Initializes the database before fetching data
- Inserts each user and post into the SQLite database

**Error Handling:**

- Catches `ConnectionError` if the server cannot be reached
- Catches `HTTPError` for HTTP-related issues
- Validates that data was received before processing

---

### **db_example.py**

Manages SQLite database operations for users and posts.

**Key Functions:**

- `init_database()` - Creates the users and posts tables if they don't exist
- `add_user(name, company)` - Inserts a new user record into the users table
- `add_post(title, body, user_id)` - Inserts a new post record with a foreign key to the user
- `get_all_users()` - Retrieves and prints all users from the database
- `get_all_posts()` - Retrieves and prints all posts from the database
- `get_users_with_posts()` - Performs an INNER JOIN to display users with their posts (limited to 10 records)

**Database Schema:**

- **users table**: id (PRIMARY KEY), name (TEXT), company (TEXT)
- **posts table**: id (PRIMARY KEY), title (TEXT), body (TEXT), user_id (FOREIGN KEY to users.id)

**Behavior:**

- Uses SQLite with a local database file (`my_database.db`)
- Uses parameterized queries to prevent SQL injection
- Each operation opens and closes its own database connection
- Creates a formatted report when displaying users with their posts

---

### **scraper.py**

Web scraper that extracts job offers from a website and exports them to CSV.

**Key Functions:**

- `main()` - Scrapes job offers and saves them to a CSV file

**Behavior:**

- Makes HTTP request to `https://realpython.github.io/fake-jobs/`
- Uses BeautifulSoup to parse HTML and find job listings
- Extracts job title (h2 with class "title") and company name (h3 with class "company")
- Creates a CSV file (`job_offers.csv`) with columns: Title, Company
- Prints each job offer to the console while writing to the CSV file
- Validates HTTP status code (must be 200)

**Error Handling:**

- Checks for non-200 HTTP status codes and prints an error message

---

### **validator_posts.py**

Validates post data before insertion into the database.

**Key Functions:**

- `validate_post_title(title)` - Validates that a post title is at least 5 characters long

**Behavior:**

- Returns `True` if the title meets validation requirements
- Raises `ValueError` with message "Title is too short!" if title length is less than 5 characters
- Used to ensure data quality before database insertion

---

## Test Modules

### **test_db.py**

Unit tests for database operations using pytest.

**Key Tests:**

- `test_insert_users_to_database(db_session)` - Tests inserting a user into an in-memory SQLite database
  - Verifies that one record was inserted
  - Validates the user's name and company are stored correctly
  - Uses a pytest fixture with an in-memory database to ensure test isolation

**Features:**

- Uses pytest fixture `db_session` to create a fresh in-memory database for each test
- Tests database INSERT and SELECT operations

---

### **test_logic.py**

Unit tests for the API client's data extraction logic.

**Key Tests:**

- `test_extract_company_name_correctly()` - Tests successful extraction of company name
  - Arranges test data with proper structure
  - Verifies correct company name is extracted
- `test_extract_company_name_incorrectly()` - Tests error handling with incomplete data
  - Verifies that a `KeyError` is raised when company data is missing
  - Uses `pytest.raises()` for exception testing

**Features:**

- Demonstrates the Arrange-Act-Assert (AAA) test pattern
- Tests both success and failure scenarios

---

### **test_validator_posts.py**

Unit tests for post title validation and integration testing.

**Key Tests:**

- `test_title_validation_success()` - Tests that valid titles pass validation
  - A title with 10+ characters should return `True`
- `test_title_validation_failed()` - Tests that short titles raise an error
  - A title with 3 characters should raise `ValueError`
- `test_add_post_integration(db_create)` - Integration test combining validation and database operations
  - Validates the title first
  - Inserts the post into a test database
  - Verifies the post was stored correctly

**Features:**

- Uses pytest fixture `db_create` for in-memory database
- Combines validation and database operations in a single integration test

---

## Requirements

The project dependencies are specified in `requirements.txt`:

- **beautifulsoup4** (v4.14.3) - For HTML parsing in web scraping
- **requests** - For making HTTP requests to APIs and websites
- **pytest** - For unit and integration testing

---

## Usage

### Running the Main Application

```bash
python api_client.py
```

This will:

1. Initialize the database
2. Fetch and store users from JSONPlaceholder API
3. Fetch and store posts from JSONPlaceholder API

### Running the Web Scraper

```bash
python scraper.py
```

This will:

1. Scrape job offers from the fake jobs website
2. Create a `job_offers.csv` file with the results

### Running the Tests

```bash
pytest
```

This will run all tests in the `test_*.py` files and display the results.

### Querying the Database

```bash
python db_example.py
```

This will execute the `get_users_with_posts()` function and display users with their associated posts.

---

## Learning Concepts Demonstrated

- **API Integration**: Making HTTP requests and handling JSON responses
- **Web Scraping**: Parsing HTML with BeautifulSoup and extracting data
- **Database Operations**: SQLite CRUD operations, foreign keys, and JOIN queries
- **Error Handling**: Try-except blocks for connection and HTTP errors
- **Data Validation**: Input validation before database insertion
- **Unit Testing**: Using pytest with fixtures and parametrized tests
- **Integration Testing**: Testing multiple components together
- **CSV Export**: Writing data to CSV files
