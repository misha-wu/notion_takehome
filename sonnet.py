#!/usr/bin/env python3

from logging import getLogger
import click
import textwrap
from constants import (
    __HELP_STR_TEMPLATE,
    __MAIL_TEMPLATE,
    __MSG,
    __RESULTS,
    __SENDER,
    DEFAULT_TEXT_WIDTH,
)
from notion_client import APIResponseError
from utils import get_mail_api, mark_read_api, send_mail_api, delete_mail_api

logger = getLogger(__name__)


# add timestamps
@click.command()
@click.option("-s", "--sender", help="Sender username", required=True)
@click.option("-r", "--recipient", help="Recipient username", required=True)
@click.option("-m", "--message", help="Message to send", required=True)
def send_mail(sender: str, recipient: str, message: str) -> None:
    """
    Send mail {message} from {recipient} to {sender}
    """
    try:
        send_mail_api(message, recipient, sender)
        click.echo(f"️🔖 Sent letter with message: {message}")
    except APIResponseError as error:
        click.echo(error)


# add timestamps
@click.command()
@click.option("-u", "--username", help="Username", required=True)
@click.option("-s", "--sender", help="Sender username", required=True)
def burn_mail(username: str, sender: str) -> None:
    """
    Burn mail from {sender} in {username}'s inbox.
    """
    try:
        mail_results = get_mail_api(username, sender, all_mail=True)[__RESULTS]
        if len(mail_results) == 0:
            click.echo(f"️‍No messages to burn from sender {sender}...")
            return
        click.echo(f"️‍🔥️ Burning ({len(mail_results)}) letter(s) ️‍🔥️")
        for result in mail_results:
            page_id = result["id"]
            delete_mail_api(page_id)
    except APIResponseError as error:
        # pass through the errors, since the underlying api is descriptive
        click.echo(error)


@click.command()
@click.option("-r", "--recipient", help="Recipient username", required=True)
@click.option(
    "-a",
    "--all_mail",
    is_flag=True,
    show_default=True,
    default=False,
    help="Show all mail",
)
def check_mail(recipient: str, all_mail: bool):
    """
    Check mail in {recipient}'s inbox.
    """
    try:
        mail_results = get_mail_api(recipient, all_mail=all_mail)[__RESULTS]
        if all_mail:
            click.echo(f"\t🕊️ Mail: ({len(mail_results)})")
        else:
            click.echo(f"\t🕊️ New Mail: ({len(mail_results)})")
        for result in mail_results:
            page_id = result["id"]

            time = result["last_edited_time"]
            columns = result["properties"]
            mail_str = __MAIL_TEMPLATE.format(
                __TIMESTAMP=time,
                __RECIPIENT=recipient,
                __SENDER=columns[__SENDER]["rich_text"][0]["plain_text"],
                __MSG=columns[__MSG]["title"][0]["plain_text"],
            )
            click.echo(
                textwrap.fill(mail_str, DEFAULT_TEXT_WIDTH, replace_whitespace=False)
            )
            mark_read_api(page_id)

    except APIResponseError as error:
        click.echo(error)


@click.command()
def sonnet():
    click.echo(__HELP_STR_TEMPLATE)
