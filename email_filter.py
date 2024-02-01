import csv
import re

class EmailManager:
    def __init__(self, filename):
        self.filename = filename
        self.emails = set()

    def load_emails(self):
        try:
            with open(self.filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    self.emails.add(row[0])
            print("Emails loaded successfully.")
        except FileNotFoundError:
            print("CSV file not found.")
        except Exception as e:
            print(f"Error loading emails: {str(e)}")

    def save_emails(self):
        try:
            with open(self.filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for email in self.emails:
                    writer.writerow([email])
            print(f"Emails saved to {self.filename}")
        except Exception as e:
            print(f"Error saving emails: {str(e)}")

    def filter_email(self, emails):
        email_pattern = re.compile(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$')
        filtered_emails = []
        for email in emails:
            if isinstance(email, list):
                filtered_emails.extend(self.filter_email(email))
            elif re.match(email_pattern, email):
                filtered_emails.append(email)
            else:
                print(f"Invalid email format: {email}")
        return filtered_emails

    def update_email_list(self, new_emails):
        filtered_emails = self.filter_email(new_emails)
        self.emails.update(filtered_emails)
        self.save_emails()

    def __enter__(self):
        self.load_emails()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.save_emails()

def main():
    csv_filename = 'email_list.csv'

    with EmailManager(csv_filename) as email_manager:
        emails = ["joshjwenner@gmail.com", ["test@test.com", "hello@python.com"], "working123@yahoo.com"]
        email_manager.update_email_list(emails)

if __name__ in "__main__":
    main()