#! python3

# Import necessary libraries
import psycopg2


def select_from_time(conn, time):
    query = f"""SELECT time_id FROM weather.time 
WHERE year = '{time[:4]}' 
AND month = '{time[5:7]}' 
AND day = '{time[8:10]}' 
AND hour = '{time[11:13]}' 
AND minute = '{time[14:16]}' 
AND second = '{time[17:20]}';"""
    value_id = ""

    try:
        exist = True
        while exist == True:
            cur = conn.cursor()
            cur.execute(query)

            row = cur.fetchone()

            if row == None:
                try:
                    insert_query = f"INSERT INTO weather.time (time_id, year, month, day, hour, minute, second) VALUES ('{time}', {time[:4]}, {time[5:7]}, {time[8:10]}, {time[11:13]}, {time[14:16]}, {time[17:20]});"
                    cur = conn.cursor()
                    cur.execute(insert_query)

                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)

            else:
                value_id = row[0]
                exist = False

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:

        cur.close()

        if value_id == "":
            value_id = None
        return value_id
