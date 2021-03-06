#!/bin/bash

for f in $@; do
    luac -l -p $f | egrep ETGLOBAL | \
    awk '{print "'$f' " $2 " " $7}' | \
    ( ! egrep -v \
    '] (string|xpcall|package|tostring|print|os|unpack|require|getfenv|setmetatable|next|assert|tonumber|io|rawequal|collectgarbage|getmetatable|module|rawset|math|debug|pcall|table|newproxy|type|coroutine|_G|select|gcinfo|pairs|rawget|loadstring|ipairs|_VERSION|dofile|setfenv|load|error|loadfile)$' )
done
