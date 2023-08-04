# import sqlite3
# connection = sqlite3.connect("pokemon.db")
# cursor = connection.cursor()

# class Pokemon:
#     all = []

#     def __init__(self, name, type, size, owned, id=None):
#         self.id = id
#         self.name = name
#         self.type = type
#         self.size = size
#         self.owned = owned
#         Pokemon.all.append(self)
#     #create the table if it does not exists
#     @classmethod
#     def create_table(cls):
#         sql = """
#             CREATE TABLE IF NOT EXISTS pokemon
#             (
#             id INTEGER PRIMARY KEY,
#             name TEXT,
#             type TEXT,
#             size INTEGER,
#             owned INTEGER
#             )
#             """
        
#         cursor.execute(sql)
#         connection.commit()

#     def pushtobackend(self):
#         value = f'''
#                 INSERT INTO pokemon (name, type, size, owned)
#                 VALUES ("{self.name}", "{self.type}", "{self.size}", "{self.owned}")
#                 '''
#         cursor.execute(value)
#         connection.commit()
#         input = self.fetchall()
#         self.id = input[-1][0]

    
#     def edit(self, var, new_input):
#         if type(new_input) is str:
#             value = f'''
#                 UPDATE pokemon
#                 SET {var} = {new_input}
#                 WHERE id = {self.id}
#                 '''
#         else:
#             value = f'''
#                 UPDATE pokemon
#                 SET {var} = {int(new_input)}
#                 WHERE id = {self.id}
#             '''
#         cursor.execute(value)
#         connection.commit()

#     def delete(self):
#         value = f'''
#             DELETE FROM pokemon
#             WHERE id = {self.id}
#             '''
#         cursor.execute(value)
#         connection.commit()

#     @classmethod
#     def fetchone(cls, id):
#         value = f'''
#                 SELECT * FROM pokemon
#                 WHERE id = {id}
#                 '''
        
#         x = cursor.execute(value).fetchone()
#         return x
    
#     @classmethod
#     def fetchall(cls):

#         value = f'''
#             SELECT * FROM pokemon
#             '''
#         x = cursor.execute(value).fetchall()
#         return x

# picahu = Pokemon("Pikachu", "Electric", 2, 0)
# second = Pokemon("Squirel", "Tree", 2, 0)
# third = Pokemon("Kirby", "Elastic", 3, 1 )

# # Pokemon.create_table()
# # picahu.pushtobackend()
# # second.pushtobackend()
# # third.pushtobackend()
# print(f"{second.id}, {third.id}, {picahu.id}")
# third.delete()


