import mysql.connector as connector
connection = connector.connect(user="root", password="password_removed")
cursor = connection.cursor()

db_query = """CREATE DATABASE IF NOT EXISTS little_lemon15"""
cursor.execute(db_query)
cursor.execute("""USE little_lemon15""")

create_bookings = """CREATE TABLE bookings(GuestFirstName VARCHAR(200), GuestLastName VARCHAR(200), TableNo INT, BookingSlot TIME, EmployeeID INT, BookingID INT, PRIMARY KEY(EmployeeID))"""
cursor.execute(create_bookings)

insert1 = """INSERT INTO bookings(GuestFirstName, GuestLastName, TableNo, BookingSlot, EmployeeID, BookingID) VALUES('Henry', 'Williams', 1, '17:00', 23, 321)"""
cursor.execute(insert1)
connection.commit()

insert2 = """INSERT INTO bookings VALUES('Sarah', 'Mcmillan', 5, '15:30', 52, 647), ('Ichigo', 'Tatsumi', 3, '12:00', 26, 964), ('Joyita', 'Roy', 10, '13:30', 45, 647)"""
cursor.execute(insert2)
connection.commit()

create_orders_table = """CREATE TABLE orders(BookingID INT NOT NULL, BillAmount FLOAT NOT NULL, City VARCHAR(255) NOT NULL)"""
cursor.execute(create_orders_table)

#insert
insert1 = """INSERT INTO orders VALUES(321, 9626.02, 'Kolkata'), (964, 8435.99, 'Bangalore'), (647, 3678.54, 'Kolkata'), (371, 6549.58, 'Tokyo'), (25, 3456.64, 'Sarnia')"""
cursor.execute(insert1)
connection.commit()

stored_procedure_query = """CREATE PROCEDURE GetCustomerAndBillAmount() BEGIN SELECT bookings.BookingID, CONCAT(bookings.GuestFirstName, ' ', bookings.GuestLastName) AS CustomerName, orders.BillAmount FROM bookings INNER JOIN orders ON bookings.BookingID = orders.BookingID WHERE orders.BillAmount >= 3500 ORDER BY orders.BillAmount DESC; END"""
cursor.execute(stored_procedure_query)
cursor.callproc("""GetCustomerAndBillAmount""")
results = next(cursor.stored_results())
dataset = results.fetchall()
for data in dataset:
    print(*data)