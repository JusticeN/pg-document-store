
def sql_create_table(table_name):
    return "CREATE TABLE {} (id serial PRIMARY KEY, data json);".format(table_name)

def sql_insert_in_table(table_name, values):
    return "INSERT INTO {} (data) VALUES ({});".format(table_name, values)

def sql_delete_table(table_name, where):
    return "DELETE {} WHERE {};".format(table_name, where)

def sql_read_table(table_name, where):
    return "SELECT id, data FROM {} WHERE {};".format(table_name, where)