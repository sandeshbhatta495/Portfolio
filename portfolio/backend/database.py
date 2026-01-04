import sqlite3
import os
from datetime import datetime

class Database:
    def __init__(self, db_path=None):
        if db_path is None:
            db_path = os.path.join(os.path.dirname(__file__), 'portfolio.db')
        self.db_path = db_path
        self.init_database()
    
    def get_connection(self):
        """Create a database connection"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_database(self):
        """Initialize database tables"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Create contacts table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                subject TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create resume downloads table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS resume_downloads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                downloaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                ip_address TEXT,
                user_agent TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
        print("Database initialized successfully")
    
    def save_contact(self, name, email, subject, message):
        """Save contact form submission"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO contacts (name, email, subject, message)
            VALUES (?, ?, ?, ?)
        ''', (name, email, subject, message))
        
        conn.commit()
        contact_id = cursor.lastrowid
        conn.close()
        
        return contact_id
    
    def track_resume_download(self, ip_address=None, user_agent=None):
        """Track resume download"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO resume_downloads (ip_address, user_agent)
            VALUES (?, ?)
        ''', (ip_address, user_agent))
        
        conn.commit()
        conn.close()
    
    def get_contacts(self, limit=50):
        """Get recent contact submissions"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM contacts
            ORDER BY created_at DESC
            LIMIT ?
        ''', (limit,))
        
        contacts = [dict(row) for row in cursor.fetchall()]
        conn.close()
        
        return contacts
    
    def get_stats(self):
        """Get portfolio statistics"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Total contacts
        cursor.execute('SELECT COUNT(*) as count FROM contacts')
        total_contacts = cursor.fetchone()['count']
        
        # Total resume downloads
        cursor.execute('SELECT COUNT(*) as count FROM resume_downloads')
        total_downloads = cursor.fetchone()['count']
        
        # Recent contacts (last 7 days)
        cursor.execute('''
            SELECT COUNT(*) as count FROM contacts
            WHERE created_at >= datetime('now', '-7 days')
        ''')
        recent_contacts = cursor.fetchone()['count']
        
        conn.close()
        
        return {
            'total_contacts': total_contacts,
            'total_downloads': total_downloads,
            'recent_contacts': recent_contacts
        }
    
    def clear_old_data(self, days=90):
        """Clear old data (optional maintenance)"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            DELETE FROM contacts
            WHERE created_at < datetime('now', '-' || ? || ' days')
        ''', (days,))
        
        cursor.execute('''
            DELETE FROM resume_downloads
            WHERE downloaded_at < datetime('now', '-' || ? || ' days')
        ''', (days,))
        
        conn.commit()
        deleted_count = cursor.rowcount
        conn.close()
        
        return deleted_count


if __name__ == '__main__':
    # Test database
    db = Database()
    print("Database test successful!")
    print(f"Stats: {db.get_stats()}")
