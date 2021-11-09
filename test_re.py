body_text="""hi http://www.np.reddit.com/r/autowikibot/comments/1ux484/ask_wikibot/_sep_mildlyinfuriating where"""
import  re
body_text=re.sub(r"""(http|ftp|https):\/\/([\w_-]+(?:(?:\.[&\w_-]+)+))([\&\w.,@?^=%&:\/~+#-]*[\&\w@?^=%&\/~+#-])""", ' ', body_text, flags=re.MULTILINE)
print(body_text)