"""#7"""


class MessageSender:
    """Базовий клас для надсилання повідомлень."""

    def send_message(self, message: str):
        """
        Абстрактний метод для надсилання повідомлень.

        Arguments:
            message (str): Текст повідомлення.

        Raises: 
            NotImplementedError: Якщо метод не перевизначено у дочірньому класі.
        """
        raise NotImplementedError("Метод для надсилання сповіщень не перевизначено у дочірньому класі.")


class SMSService:
    """Сервіс надсилання повідомлення через SMS."""

    def send_sms(self, phone_number: str, message: str):
        """
        Відправляє SMS-повідомлення.

        Arguments:
            phone_number (str): Номер телефону отримувача.
            message (str): Текст повідомлення.

        Raises:
            TypeError: Якщо аргументи мають неправильний тип.
        """
        if not isinstance(phone_number, str):
            raise TypeError("'phone_number' must be 'str'")
        if not isinstance(message, str):
            raise TypeError("'message' must be 'str'")

        print(f"Відправка SMS на {phone_number}: {message}")


class EmailService:
    """Сервіс надсилання повідомлення через Email."""

    def send_email(self, email_address: str, message: str):
        """
        Відправляє Email-повідомлення.

        Arguments:
            email_address (str): Email-адреса отримувача.
            message (str): Текст повідомлення.

        Raises:
            TypeError: Якщо аргументи мають неправильний тип.
        """
        if not isinstance(email_address, str):
            raise TypeError("'email_address' must be 'str'")
        if not isinstance(message, str):
            raise TypeError("'message' must be 'str'")

        print(f"Відправка Email на {email_address}: {message}")


class PushService:
    """Сервіс надсилання повідомлення через Push."""

    def send_push(self, device_id: str, message: str):
        """
        Відправляє Push-повідомлення.

        Arguments:
            device_id (str): Ідентифікатор пристрою отримувача.
            message (str): Текст повідомлення.

        Raises:
            TypeError: Якщо аргументи мають неправильний тип.
        """
        if not isinstance(device_id, str):
            raise TypeError("'divce_id' must be 'str'")
        if not isinstance(message, str):
            raise TypeError("'message' must be 'str'")

        print(f"Відправка Push-повідомлення на пристрій {device_id}: {message}")


class SMSAdapter(MessageSender):
    """Адаптер для надсилання повідомлень через SMS."""

    def __init__(self, service: SMSService, phone_number: str):
        """
        Ініціалізує SMS-адаптер.

        Arguments:
            service (SMSService): Об'єкт сервісу SMS.
            phone_number (str): Номер телефону отримувача.
        """
        self.service = service
        self.phone_number = phone_number


    def send_message(self, message: str):
        """
        Надсилає SMS-повідомлення.

        Arguments:
            message (str): Текст повідомлення.

        Raises:
            Exception: Якщо сталася помилка під час надсилання.
        """
        try:
            self.service.send_sms(self.phone_number, message)
        except:
            print("Помилка надсилання SMS.")


class EmailAdapter:
    """Адаптер для надсилання повідомлень через Email."""

    def __init__(self, service: EmailService, email_address: str):
        """
        Ініціалізує Email-адаптер.

        Arguments:
            service (EmailService): Об'єкт сервісу Email.
            email_address (str): Email-адреса отримувача.
        """
        self.service = service
        self.email_address = email_address


    def send_message(self, message: str):
        """
        Надсилає Email-повідомлення.

        Arguments:
            message (str): Текст повідомлення.

        Raises:
            Exception: Якщо сталася помилка під час надсилання.
        """
        try:
            self.service.send_email(self.email_address, message)
        except:
            print("Помилка надсилання Email.")


class PushAdapter:
    """Адаптер для надсилання повідомлень через Push."""

    def __init__(self, service: PushService, device_id: str):
        """
        Ініціалізує Push-адаптер.

        Arguments:
            service (PushService): Об'єкт сервісу Push.
            device_id (str): Ідентифікатор пристрою отримувача.
        """
        self.service = service
        self.device_id = device_id


    def send_message(self, message: str):
        """
        Надсилає Push-повідомлення.

        Arguments:
            message (str): Текст повідомлення.

        Raises:
            Exception: Якщо сталася помилка під час надсилання.
        """
        try:
            self.service.send_push(self.device_id, message)
        except:
            print("Помилка надсилання Push.")


if __name__ == "__main__":
    adapters = [
        SMSAdapter(SMSService(), "+380xxxxxxxxx"),
        EmailAdapter(EmailService(), "user@mail"),
        PushAdapter(PushService(), "device_1234")
    ]

    for adapter in adapters:
        adapter.send_message("Hello world!")
