from unittest.mock import patch

from click.testing import CliRunner

from sonnet import burn_mail, check_mail, send_mail

TEST_MESSAGE = "test message"
TEST_RECIPIENT = "james"
TEST_SENDER = "ravi"
MOCK_RESULT_NO_MAIL = {"results": []}
MOCK_RESULT_GET_MAIL = {
    "results": [
        {
            "id": "0000",
            "last_edited_time": "20240812",
            "properties": {
                "Opened": {"id": "PHrf", "type": "checkbox", "checkbox": True},
                "Recipient": {
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {"content": "james", "link": "None"},
                            "plain_text": "james",
                            "href": "None",
                        }
                    ],
                },
                "Sender": {
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {"content": "ravi", "link": "None"},
                            "plain_text": "ravi",
                            "href": "None",
                        }
                    ],
                },
                "Message": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Give me the light: upon thy life, I charge thee, Whate'er thou hear'st or seest, stand all aloof, And do not interrupt me in my course. If thou, jealous, dost return to pry In what I further shall intend to do, By heaven, I will tear thee joint by joint",
                                "link": "None",
                            },
                            "plain_text": "Give me the light: upon thy life, I charge thee, Whate'er thou hear'st or seest, stand all aloof, And do not interrupt me in my course. If thou, jealous, dost return to pry In what I further shall intend to do, By heaven, I will tear thee joint by joint",
                            "href": "None",
                        }
                    ],
                },
            },
        }
    ]
}


def test_check_all_mail():
    runner = CliRunner()
    with patch("sonnet.get_mail_api", return_value=MOCK_RESULT_GET_MAIL):
        with patch("sonnet.mark_read_api"):
            result = runner.invoke(
                check_mail, ["--recipient", TEST_RECIPIENT, "--all_mail"]
            )
            assert result.exit_code == 0
            assert "Mail: (1)" in result.output
            assert "Give me the light: upon thy life, I charge thee" in result.output


def test_check_no_new_mail():
    runner = CliRunner()
    with patch("sonnet.get_mail_api", return_value=MOCK_RESULT_NO_MAIL):
        with patch("sonnet.mark_read_api"):
            result = runner.invoke(check_mail, ["--recipient", TEST_RECIPIENT])
            assert result.exit_code == 0
            assert "New Mail: (0)" in result.output


def test_send_mail():
    runner = CliRunner()
    with patch("sonnet.send_mail_api"):
        result = runner.invoke(
            send_mail,
            [
                "--sender",
                TEST_SENDER,
                "--recipient",
                TEST_RECIPIENT,
                "--message",
                TEST_MESSAGE,
            ],
        )
        assert result.exit_code == 0
        assert TEST_MESSAGE in result.output


def test_burn_mail():
    runner = CliRunner()
    with patch("sonnet.get_mail_api", return_value=MOCK_RESULT_GET_MAIL):
        with patch("sonnet.delete_mail_api"):
            result = runner.invoke(
                burn_mail, ["--username", TEST_RECIPIENT, "--sender", TEST_SENDER]
            )
            assert result.exit_code == 0
            assert "Burning (1) letter(s)" in result.output


def test_burn_no_mail():
    runner = CliRunner()
    with patch("sonnet.get_mail_api", return_value=MOCK_RESULT_NO_MAIL):
        result = runner.invoke(
            burn_mail, ["--username", TEST_RECIPIENT, "--sender", TEST_SENDER]
        )
        assert result.exit_code == 0
        assert f"No messages to burn from sender {TEST_SENDER}..." in result.output
