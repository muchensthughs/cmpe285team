def executeSql(db, sql):
    c=db.cursor()
    c.execute(sql)
    res = c.fetchall()
    c.close()
    return res