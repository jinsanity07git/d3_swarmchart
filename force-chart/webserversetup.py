cd C:\Users\zihao\github\d3_swarmchart
## change drive in cmd
D:
cd D:\test\github

python -m http.server



#https://stackoverflow.com/questions/10752055/cross-origin-requests-are-only-supported-for-http-error-when-loading-a-local

'''
Python 2
If you have Python installed...

1.Change directory into the folder where your file some.html or file(s) exist using the command cd /path/to/your/folder

2.Start up a Python web server using the command 
python -m SimpleHTTPServer 8000

This will start a web server that hosts your entire directory listing, 
which will be made accessible through the following URL: http://localhost:8000

You can use a custom port  python -m SimpleHTTPServer 9000 giving you link: http://localhost:9000
This approach is built in to any Python installation.

Python 3
Do the same steps, but use the following command instead python3 -m http.server
'''


