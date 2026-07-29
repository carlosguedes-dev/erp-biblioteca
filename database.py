import sqlite3
from datetime import datetime

DB_NAME = "erp_biblioteca.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Tabela de Livros
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        category TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'Disponível',
        added_date TEXT NOT NULL
    )
    ''')
    
    # Tabela de Clientes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        cpf TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        registered_date TEXT NOT NULL
    )
    ''')
    
    # Tabela de Empréstimos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS loans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER NOT NULL,
        client_id INTEGER NOT NULL,
        loan_date TEXT NOT NULL,
        return_date TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'Ativo',
        FOREIGN KEY (book_id) REFERENCES books (id),
        FOREIGN KEY (client_id) REFERENCES clients (id)
    )
    ''')
    
    conn.commit()
    conn.close()

# --- Funções CRUD Livros ---
def add_book(title, author, category):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    added_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO books (title, author, category, added_date) VALUES (?, ?, ?, ?)", 
                   (title, author, category, added_date))
    conn.commit()
    conn.close()

def get_all_books():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books ORDER BY id DESC")
    books = cursor.fetchall()
    conn.close()
    return books

def update_book_status(book_id, status):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET status = ? WHERE id = ?", (status, book_id))
    conn.commit()
    conn.close()

# --- Funções CRUD Clientes ---
def add_client(name, cpf, email, phone):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    registered_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO clients (name, cpf, email, phone, registered_date) VALUES (?, ?, ?, ?, ?)",
                   (name, cpf, email, phone, registered_date))
    conn.commit()
    conn.close()

def get_all_clients():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients ORDER BY id DESC")
    clients = cursor.fetchall()
    conn.close()
    return clients

# --- Funções CRUD Empréstimos ---
def add_loan(book_id, client_id, return_date):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    loan_date = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO loans (book_id, client_id, loan_date, return_date) VALUES (?, ?, ?, ?)",
                   (book_id, client_id, loan_date, return_date))
    conn.commit()
    conn.close()
    update_book_status(book_id, 'Emprestado')

def get_active_loans():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    query = '''
        SELECT loans.id, books.title, clients.name, loans.loan_date, loans.return_date, loans.status, books.id
        FROM loans
        JOIN books ON loans.book_id = books.id
        JOIN clients ON loans.client_id = clients.id
        WHERE loans.status = 'Ativo'
        ORDER BY loans.id DESC
    '''
    cursor.execute(query)
    loans = cursor.fetchall()
    conn.close()
    return loans

def return_loan(loan_id, book_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE loans SET status = 'Devolvido' WHERE id = ?", (loan_id,))
    conn.commit()
    conn.close()
    update_book_status(book_id, 'Disponível')

def get_dashboard_metrics():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM books")
    total_books = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM clients")
    total_clients = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM loans WHERE status='Ativo'")
    active_loans = cursor.fetchone()[0]
    
    conn.close()
    return total_books, total_clients, active_loans
