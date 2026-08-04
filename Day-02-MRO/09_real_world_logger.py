class FileLogger:
    def log(self):
        print("File logged")
        super().log()

class DatabaseLogger:
    def log(self):
        print("Database logged")
        super().log()

class CloudLogger:
    def log(self):
        print("Cloud logged")

class ApplicationLogger(FileLogger, DatabaseLogger, CloudLogger):
    def log(self):
        print("Logged successfully")
        super().log()


login = ApplicationLogger()
login.log()
print(ApplicationLogger.mro())