# test link removal
x=""" like further clarification, please don't hesitate to [message the mods](http://www.reddit.com/message/compose?to=%2Fr%2FAskReddit&amp;message=My%20Post:%20http://www.reddit.com/r/AskReddit/comments/2qyru6/reddit_who_is_wrong_the_cheater_or_the_cheated/).*"""

import re 
x=re.sub(r"""(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,;@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])""", ' ', x, flags=re.MULTILINE)
print(x)