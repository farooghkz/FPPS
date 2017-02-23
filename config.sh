#!/bin/sh


echo
echo =====  Welcome to Faroogh\'s pastebin configuration wizard  =====
read -p "What is administrator's email address of this pastebin? " email
read -p "What is your prefered key(you need this key to use your pastebin)? " key
echo please confirm\(y/n\)
echo email: $email
echo key: $key
read ans
if [ $ans = "y" ]; then
    cat no-key.html | sed -e s/admin@somewhere\.com/$email/;
    keyhash=$(perl -e 'print crypt $key, "salt"');
    cat action.cgi | sed -e s/sacA7YLUSAodg/$keyhash/;
    echo Done!
fi
