# Profiles REST API

A REST API built with FastAPI to manage and retrieve profile records from a SQLite database.

## 📋 Project Overview

This project creates a REST API that:
- Stores 111 profile records in a SQLite database
- Provides endpoints to fetch profile data
- Returns data in JSON format with status and record count

## 🛠️ Technology Stack

- **Language**: Python 3.8+
- **Framework**: FastAPI
- **Database**: SQLite3
- **Libraries**: 
  - pandas (for Excel data processing)
  - uvicorn (ASGI server)
  - openpyxl (Excel file handling)

## 📁 Project Structure

```
├── app.py                  # Main FastAPI application
├── database.py             # Database setup and data insertion script
├── profiles.db             # SQLite database file (generated)
├── Sample_Input.xlsx       # Sample data file with 100 records
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/profiles-api.git
cd profiles-api
```


### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Database

Run the database setup script to create the database and insert records:

```bash
python database.py
```

This will:
- Create `profiles.db` SQLite database
- Create the `profiles` table
- Insert 111 records from `Sample_Input.xlsx`

### 4. Run the API

```bash
python app.py
```


The API will be available at: `http://localhost:8000`

## 📡 API Endpoints

### Get All Profiles

**Endpoint**: `GET /profiles`

**Response**:
```json
{
  "status": "success",
  "record_count": 100,
  "data": [
    {
      "id": "SYB1",
      "name": "John Doe",
      "email": "john.doe@example.com",
      "phone": "1234567890",
      "designation": "Manager",
      "department": "IT"
    }
  ]
}
```

## 🧪 Testing the API


### Using Browser

Simply open: `http://localhost:8000/profiles`



## 📊 Technical Details

### How the Data is Stored

1. **Database**: SQLite3 database (`profiles.db`)
2. **Table Schema**:
   ```sql
   CREATE TABLE profiles (
       id TEXT PRIMARY KEY,
       name TEXT NOT NULL,
       email TEXT UNIQUE NOT NULL,
       phone TEXT,
       designation TEXT,
       department TEXT
   )
   ```
3. **Data Source**: Records are imported from `Sample_Input.xlsx` using pandas
4. **Data Insertion**: Uses `INSERT OR IGNORE` to prevent duplicate entries based on email uniqueness

### How the API Fetches Data

1. **Connection**: The API establishes a connection to `profiles.db` for each request
2. **Query Execution**: SQL queries are executed using `sqlite3` cursor
3. **Row Factory**: `sqlite3.Row` is used to return results as dictionary-like objects
4. **Connection Management**: Database connections are properly opened and closed after each operation

### How JSON Response is Generated

1. **Data Retrieval**: SQL query results are fetched using `cursor.fetchall()` or `cursor.fetchone()`
2. **Conversion**: SQLite Row objects are converted to Python dictionaries using `dict(row)`
3. **Response Structure**: Data is wrapped in a structured response with:
   - `status`: Operation status ("success" or error)
   - `record_count`: Total number of records (for GET all)
   - `data`: The actual profile data as a list of dictionaries or single dictionary
4. **JSON Serialization**: FastAPI automatically serializes Python dictionaries to JSON format
5. **Error Handling**: Exceptions are caught and returned as HTTPException with appropriate status codes

## 🗄️ Database Schema

```sql
CREATE TABLE IF NOT EXISTS profiles (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    designation TEXT,
    department TEXT
)
```

## 📦 Dependencies

See `requirements.txt`:
```
fastapi==0.109.0
uvicorn==0.27.0
pandas==2.1.4
openpyxl==3.1.2
```

## 🔍 Error Handling

The API includes comprehensive error handling:
- **404 Not Found**: When a profile ID doesn't exist
- **500 Internal Server Error**: For database or server errors
- Custom error messages for debugging

## 📝 API Response Examples

### Success Response - Get All Profiles
```json
{
  "status": "success",
  "record_count": 100,
  "data": [
    {
      "id": "SYB1",
      "name": "John Doe",
      "email": "john.doe@example.com",
      "phone": "1234567890",
      "designation": "Manager",
      "department": "IT"
    },
    {
      "id": "SYB2",
      "name": "Jane Smith",
      "email": "jane.smith@example.com",
      "phone": "9876543210",
      "designation": "Developer",
      "department": "Engineering"
    }
  ]
}
```