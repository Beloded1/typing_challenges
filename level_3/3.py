from constants import ___
import typing

def create_user(user_name: str, user_age: int, after_created: typing.Callable[[int, str], None]) -> None:
    user_id = 111 
    after_created(user_id, user_name)
   

def send_test_email(user_id: int, user_name: str) -> None:
    print(f"Sending test email to user {user_id} - {user_name}")


if __name__ == "__main__":
    create_user(
        user_name="Ilya",
        user_age=32,
        after_created=send_test_email,
    ) 
