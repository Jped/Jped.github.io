import os
import datetime
directory   = r"C:\Users\pedoe\Documents\code\personalsite\thoughts\\"
html_dir    = r"C:\Users\pedoe\Documents\code\personalsite\thtml\\"
files       = os.listdir(directory)
for file in files:
    thought     = open(directory+ file,"r")
    contents    = thought.read().replace("\n", "<br>")
    name        = thought.name
    name        = name[name.rfind("\\")+1:]
    print name
    print "______________________________"
    thought.close()
    #create a thought html
    print directory+name
    thtml       = open(html_dir+name.replace(".txt",".html"), "w")
    thtml.write("""<doctype !html>
    <html>
    <head>
      <meta charset="utf-8">
      <title> Thoughts Jonathan Pedoeem</title>
      <link rel="stylesheet" href="./css/bootstrap.css" type="text/css">
      <link rel="stylesheet" href="./css/styles.css" type="text/css">
    </head>
    <body class= "flexCenter">
      <div class = "container">
        <h1>{0}</h1>
        <small>{1}</small>
        <hr>
        <p>{2}</p>
      </div>
    </body>
    </html>
""".format(name,str(datetime.date.today()), contents))
    thtml.close()
    #delete the thought file
    os.remove(directory+ file)
    #create master thought.html
html_files       = os.listdir(html_dir)
html_list        = "<ul>"
for hf in html_files:
    html_list+="<li><a href='./thml/{0}''>{1}</a></li>".format(hf, hf[:hf.find('.')])

html_list+= "</ul>"
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

thought_file = open("thoughts.html", "w")
thought_file.write(thought_html)
thought_file.close()
