
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

# Testing:
Sonnet unit-tests individual functions with `pytest` and `click-test-runner` packages, mocking away database interactions.
The CLI runner is mocked with click, while underlying notion API calls are patched with pytest mocks.

To run tests, make sure your `venv` is activated.
Then, run `pytest test/test_sonnet.py`.

# Setup:

1. make sure pip is installed
2. in your project directory, `python3 -m venv .venv`
3.  `source .venv/bin/activate`
4.  `pip install -r requirements.txt`
5.  `pip install .`
6. congrats! run `sonnet` to see how to get started!

# Discussion:
**Future Improvements**
Moving forward, it would be good to have a more extensive suite of testing, including real end-to-end tests and mock server instances.
To support intuitive mailbox-like features, it would also be exciting to introduce mechanisms to mark mail unread, encrypt secret letters, schedule sending letters, and filter mailbox by sender usernames.
Similarly, better packaging could provide a more seamless experience.

# Technical Choices:
- Design:
  - CLIs are already unintuitive in regards to state, so make an effort to give as much feedback to the user as possible! Confirm at every step that their actions have happened or errored, and communicate explicitly about the state of the system.
  - Each message opened should have it's own information, and should not rely on users memorizing metadata -- thus the letter format.
- Language to use: Python vs JS
	- while JS is understandably the language of choice in prod, Python is much simpler to boostrap together -- thus, I leaned towards Python to quickly prototype my ideas. After iterations and feedback, I would consider swapping to JS for continuity in a greater framework... but for now, it servers our purposes just fine.
 - API to use: argparse vs click
	 - Click ultimately won out, due to it's built-in help messages, less-fussy choices, and simplistic tagging system -- I felt that it was a better representation of a shell-like CLI, especially with `setuptools` integrations.
		- Flexibility -- Since this is a personal instance, it makes sense to use purely client-side frameworks. However, should this become a server-side wrapper, this choice easily lends itself to being a Flask app running on a server, as they share the underlying CLI frameworks.
 - Choosing features that fit the narrative: there was a theme!
	 - Chose features that best align themselves with literature -- "burning all the letters you wrote me"? So Eliza.
	 - In effort to best convey the idea of letters and notes, I templated the display text to suit the style as best as possible.
 - Organizing modularity -- extracting shared functionality, constants, etc. for cleanliness in reading.
 - Safe coding practices -- i.e. isolating variables with virtualenv, using .env for secret keys, using code cleaning packages like `black` or `flake8` and annotations when possible.

# References:
[Unofficial Python SDK Notion-client](https://github.com/ramnes/notion-sdk-py)
[Database docs](https://developers.notion.com/docs/working-with-databases)
[Textwrap documentation](https://docs.python.org/3/library/textwrap.html)
[Click documentation](https://click.palletsprojects.com/en/8.1.x)
