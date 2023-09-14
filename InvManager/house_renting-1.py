import datetime
users = []
house_details = []
payment_details = []
bookings_list = []


class house_rent_App:
    booking_count = 0

    def __init__(self, id: int, Name: str, Email: str, Password: str, Role: str ,Phn_no: int, Aadhar_no: int):
        self.userID = id
        self.name = Name
        self.email = Email
        self.password = Password
        self.role = Role
        self.phn_no = Phn_no
        self.aadhar_no = Aadhar_no

    def hardCodedData(self):
        users.append(self)
        return users

    def validateLogin(self, email, password):
        for user in users:
            if user.email == email and user.password == password:
                return user
        return None

    def Welcome(self):
        print('Hi Welcome', self.name)

class HouseList:
    def __init__(self, id, house_type, sqr_feet, rent_price):
        self.HouseId = id
        self.HouseType = house_type
        self.sqr_feet = sqr_feet
        self.Rent_Price = rent_price


class Payment:
    def __init__(self, paymentId, payment_method, card_no, month, year, cvv, amount, payment_status = 'not_paid'):
        self.paymentId = paymentId
        self.payment_method = payment_method
        self.card_no = card_no
        self.cvv = cvv
        self.month = month
        self.year = year
        self.amount = amount
        self.payment_status = payment_status

    def hardCodedData(self):
        payment_details.append(self)

class Bookings:
    def __init__(self, BookingID, userId, BookedOn, houseDetails):
        self.booking_id = BookingID
        self.userId = userId
        self.booked_on = BookedOn
        self.houseDetails = houseDetails


class houseListings(house_rent_App):
    def __init__(self, id, Name, Email, Password, Role, Phn_no, Aadhar_no):
        super().__init__(id, Name, Email, Password, Role, Phn_no, Aadhar_no)
        self.BookHouse_details = []


    def booking_for_customer(self):
        #stayInCustomerMenu = True
        house1 = HouseList(1, '1BK',1200,2000)
        house2 = HouseList(2, '2BHK',1500,5000)
        house3 = HouseList(3, '3BHK',1800,10000)
        house_details.append(house1)
        house_details.append(house2)
        house_details.append(house3)
        while True:
            print("\n******************************")
            print("Customer Menu")
            print("1. List Of Houses")
            print("2. Select The Houses")
            print("3. Booked History")
            print("4. Logout")
            choice = int(input("Enter your Choice: "))


            if choice == 1:


                for house in house_details:
                    print("House No:", house.HouseId)
                    print("House Type:", house.HouseType)
                    print("House sqr_feet:", house.sqr_feet)
                    print("House Rent:", house.Rent_Price)
                    print('---------------------------------------------')

            elif choice == 2:
                while True:
                    print("House List:")
                    for house in house_details:
                        print(house.HouseId, house.HouseType, house.sqr_feet, house.Rent_Price)

                    house_id = int(input("Enter the ID of the house to add to book (or 0 to stop adding): "))
                    if house_id == 0:
                        break
                    selected_item = None
                    for house in house_details:
                        if house.HouseId == house_id:
                            selected_item = house
                            break

                    if selected_item is None:
                        print("Invalid movie ID. Please try again.")
                    else:

                        cart_item = {
                            'HouseId': selected_item.HouseId,
                            'HouseType': selected_item.HouseType,
                            'sqr_feet': selected_item.sqr_feet,
                            'Rent_Price': selected_item.Rent_Price
                        }
                        self.BookHouse_details.append(cart_item)
                        print("Item added to booking successfully.")
                    view_cart = input("Do you want to see the booking? (y/n): ")
                    if view_cart.lower() == "y":

                        print("Your Booking:")
                        for item in self.BookHouse_details:
                                print("House ID:", item['HouseId'])
                                print("House Type:", item['HouseType'])
                                print("Sqr_feet:", item['sqr_feet'])
                                print("Rent_Price:", item['Rent_Price'])
                                print('---------------------------------------------')

                        print("Payment Options:")
                        print("1. Card")
                        print("2. UPI")

                        payment_choice = int(input("Choose a payment option: "))

                        if payment_choice == 1:
                            print("Payment successful. Thank you for using card.")
                        elif payment_choice == 2:
                            print("Payment successful. Thank you for using UPI.")
                        else:
                            print("Invalid payment option.")
                        booking_data = Bookings(self.booking_count, self.userID, datetime.datetime.now(), self.BookHouse_details)


                        bookings_list.append(booking_data)
                        self.booking_count += 1
                        break

            elif choice == 3:
                self.booking_id = 1
                for booking in bookings_list:
                    print(f"Booking ID: {booking.booking_id}")
                    print(f"User ID: {booking.userId}")
                    #print(f"Booked On: {booking.booked_on}")
                    for item in self.BookHouse_details:
                        print(f"Booked On: {booking.booked_on}")
                        print("Details:", item)
                    print('---------------------------------------------')

                    self.booking_id += 1


            elif choice == 4:
                print("Logout Successfully")
                break
            else:
                print("Invalid Entry")



class AdminFlow(house_rent_App):
    def __init__(self, id, Name, Email, Password, Role):
        super().__init__(id, Name, Email, Password, Role)

    def Welcome(self):
        print('Hi Welcome Admin')
        print(self.name)


if __name__ == "__main__":
    app = house_rent_App(1, "Sanjay", "sanjay@gmail.com", "sanjay123", "Renter",99999999 ,123245657654)
    app.hardCodedData()
    app = house_rent_App(2, "Rahul", "ragul@gmail.com", "rahul123", "Admin",2654371578 ,875782682682)
    app.hardCodedData()
    app = house_rent_App(3, "Arjunan", "arjunan@gmail.com", "arjunan123", "Owner",8767654253 ,765544325725)
    app.hardCodedData()

    login_user = app.validateLogin("sanjay@gmail.com", "sanjay123")

    if login_user:
        print('Login Success')
        if login_user.role == "Admin":
            admin = AdminFlow(login_user.userID, login_user.name, login_user.email, login_user.password, login_user.role, login_user.phn_no, login_user.aadhar_no)
            admin.Welcome()
        elif login_user.role == "Renter":
            book = houseListings(login_user.userID, login_user.name, login_user.email, login_user.password, login_user.role, login_user.phn_no, login_user.aadhar_no)
            book.Welcome()
            book.booking_for_customer()

