import pymysql
pymysql.version_info = (1, 3, 13, "final",0) #欺骗计算机，否则报错：mysqlclient 1.3.13 or newer is required; you have 0.9.3.
pymysql.install_as_MySQLdb() #否则会报错：Did you install mysqlclient?