
# Welcome to Sonnet 🔖 

Sonnet currently supports python>=3.0 and notion_client>=2.2.1
# Features:
Sonnet is a lightweight mail-like Notion CLI built with `Click` and packaged with `setuptools`.
Sonnet currently supports reading and sending mail between two specified parties. Users can also filter mail by unread, and burn (delete) all mail from a sender -- perfect for subtle dramatics. Furthermore, Sonnet uses `textwrap` to pretty-print information, including conversation timestamps and participants.

 - `check_mail`:
	 - -r, --recipient: recipient username
	 - -a, --all_mail, default=False: toggle to only show unread (default) or all mail
 - `send_mail`:
	 - -r, --recipient: recipient username
	 - -s, --sender: sender username
	 - -m, --message: message to send
- `burn_mail`:
	- -u, --username: user inbox
	- -s, --sender: sender mail to delete from

# Setup:

1. make sure pip is installed
2. in your project directory, `python3 -m venv .venv`
3.  `source .venv/bin/activate`
4.  `pip install -r requirements.txt`
5.  `pip install .`
6. congrats! run `sonnet` to see how to get started!

# Discussion:
**Future Improvements**
Currently, Sonnet does not include e2e testing, due to the fact that it is still a very barebones wrapper over the extensively-tested notion-client API. However, should Sonnet grow, adding integration/unit testing with `pytest` would be a great start.
To support intuitive mailbox-like features, it would also be exciting to introduce mechanisms to mark mail unread, encrypt secret letters, schedule sending letters, and filter mailbox by sender usernames. 

# Technical Choices:
- Language to use: Python vs JS
	- while JS is understandably the language of choice in prod, Python is much simpler to boostrap together -- thus, I leaned towards Python to quickly prototype my ideas. After iterations and feedback, I would consider swapping to JS for continuity in a greater framework... but for now, it servers our purposes just fine.
 - API to use: argparse vs click
	 - Click ultimately won out, due to it's built-in help messages, less-fussy choices, and simplistic tagging system -- I felt that it was a better representation of a shell-like CLI, especially with `setuptools` integrations.
		- Flexibility -- Since this is a personal instance, it makes sense to use purely client-side frameworks. However, should this become a server-side wrapper, this choice easily lends itself to being a Flask app running on a server, as they share the underlying CLI frameworks.
 - Choosing features that fit the narrative: there was a theme!
	 - Chose features that best align themselves with literature -- "burning all the letters you wrote me"? So Eliza.
	 - In effort to best convey the idea of letters and notes, I templated the display text to suit the style as best as possible.

# References:
[Unofficial Python SDK Notion-client](https://github.com/ramnes/notion-sdk-py)
[Database docs](https://developers.notion.com/docs/working-with-databases)
[Textwrap documentation](https://docs.python.org/3/library/textwrap.html)
[Click documentation](https://click.palletsprojects.com/en/8.1.x)
