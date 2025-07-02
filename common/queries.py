from tabulate import tabulate

def exec_cursor(query, cur, val=None):
    if (cur is None):
        raise ValueError("Cursor is None. Please provide a valid cursor.")
    
    if val is not None:
        cur.execute(query, tuple(val))
    else:
        cur.execute(query)


def show_table(data, headers):
    print(tabulate(data, headers=headers, tablefmt='grid'))


def query_select(query, table, conn):
    select_query = query
    
    cur = conn.cursor()
    exec_cursor(f"{select_query} {table}", cur)
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    show_table(rows, columns)


def query_insert(query, table, cols, values, conn):
    if cols:
        if isinstance(cols, str):
            cols = cols.split(',')
        cols = ', '.join([col.strip() for col in cols])
    
    # Generate the correct number of placeholders for the values
    if isinstance(values, (list, tuple)):
        placeholders = ', '.join(['%s'] * len(values))
    else:
        placeholders = '%s'
    
    insert_query = f"{query} {table} ({cols}) VALUES ({placeholders})"
    
    print(insert_query)

    cur = conn.cursor()
    exec_cursor(insert_query, cur, val=values)
    conn.commit()

    print(f"Inserted {cur.rowcount} row(s) into {table}.")