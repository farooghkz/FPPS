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


sub get_sum_of_key ($){
    #TODO: use a prepared algorithm or make one yourself!
    return "";
}

#TODO: change these, use ENV hash
$text = "jfd";
$key = "key";
$filename = "file.exe";
$MAX_TEXT_LEN = 1024;
$rtl = 0;
$rtl_;

if ($rtl){
    $rtl_ = "rtl";
}else{
    $rtl_ = "ltr";
}

$sum_of_key = "";
$index_page = "index.cgi";

print "Content-Type: text/html\n\n";
print "<html><head><title>Faroogh\'s personel pastebin</title></head><body>";

if (get_sum_of_key(key) ne $sum_of_key){
    print "Sorry keys don\'t match!";
}elsif ($text.length() > $MAX_TEXT_LEN){
    print "Oversize!<br>Maximum file size: " . $MAX_TEXT_LEN . " Bytes<br>Your file size: " . $text.length();
}else{
    
    $r = open FH, ">" . $filename . "html";
    if ($r != 0){
        print FH "<!doctype html><html><head><title>Faroogh\'s personel pastebin |  $filename  </title></head><body><a href=$index_page><h1>Faroogh's personel pastebin</h1></a><hr><code style=\"$rtl_\"><pre>";
        print FH $text;
        print FH "</pre></code></body></html>";
        close FH;
        print "Successful! filename: " . filename;
    }else{
        print "Could not open " . filename . " for writing!";
    }
}

print "</body></html>";





