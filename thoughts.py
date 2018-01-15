import os
import datetime
from subprocess import call

directory   = r"/mnt/c/Users/pedoe/Documents/code/personalsite/thoughts/"
html_dir    = r"/mnt/c/Users/pedoe/Documents/code/personalsite/thtml/"
files       = os.listdir(directory)
readable_date = str(datetime.date.today())
for file in files:
    thought     = open(directory+ file,"r")
    contents    = thought.read().replace("\n", "<br>")
    name        = thought.name
    name        = name[name.rfind("/")+1:]
    name        = name.split(".txt")[0]
    print name
    print "______________________________"
    thought.close()
    #create a thought html
    print directory+name
    thtml       = open(html_dir+name+".html", "w")
    thtml.write("""<doctype !html>
    <html>
    <head>
      <meta charset="utf-8">
      <title> Thoughts Jonathan Pedoeem</title>
      <link rel="stylesheet" href="../css/bootstrap.css" type="text/css">
      <link rel="stylesheet" href="../css/styles.css" type="text/css">
    </head>
    <body class= "flexCenter">
      <div class = "container" style="width:50%">
        <h1>{0}</h1>
        <small>{1}</small>
        <hr>
        <p>{2}</p>
      </div>
    </body>
    </html>
""".format(name,readable_date, contents))
    thtml.close()
    #delete the thought file
    os.remove(directory+ file)
    #create master thought.html
html_files       = os.listdir(html_dir)
article_list     = []
html_list        = "<ul>"
for hf in html_files:
    article_list.append(("<li><a href='./thtml/{0}'>{1}</a></li>".format(hf, hf[:hf.find('.')]),os.path.getmtime(html_dir+"/"+hf)))
article_list = sorted(article_list, key= lambda s:s[1])
for s in article_list:
    html_list+=s[0]
html_list+= "</ul>"
print html_list
thought_html   =   """<doctype !html>
<html>
<head>
  <meta charset="utf-8">
  <title> Thoughts Jonathan Pedoeem</title>
  <link rel="stylesheet" href="./css/bootstrap.css" type="text/css">
  <link rel="stylesheet" href="./css/styles.css" type="text/css">
</head>
<body>
  <div class = "container">
    <div id = "list">
      <h3>Some of My Thoughts</h3>
      <small>I'm sorry I can't spell.</small>
      <br>
    {0}
    </div>
  </div>
</body>
</html>
""".format(html_list)

thought_file = open("/mnt/c/Users/pedoe/Documents/code/personalsite/thoughts.html", "w")
thought_file.write(thought_html)
thought_file.close()

call("git add --all", shell=True   )
call("git commit -m 'added new essay {0}'".format(readable_date), shell=True)
call('git push', shell=True)
