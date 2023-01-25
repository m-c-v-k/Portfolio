#! python3

# Import necessary libraries
import psycopg2


def select_from_approved_time(conn, a_time, r_time):
    query = f"SELECT approved_time_id FROM weather.approved_time WHERE reference_time = '{r_time}';"
    value_id = ""

    try:
        exist = True
        while exist == True:
            cur = conn.cursor()
            cur.execute(query)

            row = cur.fetchone()

            if row == None:
                try:
                    insert_query = f"INSERT INTO weather.time (time_id, year, month, day, hour, minute, second) VALUES ('{r_time}', {r_time[:4]}, {r_time[5:7]}, {r_time[8:10]}, {r_time[11:13]}, {r_time[14:16]}, {r_time[17:20]});"
                    cur = conn.cursor()
                    cur.execute(insert_query)
                    conn.commit()

                    insert_query = f"INSERT INTO weather.approved_time (approved_time_id, reference_time) VALUES ('{a_time}', '{r_time}');"

                    cur.execute(insert_query)
                    conn.commit()

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
