#!/bin/bash
if [ $# -ne 2 ] 
then 
	echo "illegal number of parameters"; echo "you must provide an url to print and an uuid to generate the image"
	exit 1
else
	url=$1
	id=$2
	my_img="/tmp/$id.png"
fi

echo "generating image $my_img for $url "


echo "var timeout = 500; console.log('opening  $url '  ); var page = require('webpage').create(); page.open( '$url' , ">/tmp/sc.js
echo "function (status) {     if (status !== 'success') {         console.log('Unable to load the address!');    phantom.exit(); " >>/tmp/sc.js
echo "   } else {         window.setTimeout(function () {             page.render( '$my_img' );  phantom.exit();     }, timeout );  } }); ">>/tmp/sc.js



phantomjs /tmp/sc.js



