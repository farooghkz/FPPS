#!/usr/bin/perl
# Faroogh's personel pastebin service
# Copyright (C) 2017  FarooghKZ <farooghkz@spams_come_here.openmailbox.org>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
#  any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.


$RANDOM_NUMBER  = int(rand() * 1000);

print "Content-Type: text/html\n\n";

print <<'END';
<!doctype html>
<html>
    <head>
        <title>Faroogh's personel pastebin</title>
    </head>
    <body style="background-color: #cedbe5">
        <h1>Faroogh's personel pastebin</h1>
        <hr>
        <form name="frm" action="action.cgi" method="get">
        Text:<br>
        <textarea name="text" style="width:300px ;height:100px"></textarea><br>
        <table>
        <tr><td>Key:</td><td><input name="key"></td></tr>
        <tr><td>Filename:</td><td><input name="filename" value="
END
print $RANDOM_NUMBER;
print <<'END';
"></td></tr> 
        </table>
        <span style="color:red">WARNING!</span> All pastebins are public.<br>
        <a href="no-key.html">Don't have a key?</a><br>
        <input type="checkbox" name="rtl" label="RTL?"><br>
        <input type="submit" value="Submit">
        <hr>
        </form>
        Faroogh's personel pastebin service is a Free/Open Source software. for more information and code see: <a href="license.html">License page</a>. source code is available on <a href="http://github.com/">Github</a>
    </body>
</html>
END
