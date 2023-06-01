from constants import ___


def create_user(user_name: str, user_age: int, after_created: callable) -> None:
    user_id = 111 
    after_created(user_id, user_name)


def send_test_email(user_id: int) -> None:
    print(f"Sending test email to user {user_id}")


if __name__ == "__main__":
    assert create_user(
        user_name="Ilya",
        user_age=32,
        after_created=send_test_email,
    ) is None
