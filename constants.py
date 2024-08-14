DEFAULT_TEXT_WIDTH = 70
__RESULTS = "results"
__RECIPIENT = "Recipient"
__SENDER = "Sender"
__MSG = "Message"
__IS_OPENED = "Opened"
__TIMESTAMP = "Timestamp"
__MAIL_TEMPLATE = """\
.-"-._,-'_`-._,-'_`-._,-'_`-._,-'_`-,_,-'_`-,_,-'_`-,_,-'_`-,_,-'_`-,.
{__TIMESTAMP}\n\t
from:{__SENDER}
to:{__RECIPIENT}
======================================================================
message:
{__MSG}
======================================================================


  """
__HELP_STR_TEMPLATE = """
.-"-._,-'_`-._,-'_`-._,-'_`-._,-'_`-,_,-'_`-,_,-'_`-,_,-'_`-,_,-'_`-,.

  Welcome to Sonnet 🕊️🕊️ a Notion Mailbox CLI 🔖 
  
.-"-._,-'_`-._,-'_`-._,-'_`-._,-'_`-,_,-'_`-,_,-'_`-,_,-'_`-,_,-'_`-,.
    Please select an option:
  - send_mail: Send mail {message} from {recipient} to {sender}
  Options:
    -s, --sender TEXT     Sender username  [required]
    -r, --recipient TEXT  Recipient username  [required]
    -m, --message TEXT    Message to send  [required]
    --help                Show this message and exit.

  - check_mail: Check mail in {recipient}'s inbox.
  Options:
    -r, --recipient TEXT  Recipient username  [required]
    -a, --all_mail        Show all mail
    --help                Show this message and exit.
  
  - burn_mail: Burn mail from {sender} in {username}'s inbox.
  Options:
    -u, --username TEXT  Username  [required]
    -s, --sender TEXT    Sender username  [required]
    --help               Show this message and exit.
  """
