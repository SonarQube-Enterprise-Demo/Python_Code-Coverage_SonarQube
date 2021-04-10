import mysql.connector


#
#
# my_db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="pwdpwd",
#     database="todo"
# )
#
# my_cursor = my_db.cursor()
#
# my_cursor.execute("CREATE DATABASE todo")
#
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="pwdpwd",
#     database="todo",
# )
#
#
# class Schema:
#     def __init__(self):
#         self.conn = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="pwdpwd",
#             database="todo",
#         )
#         # my_cursor = self.conn.cursor()
#         self.create_user_table()
#         self.create_to_do_table()
#
#     def create_to_do_table(self):
#         query = """
#         CREATE TABLE IF NOT EXISTS "Todo" (
#             id INTEGER PRIMARY KEY,
#           Title TEXT,
#           Description TEXT,
#           _is_done boolean,
#           _is_deleted boolean,
#           CreatedOn Date DEFAULT CURRENT_DATE,
#           DueDate Date,
#           UserId INTEGER FOREIGNKEY REFERENCES User(_id)
#         );
#         """
#        self.conn.execute_command(query)

class Schema:
    def __init__(self):
        self.conn = mysql.connector.Connect(
            host="localhost",
            user="root",
            passwd="pwdpwd",
            database="todo",
        )
        self.create_user_table()
        self.create_to_do_table()

    def create_user_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS user (
                id int NOT NULL AUTO_INCREMENT,
                name varchar(45) NOT NULL,
                email varchar(45) NOT NULL,
                PRIMARY KEY (id)
            );
            """
        my_cursor = self.conn.cursor()
        my_cursor.execute(query)

    def create_to_do_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS todo (
          id int NOT NULL,  
          title varchar(45) NOT NULL,  
          description varchar(45) NOT NULL,  
          _is_done boolean,
          _is_deleted boolean,
          createdOn Date,
          duedate date,
          UserId int,
          PRIMARY KEY (id),
          FOREIGN KEY (id) REFERENCES user(ID)
        ); 
        """
        my_cursor = self.conn.cursor()
        my_cursor.execute(query)


class ToDoModel:
    TABLENAME = "TODO"

    def __init__(self):
        self.conn = mysql.connector.connect('todo.db')

    def create(self, text, description, tablename=TABLENAME):
        query = f'insert into {tablename} ' \
                f'(Title, Description) ' \
                f'values ("{text}","{description}")'

        result = self.conn.cursor().execute(query)
        return result
