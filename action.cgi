#!/usr/bin/perl
# Faroogh's personel pastebin service
# Copyright (C) 2017 FarooghKZ <farooghkz@openmailbox.org>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
#  any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.



@args = split /&/, $ENV{"QUERY_STRING"};
for $i (@args) {
    @t = split /=/, $i;
    if ($t[0] eq "text"){
        $text = $t[1]; #TODO: convert this to plain text
    }elsif ($t[0] eq "key"){
        $key = $t[1];
    }elsif ($t[0] eq "filename"){
        $filename = $t[1];
    }elsif ($t[0] eq "rtl" && $t[1] eq "on"){
        $rtl = 1;
    }
}
$MAX_TEXT_LEN = 1024;
$rtl_;

if ($rtl){
    $rtl_ = "text-direction: rtl; text-align: right";
}else{
    $rtl_ = "";
}

$sum_of_key = "sacA7YLUSAodg";
$index_page = "index.cgi";

print "Content-Type: text/html\n\n";
print "<html><head><title>Faroogh\'s personel pastebin</title></head><body>";

if (crypt($key, "salt") ne $sum_of_key){
    print "Sorry keys don\'t match!";
}elsif ($text.length() > $MAX_TEXT_LEN){
    print "Oversize!<br>Maximum file size: " . $MAX_TEXT_LEN . " Bytes<br>Your file size: " . $text.length();
}else{
    
    $r = open FH, ">" . $filename . ".html";
    if ($r != 0){
        print FH "<!doctype html><html><head><title>Faroogh\'s personel pastebin |  $filename  </title></head><body><a href=$index_page><h1>Faroogh's personel pastebin</h1></a><hr><code style=\"$rtl_\"><pre>";
        print FH $text;
        print FH "</pre></code><hr></body></html>";
        print FH "Faroogh\'s personel pastebin service is a Free/Open Source software. for more information and code see: <a href=\"license.html\">License page</a>. source code is available on <a href=\"http://github.com/\">Github</a>";
        close FH;
        print "Successful! filename: " . $filename . ".html";
    }else{
        print "Could not open " . $filename . " for writing!";
    }
}

print "</body></html>";
