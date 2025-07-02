from tabulate import tabulate
class QueryType:
    SELECT = "SELECT"
    INSERT = "INSERT"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    
class QueryCursor:
    def __init__(self, query, conn, values=None):
        self.query = query
        self.values = values
        self.conn = conn
        self.cursor = self.conn.cursor()
        
    def get_curs(self):
        return self.cursor

    def execute(self):
        if self.values is not None:
            self.cursor.execute(self.query, tuple(self.values))
        else:
           self.cursor.execute(self.query)


def exec_cursor(query, cur, val=None):
    if (cur is None):
        raise ValueError("Cursor is None. Please provide a valid cursor.")
    
    if val is not None:
        cur.execute(query, tuple(val))
    else:
        cur.execute(query)


def show_table(data, headers):
    print(tabulate(data, headers=headers, tablefmt='grid'))


def query_select(table, conn):
    # SELECT * FROM
    select_query = f"{QueryType.SELECT} * FROM"

    qr = QueryCursor(select_query + f" {table}", conn)
    qr.execute()
    cur = qr.get_curs()
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    show_table(rows, columns)


def query_insert(table, cols, values, conn):
    insert_query = f"{QueryType.INSERT} INTO"
    
    if cols:
        if isinstance(cols, str):
            cols = cols.split(',')
        cols = ', '.join([col.strip() for col in cols])
    
    # Generate the correct number of placeholders for the values
    if not cols:
        raise ValueError("Column names must be provided for insert operation.")
    
    if isinstance(values, (list, tuple)):
        placeholders = ', '.join(['%s'] * len(values))
        str_tup = tuple(values)
    else:
        placeholders = '%s'
        str_tup = (values,)
    
    insert_query = f"{insert_query} {table} ({cols}) VALUES ({placeholders})"
    
    qr = QueryCursor(insert_query, conn, str_tup)
    qr.execute()
    cur = qr.get_curs()
    conn.commit()

    print(f"Inserted {cur.rowcount} row(s) into {table}.")