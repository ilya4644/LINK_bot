import sqlite3


class DataBase:
    def __init__(self):
        self.name = {0: "userid", 1: "fullname", 2: "sex", 3: "age", 4: "institute", 5: "course", 6: "interests", 7: "photo", 8: "want", 9: "shown", 10: "username", 11: "likeid", 12: "look", 13: "admin", 14: "likesimp", 15: "form", 16: "napr"}
        self.conn = sqlite3.connect('test.db')
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
        userid INT PRIMARY KEY,
        fullname TEXT,
        sex INT,
        age INT,
        institute INT,
        course INT,
        interests TEXT,
        photo TEXT,
        want INT,
        shown TEXT,
        username TEXT,
        likeid TEXT,
        look INT,
        admin INT,
        likesimp TEXT,
        form TEXT,
        napr TEXT);""")
        self.conn.commit()

    def addUser(self, user):
        self.cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", user)
        self.conn.commit()

    def updateShown(self, user, id_username):
        self.cur.execute(f"SELECT shown FROM users WHERE userid = {user[0]};")
        ids = str(self.cur.fetchone()[0])
        ids += " " + str(id_username)
        changer = [ids, user[0]]
        self.cur.execute("UPDATE users SET shown = ? WHERE userid = ?;", changer)
        self.conn.commit()

    def delete_shown(self, id_username):
        self.cur.execute("SELECT * FROM users")
        users = self.cur.fetchall()
        if len(users) != 0:
            for i in range(len(users)):
                count = f'{users[i][9]}'
                if f'{id_username}' in count:
                    res = count.replace(f'{id_username}', '')
                    self.update('shown', res, users[i][0])
        self.conn.commit()

    def update_likeid(self, id_prof, user):
        self.cur.execute(f"UPDATE users SET likeid = '{id_prof}' WHERE userid = {user};")
        self.conn.commit()

    def update(self, insdex, val, user):
        self.cur.execute(f"UPDATE users SET {insdex} = '{val}' WHERE userid = {user};")
        self.conn.commit()

    def not_watch(self):
        self.cur.execute("SELECT * FROM users")
        users = self.cur.fetchall()
        count = ''
        if len(users) != 0:
            for i in range(len(users)):
                count += f'{users[i][0]} '
            return count

    def show(self, user, users, want, sex):
        for i in range(len(users)):
            if users[i][0] != user[0]:
                if user[8] == 3:
                    if users[i][8] == 1 and user[2] == 1 and str(users[i][0]) not in str(user[9]):
                        self.updateShown(user, users[i][0])
                        return users[i]
                    elif users[i][8] == 2 and user[2] == 0 and str(users[i][0]) not in str(user[9]):
                        self.updateShown(user, users[i][0])
                        return users[i]
                    elif users[i][8] == 3 and str(users[i][0]) not in str(user[9]):
                        self.updateShown(user, users[i][0])
                        return users[i]
                elif user[8] < 3:
                    if (users[i][8] == want or users[i][8] == 3) and users[i][2] == sex and str(users[i][0]) not in str(user[9]):
                        self.updateShown(user, users[i][0])
                        return users[i]
                else:
                    if users[i][8] == want and user[i][2] == sex and str(users[i][0]) not in str(user[9]):
                        self.updateShown(user, users[i][0])
                        return users[i]
                if i == len(users) - 1:
                    return False

    def showPeople(self, user):
        self.cur.execute("SELECT * FROM users")
        users = self.cur.fetchall()
        if user[8] == 1:
            if user[2] == 1:
                return self.show(user, users, 1, 1)
            else:
                return self.show(user, users, 2, 1)
        elif user[8] == 2:
            if user[2] == 1:
                return self.show(user, users, 1, 0)
            else:
                return self.show(user, users, 2, 0)
        elif user[8] == 3:
            return self.show(user, users, 1, 1)
        elif user[8] == 4:
            return self.show(user, users, 5, 0)
        elif user[8] == 5:
            return self.show(user, users, 4, 1)

    def userExist(self, user_id):
        self.cur.execute(f"SELECT COUNT(*) FROM users WHERE userid = {user_id}")
        count = self.cur.fetchone()[0]
        if count != 0:
            return True
        else:
            return False

    def getUser(self, user_id):
        self.cur.execute("SELECT * FROM users")
        users = self.cur.fetchall()
        if len(users) != 0:
            for i in range(len(users)):
                if users[i][0] == user_id:
                    return users[i]

    def check_admin(self):
        self.cur.execute("SELECT * FROM users")
        users = self.cur.fetchall()
        count_admin = []
        if len(users) != 0:
            for i in range(len(users)):
                if users[i][13] == 1:
                    count_admin.append(users[i][0])
        return count_admin

    def get_stat_users(self):
        self.cur.execute("SELECT * FROM users")
        users = self.cur.fetchall()
        count = {"id": '', "username": '', 'want': ''}
        if len(users) != 0:
            for i in range(len(users)):
                count['id'] += f' {users[i][0]}'
                count['username'] += f' {users[i][10]}'
                count['want'] += f' {users[i][8]}'
        return count

    def sender(self):
        self.cur.execute("SELECT * FROM users")
        users = self.cur.fetchall()
        count = {"id_man": '', "id_gl": '', 'all_id': ''}
        if len(users) != 0:
            for i in range(len(users)):
                count['all_id'] += f' {users[i][0]}'
                if users[i][2] == 1:
                    count['id_man'] += f' {users[i][0]}'
                elif users[i][2] == 0:
                    count['id_gl'] += f' {users[i][0]}'
        print(count)
        return count
