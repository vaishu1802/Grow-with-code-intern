import random
import string

# Generate OTP
def generate_otp(length):
    characters = string.ascii_letters + string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

# Send OTP via Email
def send_otp_email(email, otp):
    # Logic to send email with OTP
    print(f"OTP sent to {email}: {otp}")

# Send OTP via SMS
def send_otp_sms(phone_number, otp):
    # Logic to send SMS with OTP
    print(f"OTP sent to {phone_number}: {otp}")

# Verify OTP
def verify_otp(user_otp, otp):
    return user_otp == otp

# Example usage
def main():
    # Generate OTP
    otp = generate_otp(6)

    # Simulate sending OTP via Email
    email = "aswanth0211@gmail.com"
    send_otp_email(email, otp)

    # Simulate sending OTP via SMS
    phone_number = "+91 9360773390"
    send_otp_sms(phone_number, otp)

    # Prompt user to enter OTP
    user_otp = input("Enter the OTP: ")

    # Verify OTP
    if verify_otp(user_otp, otp):
        print("OTP verification successful")
    else:
        print("Invalid OTP")

if __name__ == "__main__":
    main()