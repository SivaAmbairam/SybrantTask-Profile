from fastapi import FastAPI, HTTPException
import sqlite3
import uvicorn

app = FastAPI(title="Profiles API", version="1.0.0")

def get_db_connection():
    '''Database connection'''
    conn = sqlite3.connect("profiles.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/")
def root():
    '''Root endpoint'''
    return {
        "message": "check below profile api",
        "endpoints": {
            "GET /profiles": "Fetch all profile records",
        }
    }

@app.get("/profiles")
def get_profiles():
    '''
    collect all the details from the database
    Return: JSON response with status, record count, and data
    '''
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM profiles")
        rows = cursor.fetchall()
        profiles = [dict(row) for row in rows]
        
        conn.close()
        
        '''RETURN JSON RESPONSE'''
        return {
            "status": "200",
            "record_count": len(profiles),
            "data": profiles
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)