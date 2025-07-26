from flask import Flask, request, render_template_string,redirect,session,send_file
from weasyprint import HTML

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/")
def home():
	return redirect("/dashboard")

@app.route("/login",methods=["GET","POST"])
def login():
	return"""
        <body bgcolor=#ebff66>
</br>

<form method="POST" action="/adminlogin"><input type="submit" value="Admin Login" style="position: relative; left: 80%; width:120px; border-radius: 15px; font-size:15px; color: royalblue; font-weight: bold; height: 45px; background-color: white; border:3px dashed blue;"></form>

<center>

<h1 style="font-family:calibri; color:#0b0478; font-size:40px;">Please enter Log In details below:</h1></br>

<p style="font-family:calibri; font-size:18px; color:#444444; background-color:#fffacd; padding:10px 20px; border-radius:15px; width:50%; border:2px dashed #0b0478;">For testing purpose, use <b>Username: ali</b> and <b>Password: raffay</b></p></br>

<form method="POST" action="/loggedin">
    <b></b> <input name="username" placeholder="Enter Username" style="width:50%; height:50px; font-size:16px; border-top:0px; border-left:0px; border-right:0px; border-bottom:2px dashed blue; background-color:white; padding:8px;"></br></br>
    <b></b> <input name="password" type="password" placeholder="Enter Password" style="width:50%; height:50px; font-size:16px; border-top:0px; border-left:0px; border-right:0px; border-bottom:2px dashed blue; background-color:white; padding:8px;"></br></br>
    <input type="submit" value="Log In" style="background-color:#ffff00; font-family:bahnschrift; font-size:16px; font-weight:bold; border-width:1px; height:44px; width:50%; border-radius:40px; color:#220080;"></br>
</form>

</center></body>
	"""

@app.route("/addcategory", methods=["POST","GET"])
def addcategory():
	password = session.get("password")
	with open("admin.txt", "r") as file:
		multilines = file.readlines()
	for singleline in multilines:
		line = singleline.strip().split(",")
		if line[0] == password:
			return"""
<body bgcolor="#fcba03">
<table style="width: 80%; position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); height:120px; padding: 10px; background-color: white; border-radius: 20px; border: 3px dashed darkred;">
  <tr>
    <td width="25%" style="padding-left:15px;"><p style="font-size: 25px; font-weight: bold; color: #ad7c00; font-family:calibri;">Add Category :</p></td>
    <td width="75%"><form method="POST" action="/addcategoryp"><input name="cat" placeholder="Add Product Category" style="font-size:15px; padding-left: 14px; padding-right: 14px; background-color: #ebebeb; width: 65%; height: 50px; border-left: none; border-right: none; border-top: none; border-bottom: 3px dashed navy;">&nbsp &nbsp &nbsp<input type="submit" value="Add Category" style="font-size:15px; padding-left: 14px; padding-right: 14px; background-color: white; border-radius: 15px; width: 25%; height: 53px; border: 3px dashed navy;"></form></td>
  </tr>
</table>
</body>

			"""



@app.route("/addcategoryp", methods=["POST"])
def addcategoryp():
	category = request.form.get("cat")
	h=[]
	with open("categories.txt", "r") as file:
		multilines=file.readlines()
	for singleline in multilines:
		line=singleline.strip().split(",")
		h+=line
		if category in line:
			return "Category Already Exists"
	h.append(category)
	with open("categories.txt", "w") as filex:
		filex.writelines(",".join(h))

	return redirect("/adminreadcat")





@app.route("/adminlogin", methods=["POST"])
def adlogin():
	return"""
    <body bgcolor=#ebff66>
</br>

<form method="POST" action="/login"><input type="submit" value="User Login" style="position: relative; left: 80%; width:120px; border-radius: 15px; font-size:15px; color: royalblue; font-weight: bold; height: 45px; background-color: white; border:3px dashed blue;"></form>

<center></br></br>

<h1 style="font-family:calibri; color:#0b0478; font-size:40px;">Please enter Log In details below:</h1></br>

<p style="font-family:calibri; color:#003366; font-size:18px;"><i>For testing purpose, use password: <b>ALIraffay!($</b> (no username required)</i></p></br>

<form method="POST" action="/adminlog">
    <b></b> <input name="password" type="password" placeholder="Enter Password" style="width:50%; height:50px; font-size:16px; border-top:0px; border-left:0px; border-right:0px; border-bottom:2px dashed blue; background-color:white; padding:8px;"></br></br>
    <input type="submit" value="Log In" style="background-color:#ffff00; font-family:bahnschrift; font-size:16px; font-weight:bold; border-width:1px; height:44px; width:50%; border-radius:40px; color:#220080;"></br>
</form>

</center></body>
	"""



@app.route("/adminlog", methods=["POST"])
def adminlogprocess():
	password=request.form.get("password")
	session["password"]=password
	with open("admin.txt", "r") as file:
		multilines=file.readlines()
	for singleline in multilines:
		line=singleline.strip().split(",")
		if line[0]==password:
			return redirect("/admin")
		else:
			return redirect("/login")


@app.route("/admin", methods=["GET"])
def adminblock():
	password = session.get("password")
	with open("admin.txt", "r") as file:
		multilines = file.readlines()
	for singleline in multilines:
		line = singleline.strip().split(",")
		if line[0] == password:
			return """
<body bgcolor="#e6f2f0">
<center>

<form action="/logout" method="POST">
  <input type="submit" value="Log Out" style="position: absolute; right: 30px; top: 20px; font-size: 15px; font-weight: bold; padding: 10px 20px; background-color: #f08080; border: 2px dashed red; border-radius: 20px; color: white;">
</form>

<br>
<h1 style="color: #4b0082; font-size: 37px; font-family: lobster;">Admin Dashboard</h1>
<br><br>

<form action="/adminread" method="POST">
  <input type="submit" value="Check Products" style="color: #4b0082; font-size: 17px; font-weight: bold; width: 70%; height: 60px; background-color: #e6e6fa; border: 3px dashed #6a5acd; border-radius: 22px;">
</form><br>

<form action="/adminadd" method="POST">
  <input type="submit" value="ADD Product" style="color: #4b0082; font-size: 17px; font-weight: bold; width: 70%; height: 60px; background-color: #e6e6fa; border: 3px dashed #6a5acd; border-radius: 22px;">
</form><br>

<form action="/admindelete" method="POST">
  <input type="submit" value="Delete Product" style="color: #4b0082; font-size: 17px; font-weight: bold; width: 70%; height: 60px; background-color: #e6e6fa; border: 3px dashed #6a5acd; border-radius: 22px;">
</form><br>

<form action="/adminupdate" method="POST">
  <input type="submit" value="Update Products" style="color: #4b0082; font-size: 17px; font-weight: bold; width: 70%; height: 60px; background-color: #e6e6fa; border: 3px dashed #6a5acd; border-radius: 22px;">
</form><br>

<form action="/adduser" method="POST">
  <input type="submit" value="Add User" style="color: #4b0082; font-size: 17px; font-weight: bold; width: 70%; height: 60px; background-color: #e6e6fa; border: 3px dashed #6a5acd; border-radius: 22px;">
</form>
<br>
<form action="/addcategory" method="POST">
  <input type="submit" value="Add Category" style="color: #4b0082; font-size: 17px; font-weight: bold; width: 70%; height: 60px; background-color: #e6e6fa; border: 3px dashed #6a5acd; border-radius: 22px;">
</form>
<br><br>
</center>
</body>
"""

		else:
			return redirect("/login")



@app.route("/adduser", methods=["POST","GET"])
def add_user():
	password=session.get("password")
	with open ("admin.txt", "r") as file:
		multilines=file.readlines()
	for singleline in multilines:
		line = singleline.strip().split(",")
		if line[0] == password:
			return"""
	<body bgcolor="#fae755">

	

<br><br><br>
<center>
<div style="width: 40%; height: 435px; background-color: white; padding: 30px; border: 2px dashed darkred; border-radius: 40px;">
<h1 align="center" style="color: #d4a200; font-family: calibri; font-size: 36px;">Add Receipt Operator</h1>
<center><form method="POST" action="/adduserp"><br>
<input type="text" placeholder="Username" name="username" style="width: 90%; height: 55px; border-right: none; border-left: none; border-top: none; border-bottom: 3px dashed blue; padding-left:15px; background-color: whitesmoke;"><br><br>
<input type="text" placeholder="Password" name="password" style="width: 90%; height: 55px; border-right: none; border-left: none; border-top: none; border-bottom: 3px dashed blue; padding-left:15px; background-color: whitesmoke;"><br><br>
<select name="role" style="width: 90%; height: 55px; border-right: none; border-left: none; border-top: none; border-bottom: 3px dashed blue; padding-left:15px; background-color: whitesmoke;">
	<option value="receipt">Receipt Operator</option>
	<option value="admin">Administrator</option>
</select><br><br>
<input type="submit" value="Add User" style="width: 90%; font-size:17px; font-family: calibri; font-weight: bold; height: 55px; border: 3px dashed darkred; padding-left:15px; background-color: white;">



</form></center>

</div>
</center>



</body>

	"""




@app.route("/adduserp", methods=["POST"])
def adduserp():
	username=request.form.get("username")
	password=request.form.get("password")
	det=[]
	role=request.form.get("role")
	if role == "receipt":
		with open("users.txt", "r") as file:
			multilines=file.readlines()
		for singleline in multilines:
			line=singleline.strip().split(",")
			det.append(line[0])
		if username not in det:
			with open("users.txt", "a") as file:
				file.write(username+","+password+"\n")
				return redirect("/login")
		else:
			return redirect("/adduser")

	else:
		with open("admin.txt", "r") as file:
			multilines=file.readlines()
		for singleline in multilines:
			line=singleline.strip().split(",")
			det.append(line[0])
		if username not in det:
			with open("admin.txt", "a") as file:
				file.write(username+","+password+"\n")
				return redirect("/login")
		else:
			return redirect("/adduser")





@app.route("/adminread", methods=["POST","GET"])
def adminread():
	password=session.get("password")
	with open("admin.txt", "r") as file:
		multilines=file.readlines()
	for singleline in multilines:
		line=singleline.strip().split(",")
		if line[0]==password:
			h="""<br><br><center><form method="GET" action="/adminreadcat"><input type="submit" value="Read Products By Category" style="width:70%; height:45px; border-radius:14px; background-color:green; color:white; border:3px dashed yellow; font-size:15px; font-weight:bold; font-family:arial;"></form></center><br><br><br>"""
			with open("labels.txt", "r") as file:
				multilines=file.readlines()
			for singleline in multilines:
				line = singleline.strip().split(",")
				with open("items.txt", "r") as files:
					multilinex=files.readlines()
				for singlelinex in multilinex:
					linex = singlelinex.split(",")
					h=h+"""<body bgcolor=#c1b8d6><center><table style="width: 70%; border: 2px dashed blue; padding-left:25px; padding-top:10px; padding-bottom:10px; font-family:calibri; font-size:18px; padding-right:25px; background-color: white; border-radius: 30px;">"""
					for label, item in zip(line,linex):
						h=h+"""

				<tr><td style="padding:10px; font-weight:bold;" width=50%>"""+label+"""</td><td width="50%" align=right style="padding:10px;">"""+item+"""</td></tr>



				"""
					h=h+"""</table></center></body><br>"""
			return h+"""<br><br><center><form method="GET" action='/admin'><input type="submit" value="Back to Admin Dashboard" style="width:60%; height:45px; border-radius:15px; background-color:#4b0082; color:white; font-size:17px; font-weight:bold; font-family:arial; border:3px dashed #9370db;"></form></center><br><br>"""
		else:
			return redirect("/login")








@app.route("/adminreadcatp", methods=["POST", "GET"])
def adminreadcat_post():
    password = session.get("password")
    category = request.form.get("productcat")

    with open("admin.txt", "r") as file:
        admin_lines = file.readlines()

    for admin_line in admin_lines:
        admin_fields = admin_line.strip().split(",")
        if admin_fields[0] == password:
            h = ""
            with open("labels.txt", "r") as file:
                label_line = file.readline().strip()
                labels = label_line.split(",")

            with open("items.txt", "r") as files:
                item_lines = files.readlines()

            for item_line in item_lines:
                linex = item_line.strip().split(",")
                if len(linex) > 11 and linex[11].strip().lower() == category.lower():
                    h += """<body bgcolor=#c1b8d6><center><table style="width: 70%; border: 2px dashed blue; padding-left:25px; padding-top:10px; padding-bottom:10px; font-family:calibri; font-size:18px; padding-right:25px; background-color: white; border-radius: 30px;"><center><h1 style="font-family:arial; color:#8c0013;">""" + category.title() + """</h1></center>"""

                    for label, item in zip(labels, linex[:-1]):
                        h += """
<tr><td style="padding:10px; font-weight:bold;" width=50%>""" + label + """</td><td width="50%" align=right style="padding:10px;">""" + item + """</td></tr>
"""

                    h += "</table></center></body><br>"

            return h+"""<br><br><center><form method="GET" action='/admin'><input type="submit" value="Back to Admin Dashboard" style="width:60%; height:45px; border-radius:15px; background-color:#4b0082; color:white; font-size:17px; font-weight:bold; font-family:arial; border:3px dashed #9370db;"></form></center><br><br>"""

    return redirect("/login")






@app.route("/adminreadcat", methods=["GET", "POST"])
def adminreadcatg():
	hh="""<select name="productcat" id="productcat" style="width:80%; font-family:arial; font-size:16px; padding-left:12px; padding-right:12px; height:50px; border:3px dashed blue;"><option value="" disabled selected hidden>Select Category</option>"""
	password=session.get("password")
	with open("categories.txt", "r") as categories:
		categoryss=categories.read()
		categorys = categoryss.strip().split(",")
	for category in categorys:
		hh=hh+"""<option value="""+category.lower()+""">"""+category+"""</option>"""
	hh=hh+"""</select>"""
	html = """<br><br><br><br><center>
<form method="POST" action="/adminreadcatp">""" + hh + """<br><br>
<input type="submit" value="Search Products By Caregory" style="width:80%; height:45px; border-radius:14px; background-color:white; border:3px dashed red; font-size:15px; font-weight:bold; font-family:arial;">
</form></center>"""

	return html+"""<br><br><center><form method="GET" action='/admin'><input type="submit" value="Back to Admin Dashboard" style="width:60%; height:45px; border-radius:15px; background-color:#4b0082; color:white; font-size:17px; font-weight:bold; font-family:arial; border:3px dashed #9370db;"></form></center><br><br>"""





@app.route("/adminadd", methods=["POST"])
def adminadd():
	hh="""<select name="productcat" id="productcat" style="width:80%; font-family:arial; font-size:16px; padding-left:12px; padding-right:12px; height:50px; border:3px dashed blue;"><option value="" disabled selected hidden>Select Category</option>"""
	password=session.get("password")
	with open("categories.txt", "r") as categories:
		categoryss=categories.read()
		categorys = categoryss.strip().split(",")
	for category in categorys:
		hh=hh+"""<option value="""+category.lower()+""">"""+category+"""</option>"""
	hh=hh+"""</select>"""
	session["hh"]=hh


	with open("admin.txt", "r") as file:
		multilines=file.readlines()
	for singleline in multilines:
		line=singleline.strip().split(",")
		if line[0]==password:
			return"""
			<br>
<center><h1 style="font-family:Arial; color:#8f3ca3;">Add Product To Your Stock</h1><br><br>

<form method="POST" action="/adminaddprocess">
  <input type="text" name="productid" placeholder="Product ID" style="width:80%; height: 55px; font-size: 18px; padding-left: 15px; padding-right: 15px; border: 3px dashed #0077b6; border-radius: 20px;"><br><br>
  <input type="text" name="productname" placeholder="Product Name" style="width:80%; height: 55px; font-size: 18px; padding-left: 15px; padding-right: 15px; border: 3px dashed #0077b6; border-radius: 20px;"><br><br>
  <input type="text" name="producttype" placeholder="Product Type" style="width:80%; height: 55px; font-size: 18px; padding-left: 15px; padding-right: 15px; border: 3px dashed #0077b6; border-radius: 20px;"><br><br>
  <input type="text" name="productsize" placeholder="Product Size" style="width:80%; height: 55px; font-size: 18px; padding-left: 15px; padding-right: 15px; border: 3px dashed #0077b6; border-radius: 20px;"><br><br>
  <input type="text" name="productprice" placeholder="Product Price" style="width:80%; height: 55px; font-size: 18px; padding-left: 15px; padding-right: 15px; border: 3px dashed #0077b6; border-radius: 20px;"><br><br>
  <input type="text" name="productcolor" placeholder="Product Color" style="width:80%; height: 55px; font-size: 18px; padding-left: 15px; padding-right: 15px; border: 3px dashed #0077b6; border-radius: 20px;"><br><br>
  <input type="text" name="productweight" placeholder="Product Weight" style="width:80%; height: 55px; font-size: 18px; padding-left: 15px; padding-right: 15px; border: 3px dashed #0077b6; border-radius: 20px;"><br><br>
  <input type="text" name="productmaterial" placeholder="Product Material" style="width:80%; height: 55px; font-size: 18px; padding-left: 15px; padding-right: 15px; border: 3px dashed #0077b6; border-radius: 20px;"><br><br>
  <input type="text" name="productbrand" placeholder="Product Brand" style="width:80%; height: 55px; font-size: 18px; padding-left: 15px; padding-right: 15px; border: 3px dashed #0077b6; border-radius: 20px;"><br><br>
  <input type="text" name="productrating" placeholder="Product Rating" style="width:80%; height: 55px; font-size: 18px; padding-left: 15px; padding-right: 15px; border: 3px dashed #0077b6; border-radius: 20px;"><br><br>
  <input type="text" name="productavailability" placeholder="Product Availability" style="width:80%; height: 55px; font-size: 18px; padding-left: 15px; padding-right: 15px; border: 3px dashed #0077b6; border-radius: 20px;"><br><br>"""+hh+"""<br><br>
  <input type="submit" value="Add Product To Stock" style="width:80%; height: 45px; border-radius: 15px; border: 3px dashed #ff6b6b; background-color: #001f3f; color: #f8f9fa; font-weight: bold; font-size: 20px;">
</form>
</center>"""+"""<br><br><center><form method="GET" action='/admin'><input type="submit" value="Back to Admin Dashboard" style="width:60%; height:45px; border-radius:15px; background-color:#4b0082; color:white; font-size:17px; font-weight:bold; font-family:arial; border:3px dashed #9370db;"></form></center><br><br>"""






@app.route("/adminaddprocess", methods=["POST"])
def processadd():
	prod=""
	password=session.get("password")
	with open("admin.txt", "r") as file:
		multilines=file.readlines()
	for singleline in multilines:
		line=singleline.strip().split(",")
		if line[0]==password:
			pid=request.form.get("productid")
			pname=request.form.get("productname")
			ptype=request.form.get("producttype")
			psize=request.form.get("productsize")
			pprice=request.form.get("productprice")
			pcolor=request.form.get("productcolor")
			pweight=request.form.get("productweight")
			pmaterial=request.form.get("productmaterial")
			pbrand=request.form.get("productbrand")
			prating=request.form.get("productrating")
			pavail=request.form.get("productavailability")
			pcat=request.form.get("productcat")
			prod=pid+","+pname+","+ptype+","+psize+","+pprice+","+pcolor+","+pweight+","+pmaterial+","+pbrand+","+prating+","+pavail+","+pcat+"\n"
			with open("items.txt","a") as file:
				file.writelines(prod)
				return redirect("adminread")
	return "Sorry, Not logged in"








@app.route("/admindelete", methods=["GET","POST"])
def admindelete():
	httml="""<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body bgcolor="#fcba03">

"""

	password=session.get("password")
	with open("admin.txt", "r") as file:
		multilines=file.readlines()
	for singleline in multilines:
		line=singleline.strip().split(",")
		if password==line[0]:
			with open("labels.txt") as labelfile:
				multilineslabel = labelfile.readlines()
			for singlelinelabel in multilineslabel:
				labelline = singlelinelabel.strip().split(",")
				with open("items.txt", "r") as itemfile:
					multiitemlines = itemfile.readlines()
				for singleitemline in multiitemlines:
					itemline = singleitemline.strip().split(",")
					httml+="""<center><table style="width: 80%; font-family:arial; padding: 10px; background-color: white; border-radius: 25px; border: 3px dashed darkred;"><tr><td width="75%"></td><td width="25%" style="padding-bottom:25px;"><form method="POST" action="/admindeletepro"><input type="submit" value="Delete Product" style="width:100%; height:40px; background-color:white; border:3px dashed darkblue; border-radius:10px;" name="""+itemline[0]+"""></form></td></tr>"""
					for items, things in zip(itemline,labelline):
						httml= httml+"""<tr><td style="padding: 10px;">"""+things+"""</td>"""+"""<td style="padding: 10px;">"""+items+"""</td></tr>"""
					httml+="""</table></center><br><br>"""
			httml=httml+"""</body></html>"""
	return httml+"""<br><br><center><form method="GET" action='/admin'><input type="submit" value="Back to Admin Dashboard" style="width:60%; height:45px; border-radius:15px; background-color:#4b0082; color:white; font-size:17px; font-weight:bold; font-family:arial; border:3px dashed #9370db;"></form></center><br><br>"""







@app.route("/admindeletepro", methods=["POST"])
def admindeletepro():
	listssss = []
	updatedlist=[]
	delitem = ""
	password = session.get("password")

	with open("admin.txt", "r") as file:
		multilines = file.readlines()

	for singleline in multilines:
		line = singleline.strip().split(",")
		if password == line[0]:
			with open("items.txt", "r") as files:
				multlinesf = files.readlines()
			for singlelinef in multlinesf:
				linef = singlelinef.strip().split(",")
				for item in linef:
					if item == linef[0]:
						listssss.append(item)

			for itemx in listssss:
				itemdel = request.form.get(itemx)
				if itemdel is not None:
					delitem += itemx

			with open("items.txt", "r") as filef:
				multilinef = filef.readlines()
			for singlelinef in multilinef:
				linef=singlelinef.strip().split(",")
				if linef[0] != delitem:
					updatedlist.append(",".join(linef)+"\n")
			updatedlistline = ",".join(updatedlist)+"\n"
			with open("items.txt", "w")	as updatelistfile:
				updatelistfile.writelines(updatedlist)
				return redirect("/admindelete")







@app.route("/adminupdate", methods=["GET","POST"])
def adminupdate():
	password=session.get("password")
	with open("admin.txt", "r") as file:
		multilines=file.readlines()
	for singleline in multilines:
		line = singleline.strip().split(",")
		if password==line[0]:
			return"""


<body bgcolor="#fcba03">
<table style="width: 80%; height:120px; padding: 10px; background-color: white; border-radius: 20px; border: 3px dashed darkred; position: absolute; top: 50%;left: 50%; transform: translate(-50%, -50%);">
	<tr>
		<td width="25%" style="padding-left:15px;"><p style="font-size: 25px; font-weight: bold; color: #ad7c00; font-family:calibri;">Update Item :</p></td>
		<td width="75%"><form method="POST" action="/adminupdatepro"><input name="updateitem" placeholder="Enter Product ID" style="font-size:15px; padding-left: 14px; padding-right: 14px; background-color: #ebebeb; width: 65%; height: 50px; border-left: none; border-right: none; border-top: none; border-bottom: 3px dashed navy;">&nbsp &nbsp &nbsp<input type="submit" value="Update Item" style="font-size:15px; padding-left: 14px; padding-right: 14px; background-color: white; border-radius: 15px; width: 25%; height: 53px; border: 3px dashed navy;"></form></td>
	</tr>
</table>
</body>


"""+"""<br><br><center><form method="GET" action='/admin'><input type="submit" value="Back to Admin Dashboard" style="width:60%; height:45px; border-radius:15px; background-color:#4b0082; color:white; font-size:17px; font-weight:bold; font-family:arial; border:3px dashed #9370db;"></form></center><br><br>"""

@app.route("/adminupdatepro", methods=["POST"])
def adminupdatepro():
    password = session.get("password")
    htttml = """<center><form method="POST" action="/adminupdatepro_s">
<table style="width:80%; background-color: whitesmoke;">"""

    update_item = request.form.get("updateitem")

    with open("admin.txt", "r") as file:
        multilines = file.readlines()

    for singleline in multilines:
        line = singleline.strip().split(",")
        if password == line[0]:
            with open("items.txt", "r") as files:
                multilinex = files.readlines()
            for singlelinex in multilinex:
                linex = singlelinex.strip().split(",")
                if update_item == linex[0]:
                    with open("labels.txt", "r") as fike:
                        multilinesk = fike.readlines()

                    for singlelinek in multilinesk:
                        linek = singlelinek.strip().split(",")

                        for itemx, thingx in zip(linex, linek):
                            htttml += """<tr>
        <td width="40%" style="padding-left: 15px; font-size: 20px; font-family: calibri;">""" + thingx + """</td>
        <td width="60%">
            <input name='""" + thingx + """' value='""" + itemx + """' style="width: 100%; height: 50px; padding-left: 15px; font-size: 20px; font-family: calibri;">
        </td>
    </tr>"""

                    htttml += """</table><br>
<table style="width:80%;">
    <tr>
        <td>
            <input type="submit" value="Update All Items" style="height: 50px; width:100%; font-size: 20px; font-family: calibri; background-color: white; border: 4px dotted red; border-radius: 20px;">
        </td>
    </tr>
</table>
</form></center>"""

    return htttml+"""<br><br><center><form method="GET" action='/admin'><input type="submit" value="Back to Admin Dashboard" style="width:60%; height:45px; border-radius:15px; background-color:#4b0082; color:white; font-size:17px; font-weight:bold; font-family:arial; border:3px dashed #9370db;"></form></center><br><br>"""






@app.route("/adminupdatepro_s", methods=["POST"])
def adminupdatepro_s():
	updates=[]
	listsx=[]
	dataa=request.form.get("Product Name")
	with open("labels.txt", "r") as file:
		multilines = file.readlines()
	for singleline in multilines:
		line = singleline.strip().split(",")
		with open("items.txt", "r") as filex:
			multilinex = filex.readlines()
		for singlelinex in multilinex:
			linex = singlelinex.strip().split(",")
			for i in line:
				updated_item = request.form.get(i)
				updates.append(updated_item)
			listsx.append(",".join(updates)+"\n")
			break


	with open("items.txt", "r") as filed:
		multilined = filed.readlines()
	for singlelined in multilined:
		lined = singlelined.strip().split(",")
		if lined[0]!=dataa:
			listsx.append(",".join(lined)+"\n")
	with open("items.txt", "w") as filej:
		filej.writelines(listsx)
	return redirect("/adminread")



@app.route("/loggedin", methods=["POST"])
def loggedin():
	username = request.form.get("username")
	password = request.form.get("password")
	session["username"]=username
	session["password"]=password
	return redirect("/dashboard")


@app.route("/dashboard", methods=["GET"])
def dashboard():
    username = session.get("username")
    password = session.get("password")
    html = ""
    
    with open("users.txt", "r") as file:
        multilines = file.readlines()

    for singleline in multilines:
        line = singleline.strip().split(",")
        if line[0] == username and line[1] == password:
            html += """ 
            <center><br><br><br><br><br><br>
                <table style="width: 70%; border: 4px dashed blue; height: 70px; background-color: white; border-radius: 30px;">
                    <tr>
                        <td style="padding-left: 25px; padding-bottom:0px; font-family: calibri; font-size: 22px; width: 50%;">
                            Enter Product Id:
                        </td>
                        <td style="padding-top:20px; height:45px; padding-bottom:0px; padding-right: 35px; font-family: calibri; font-size: 22px; width: 50%; text-align: right; border-top: 0px;">
                            <form method="POST" action="/add">
                                <input name="item" placeholder="Enter Product ID here"
                                    style="width:60%; height: 45px; padding: 0px; border-right: 0px;
                                    border-left: 0px; border-bottom: 2px solid blue; border-top: 0px;
                                    padding-left: 10px; padding-right: 10px; font-size: 18px;">
                                &nbsp;&nbsp;&nbsp;
                                <input type="submit" value="ADD ITEM"
                                    style="width:100px; height: 45px; border:3px dashed red; background-color:
                                    white; border-radius: 10px;">
                            </form>
                        </td>
                    </tr>
                </table><br><br>
                <form action="/clear">
                    <input style="width:70%; height: 45px; border-radius: 15px; border: 3px dashed red; background-color: white; font-size: 20px;" type="submit" value="Reset">
                </form>
            </center>    
            """
            return html

    return redirect("/login")





price=0.0
@app.route("/add", methods=["POST"])
def add():
	global price
	username="Ali Raffay"
	h="""<br><table style="padding:10px; width: 70%; border: 2px dashed blue; min-height: 70px; background-color: white; border-radius: 30px;">"""
	itemno = request.form.get("item")
	with open("items.txt", "r") as file:
		multilines = file.readlines()
	for singleline in multilines:
		single = singleline.strip().split(",")
		if itemno == single[0]:
			price += float(single[4])
			with open("labels.txt", "r") as files:
				multiliness = files.readlines()
				for singleline in multiliness:
					labels = singleline.strip().split(",")
			for items, things in zip(single, labels):
				h =h+ """<tr><td style="padding: 10px; font-family: calibri; font-size: 22px; width: 50%;">"""+things+"""</td><td style="padding-right: 35px; font-family: calibri; font-size: 22px; width: 50%; text-align: right;">"""+items+"""</td></tr>
"""
			h=h+"""</table><br>"""
	with open("html.txt","a") as file:
		file.writelines(h)
	with open("html.txt") as file:
		multilinesx=file.read()
		multilinesx="""<center><table style="width: 70%; border: 2px dashed blue; min-height: 70px; background-color: white; border-radius: 30px;"><tr><td style="padding-left: 25px; font-family: calibri; font-size: 22px; width: 50%;">Recipient Name:</td><td style="padding-right: 35px; font-family: calibri; font-size: 22px; width: 50%; text-align: right;">"""+username+"""</td></tr>
</table>"""+multilinesx+"""<table style="width: 70%; border: 2px dashed blue; min-height: 70px; background-color: white; border-radius: 30px;"><tr><td style="padding-left: 25px; font-family: calibri; font-weight:bold; font-size: 22px; width: 50%;">Total Dues:</td><td style="padding-right: 35px; font-family: calibri; font-size: 22px; width: 50%; text-align: right;">"""+str(price)+"""</td></tr>
</table><br><br><form action="/dashboard"><input style="width:70%; height: 45px; border-radius: 15px; border: 3px dashed red; background-color: white; font-size: 20px;" type="submit" value="Add another item"></form><form action="/update"><input style="width:70%; height: 45px; border-radius: 15px; border: 3px dashed red; background-color: white; font-size: 20px;" type="submit" value="Add Discount"></form><form action="/clear"><input style="width:70%; height: 45px; border-radius: 15px; border: 3px dashed red; background-color: white; font-size: 20px;" type="submit" value="Reset"></form></center>"""
	return render_template_string(multilinesx)












@app.route("/update")
def update():
	username ="Ali Raffay"
	with open("html.txt") as file:
		multilinesx=file.read()
		multilinesx="""<center><table style="width: 70%; border: 2px dashed blue; min-height: 70px; background-color: white; border-radius: 30px;"><tr><td style="padding-left: 25px; font-family: calibri; font-size: 22px; width: 50%;">Recipient Name:</td><td style="padding-right: 35px; font-family: calibri; font-size: 22px; width: 50%; text-align: right;">"""+username+"""</td></tr>
</table>"""+multilinesx
	with open("html.txt","w") as file:
		file.writelines(multilinesx)

	return redirect("/discount")












@app.route("/discount")
def discount():
	with open("html.txt") as file:
		multilinesx=file.read()
	multilinesx=multilinesx+"""  <table style="width: 70%; border: 2px dashed blue; height: 70px; background-color: white; border-radius: 30px;"><tr><td style="padding-left: 25px; padding-bottom:0px; font-family: calibri; font-size: 22px; width: 50%;">Discount amount:</td><td style="padding-top:20px; height:45px; padding-bottom:0px; padding-right: 35px; font-family: calibri; font-size: 22px; width: 50%; text-align: right; border-top: 0px;"><form method="POST" action="/discc"><input name="discount" placeholder="Discount" style="width:60%; height: 45px; padding: 0px; border-right: 0px; border-left: 0px; border-bottom: 2px solid blue; border-top: 0px;  padding-left: 10px; padding-right: 10px; font-size: 18px;">&nbsp&nbsp&nbsp<input type="submit" value="ADD Discount" style="width:100px; height: 45px; border:2px dashed red; background-color: white; border-radius: 10px;"></form></td></tr>
</table>  """
	return render_template_string(multilinesx)







@app.route("/discc", methods=["GET","POST"])
def discc():
	global price
	discount = float(request.form.get("discount"))
	session["discount"]=discount
	dpr=price-discount
	with open("html.txt") as file:
		multilinesx=file.read()
		multilinesx=multilinesx+"""<table style="width: 70%; border: 2px dashed blue; min-height: 70px; background-color: #ffbace; border-radius: 30px;"><tr><td style="padding-left: 25px; font-family: calibri; font-size: 22px; width: 50%;">Discount Applied: </td><td style="padding-right: 35px; font-family: calibri; font-size: 22px; width: 50%; text-align: right;">""" +str(discount)+ """</td></tr>
</table><br><table style="width: 70%; border: 2px dashed blue; min-height: 70px; background-color: #ffea4d; border-radius: 30px;"><tr><td style="padding-left: 25px; font-family: calibri; font-size: 22px; width: 50%;">Total Dues: </td><td style="padding-right: 35px; font-family: calibri; font-size: 22px; width: 50%; text-align: right;">""" + str(dpr) + """</td></tr>
</table><br><form action="/discount"><input style="width:70%; height: 45px; border-radius: 15px; border: 3px dashed red; background-color: white; font-size: 20px;" type="submit" value="Change Discount Amount"></form><br><form action="/prin"><input style="width:70%; height: 45px; border-radius: 15px; border: 3px dashed red; background-color: white; font-size: 20px;" type="submit" value="Download PDF"></form><form action="/clearlist"><input style="width:70%; height: 45px; border-radius: 15px; border: 3px dashed red; background-color: white; font-size: 20px;" type="submit" value="Reset Receipt"></form>"""
	return multilinesx




@app.route("/prin", methods=["GET","POST"])
def prin():
	global price
	discount = session.get("discount")
	dpr=price-discount
	with open("html.txt") as file:
		multilinesx=file.read()
		multilinesx=multilinesx+"""<table style="width: 70%; border: 2px dashed blue; min-height: 70px; background-color: #ffbace; border-radius: 30px;"><tr><td style="padding-left: 25px; font-family: calibri; font-size: 22px; width: 50%;">Discount Applied: </td><td style="padding-right: 35px; font-family: calibri; font-size: 22px; width: 50%; text-align: right;">""" +str(discount)+ """</td></tr>
</table><br><table style="width: 70%; border: 2px dashed blue; min-height: 70px; background-color: #ffea4d; border-radius: 30px;"><tr><td style="padding-left: 25px; font-family: calibri; font-size: 22px; width: 50%;">Total Dues: </td><td style="padding-right: 35px; font-family: calibri; font-size: 22px; width: 50%; text-align: right;">""" + str(dpr) + """</td></tr>
</table>"""
	with open("html.txt","w") as file:
		file.writelines(multilinesx)
	HTML(string=multilinesx).write_pdf("invoice.pdf")
	return send_file("invoice.pdf", as_attachment=True, download_name="Invoice.pdf")




@app.route("/clear")
def clear():
	global price
	price=0.00
	h=""
	with open("html.txt","w") as file:
		file.write(h)
	session.clear()
	return redirect("/dashboard")


@app.route("/logout", methods=["POST"])
def logout():
	session.clear()
	return redirect("/login")

@app.route("/clearlist")
def clearlist():
	global price
	price=0.00
	h=""
	with open("html.txt","w") as file:
		file.write(h)
	return redirect("/dashboard")



if __name__ == "__main__":
	app.run(debug=True)
