#!/usr/bin/env python3

import os
from typing import Optional
from constants import __IS_OPENED, __MSG, __RECIPIENT, __SENDER
from notion_client import Client
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv(".env")
notion = Client(auth=os.environ["NOTION_KEY"])


def mark_read_api(page_id: str):
    notion.pages.update(
        **{
            "page_id": page_id,
            "properties": {__IS_OPENED: {"checkbox": True}},
        }
    )


def send_mail_api(message: str, recipient: str, sender: str):
    notion.pages.create(
        **{
            "parent": {"database_id": os.environ["NOTION_PAGE_ID"]},
            "properties": {
                __MSG: {
                    "title": [
                        {"text": {"content": message}},
                    ]
                },
                __RECIPIENT: {
                    "rich_text": [
                        {"text": {"content": recipient}},
                    ]
                },
                __SENDER: {
                    "rich_text": [
                        {"text": {"content": sender}},
                    ]
                },
            },
        }
    )


def delete_mail_api(block_id: str):
    notion.blocks.delete(**{"block_id": block_id, "archived": False})


def get_mail_api(recipient: str, sender: Optional[str] = None, all_mail: bool = False):
    if not all_mail:
        filter_arr = {
            "and": [
                {
                    "property": __RECIPIENT,
                    "rich_text": {
                        "equals": recipient,
                    },
                },
                {
                    "property": __IS_OPENED,
                    "checkbox": {
                        "equals": False,
                    },
                },
            ]
        }
        if sender is not None:
            filter_arr["and"].append(
                {
                    "property": __SENDER,
                    "rich_text": {
                        "equals": sender,
                    },
                }
            )
    elif sender is not None:
        filter_arr = {
            "and": [
                {
                    "property": __RECIPIENT,
                    "rich_text": {
                        "equals": recipient,
                    },
                },
                {
                    "property": __SENDER,
                    "rich_text": {
                        "equals": sender,
                    },
                },
            ]
        }
    else:
        filter_arr = {
            "property": __RECIPIENT,
            "rich_text": {
                "equals": recipient,
            },
        }
    return notion.databases.query(
        **{
            "database_id": os.environ["NOTION_PAGE_ID"],
            "filter": filter_arr,
        }
    )
