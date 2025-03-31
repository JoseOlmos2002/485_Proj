import mysql.connector
import random
import string
from datetime import datetime, timedelta

# Establish database connection
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="Sike",
            user="root",
            password= "Nothereeither",
            database="flight_reservation"
        )

        if connection.is_connected():
            print("✅ Connected to the database")
            return connection
        
    except mysql.connector.Error as e:
        print(f"❌ Database connection failed: {e}")
        return None


def save_user(email, username, password):
    connection = connect_to_db()
    
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO USER (USERNAME, EMAIL, PASSWORD) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, email, password))
            connection.commit()  # Save the changes
            cursor.close()       # Close the cursor
            connection.close()   # Close the connection
            print("Saved user into database")
            return "✅ User saved successfully"
        
        except Exception as e:
            return f"❌ Error saving user: {e}"
    else:
        return "❌ Database connection failed"
    


def logging_in(username, password):
    connection = connect_to_db()

    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM USER WHERE USERNAME = %s AND PASSWORD = %s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()  # Fetch a single matching record
            
            return user is not None  # Returns True if user exists, else False
        
        except Exception as e:
            print(f"Error during login: {e}")
            return False
        
        finally:
            cursor.close()
            connection.close()
    return False


def generate_confirmation_number(size=10):
    characters = string.ascii_uppercase + string.digits  # Uppercase letters and digits
    return ''.join(random.choices(characters, k=size))


def add_reservation(current_location, destination, name, seat_preference, meal_preference, beverage_preference, confirmation_number):
    # Get current date for reservation
    reservation_date = datetime.now().date()

    # Calculate flight date (7 days after reservation date)
    flight_date = reservation_date + timedelta(days=7)

    # Connect to the database
    connection = connect_to_db()

    if connection:
        try:
            cursor = connection.cursor()

            # SQL query to insert reservation into the database
            query = """
                INSERT INTO FLIGHT (
                    CONFIRMATION_NUMBER, 
                    CURRENT_LOCATION, 
                    DESTINATION, 
                    RESERVATION_DATE, 
                    FLIGHT_DATE, 
                    NAME,
                    SEAT_PREFERENCE, 
                    MEAL_PREFERENCE, 
                    BEVERAGE_CHOICE
                ) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            # Execute the query and commit the transaction
            cursor.execute(query, (confirmation_number, current_location, destination, reservation_date, flight_date, name, seat_preference, meal_preference, beverage_preference))
            connection.commit()

            print("Reservation added successfully!")
            return True

        except Exception as e:
            print(f"Error during reservation: {e}")
            return False

        finally:
            cursor.close()
            connection.close()

    return False

def get_flight_info(confirmation_number):
    connection = connect_to_db()  # Ensure you have a working DB connection function

    if connection:
        try:
            cursor = connection.cursor(dictionary=True)  # Use dictionary=True for a dictionary output
            query = "SELECT * FROM FLIGHT WHERE CONFIRMATION_NUMBER = %s"
            cursor.execute(query, (confirmation_number,))
            flight_info = cursor.fetchone()  # Fetch the flight record

            return flight_info  # Returns flight details if found, else None

        except Exception as e:
            print(f"Error fetching flight info: {e}")
            return None

        finally:
            cursor.close()
            connection.close()
    return None
