#csqr.py

import os
from csqr_post import CsqrPost

login_id = os.environ.get("MY_LOGIN_ID")
login_pass = os.environ.get("MY_LOGIN_PASSWORD")
slack_api = os.environ.get("MY_SLACK_API_URL")
text = CsqrPost(login_id, login_pass, slack_api).main()
print(text)
